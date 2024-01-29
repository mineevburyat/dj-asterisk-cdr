import csv
import os
from pathlib import Path

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand
from django.utils import timezone

from readcsv.models import CDR_details, CDR_Record_Uniq


def clear_nonutf_csv_file(filename, tmp_file="clear_file.tmp"):
    with open(tmp_file, "w") as tmpfile:
        with open(filename, "br") as masterfile:
            while True:
                ch = masterfile.read(100)
                if not ch:
                    break
                line = ch.decode('utf-8', 'ignore')
                tmpfile.write(line)


def list_files(path):
    files = []
    with os.scandir(path) as gen_f:
        for item in gen_f:
            if item.is_file():
                files.append(item.name)
    return files


def extract_from_csv(filename):
    tmp_f = "clear_file.tmp"
    clear_nonutf_csv_file(filename, tmp_f)
    with open(tmp_f, newline='', encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in lines:
            yield (
                {'from_phone': row[1],
                 'to_phone': row[2],
                 'context': row[3],
                 'in_channel': row[5],
                 'out_channel': row[6],
                 'lastapp': f"{row[7].upper()}({row[8]})",
                 'start_ring': row[9],
                 'answer_ring': row[10] if row[10] else None,
                 'end_ring': row[11],
                 'duration_channel': row[12],
                 'duration_speech': row[13],
                 'status': row[14],
                 'amaflag': row[15],
                 'uniquedid': row[16]
                 })
    os.remove(tmp_f)


class Command(BaseCommand):
    help = 'Import master.csv to django base with audio files'

    def handle(self, *args, **options):
        path_to_diraudio = '/home/mineev/dj-asterisk-cdr/monitor'
        path_to_csv_file = '/home/mineev/dj-asterisk-cdr/Master.csv'
        audio_file_names = list_files(path_to_diraudio)
        for csvitem in extract_from_csv(path_to_csv_file):
            path_to_audio = None
            for name in audio_file_names:
                if name.find(csvitem.get('uniquedid')) != -1:
                    path_to_audio = path_to_diraudio + '/' + name
                    self.stdout.write(
                        f"найден аудиофайл {path_to_audio}")
                    break
            if path_to_audio:
                f = open(path_to_audio, 'rb')
                path = default_storage.save(f'media/{name}', File(f))
            else:
                path = None
            try:
                cdr_uniq = CDR_Record_Uniq.objects.get(
                    uniquedid=csvitem.get('uniquedid').split('.')[0])
                self.stdout.write(f'найдена запись {cdr_uniq.uniquedid}')
                if path:
                    cdr_uniq.file_audio = path
                    cdr_uniq.save()
                    self.stdout.write('дописал файл аудиозаписи')
            except ObjectDoesNotExist:
                cdr_uniq = CDR_Record_Uniq.objects.create(
                    uniquedid=csvitem['uniquedid'].split('.')[0],
                    from_phone=csvitem['from_phone'],
                    to_phone=csvitem['to_phone'],
                    context=csvitem['context'],
                    in_channel=csvitem['in_channel'],
                    file_audio=path)
                self.stdout.write(f"создана запись {cdr_uniq}")
            try:
                cdr_detail = CDR_details.objects.get(
                    out_channel=csvitem['out_channel'],
                    lastapp=csvitem['lastapp'],
                    start_ring=csvitem['start_ring'],
                    answer_ring=csvitem['answer_ring'],
                    end_ring=csvitem['end_ring'],
                    duration_channel=csvitem['duration_channel'],
                    duration_speech=csvitem['duration_speech'],
                    status=csvitem['status'],
                    cdr=cdr_uniq)
                self.stdout.write('найдена запись детализации.пропускаю')
            except ObjectDoesNotExist:
                cdr_detail = CDR_details.objects.create(
                    out_channel=csvitem['out_channel'],
                    lastapp=csvitem['lastapp'],
                    start_ring=csvitem['start_ring'],
                    answer_ring=csvitem['answer_ring'],
                    end_ring=csvitem['end_ring'],
                    duration_channel=csvitem['duration_channel'],
                    duration_speech=csvitem['duration_speech'],
                    status=csvitem['status'],
                    cdr=cdr_uniq)
                self.stdout.write(
                    f"создана детализация {cdr_detail.cdr.uniquedid}")
