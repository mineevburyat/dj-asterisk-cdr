import csv
import os


# clear file from non utf char
def clear_nonutf_csv_file(filename, tmp_file="clear_file.tmp"):
    with open(tmp_file, "w") as tmpfile:
        with open(filename, "br") as masterfile:
            while True:
                ch = masterfile.read(100)
                if not ch:
                    break
                line = ch.decode("utf-8", "ignore")
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
    with open(tmp_f, newline="", encoding="utf-8") as csvfile:
        lines = csv.reader(csvfile, delimiter=",", quotechar='"')
        for row in lines:
            yield (
                {
                    "from_phone": row[1],
                    "to_phone": row[2],
                    "context": row[3],
                    "in_channel": row[5],
                    "out_channel": row[6],
                    "lastapp": f"{row[7].upper()}({row[8]})",
                    "start_ring": row[9],
                    "answer_ring": row[10] if row[10] else None,
                    "end_ring": row[11],
                    "duration_channel": row[12],
                    "speach_duration": row[13],
                    "status": row[14],
                    "amaflag": row[15],
                    "uniqueid": row[16],
                }
            )
    os.remove(tmp_f)


file_names = list_files("./monitor")
for item in extract_from_csv("Master.csv"):
    for name in file_names:
        if name.find(item.get("uniqueid")) != -1:
            print(item)
            print(name)

"""
['', '89245555937', '211474', 'stadion-pstn', '"89245555937" <89245555937>', 'SIP/211474-00000001', '', 'Hangup', '', '2024-01-27 15:27:58', '2024-01-27 15:27:58', '2024-01-27 15:28:25', '27', '27', 'ANSWERED', 'DOCUMENTATION', '1706369278.2', '', '', '1706369278.2', '1']

['', '89245555937', 'ch2', 'TimeDelay', '"89245555937" <89245555937>', 'Local/ch2@TimeDelay-00000001;2', 'SIP/stadionpbx-00000008', 'Dial', 'SIP/154@stadionpbx,30', '2024-01-27 16:16:36', '', '2024-01-27 16:17:16', '40', '0', 'NO ANSWER', 'DOCUMENTATION', '1706372196.16', '', '', '1706372196.12', '12'] - 21

['', '81079246516548', '211553', 'stadion-pstn', '"8107924651b" <81079246516548>', 'SIP/211553-0000001c', 'SIP/stadionpbx-0000001e', 'Dial', 'SIP/301&SIP/200@stadionpbx,60,t', '2024-01-28 04:10:46', '2024-01-28 04:10:52', '2024-01-28 04:11:23', '36', '30', 'ANSWERED', 'DOCUMENTATION', '1706415046.98', '', '', '1706415046.98', '82'] - 21

['', '89024577388', '211553', 'stadion-pstn', '"89024577388" <89024577388>', 'SIP/211553-00000017', 'Local/ch2@TimeDelay-0000000d;1', 'Dial', 'Local/ch1@TimeDelay&Local/ch2@TimeDelay&Local/ch3@TimeDelay,40', '2024-01-28 03:34:53', '', '2024-01-28 03:34:57', '4', '0', 'NO ANSWER', 'DOCUMENTATION', '1706412893.79', '', '', '1706412893.79', '71']

1) ['', '89024577388', '211553', 'stadion-pstn', '"89024577388" <89024577388>', 'SIP/211553-00000017', 'Local/ch1@TimeDelay-0000000c;1', 'Dial', 'Local/ch1@TimeDelay&Local/ch2@TimeDelay&Local/ch3@TimeDelay,40', '2024-01-28 03:34:53', '2024-01-28 03:34:57', '2024-01-28 03:34:57', '4', '0', 'ANSWERED', 'DOCUMENTATION', '1706412893.79', '', '', '1706412893.79', '64']
['', '89024577388', '211553', 'stadion-pstn', '"89024577388" <89024577388>', 'SIP/211553-00000017', 'SIP/301-00000018', 'Dial', 'Local/ch1@TimeDelay&Local/ch2@TimeDelay&Local/ch3@TimeDelay,40', '2024-01-28 03:34:57', '2024-01-28 03:34:57', '2024-01-28 03:36:17', '79', '79', 'ANSWERED', 'DOCUMENTATION', '1706412893.79', '', '', '1706412893.79', '74']
['', '89024577388', '211553', 'stadion-pstn', '"89024577388" <89024577388>', 'SIP/211553-00000017', 'Local/ch2@TimeDelay-0000000d;1', 'Dial', 'Local/ch1@TimeDelay&Local/ch2@TimeDelay&Local/ch3@TimeDelay,40', '2024-01-28 03:34:53', '', '2024-01-28 03:34:57', '4', '0', 'NO ANSWER', 'DOCUMENTATION', '1706412893.79', '', '', '1706412893.79', '71']
['', '89024577388', '211553', 'stadion-pstn', '"89024577388" <89024577388>', 'SIP/211553-00000017', 'Local/ch3@TimeDelay-0000000e;1', 'Dial', 'Local/ch1@TimeDelay&Local/ch2@TimeDelay&Local/ch3@TimeDelay,40', '2024-01-28 03:34:53', '', '2024-01-28 03:34:57', '4', '0', 'NO ANSWER', 'DOCUMENTATION', '1706412893.79', '', '', '1706412893.79', '72']

2) ['', '89024577388', 'ch1', 'TimeDelay', '"89024577388" <89024577388>', 'Local/ch1@TimeDelay-0000000c;2', 'SIP/301-00000018', 'Dial', 'SIP/301,15', '2024-01-28 03:34:53', '2024-01-28 03:34:57', '2024-01-28 03:34:57', '4', '0', 'ANSWERED', 'DOCUMENTATION', '1706412893.81', '', '', '1706412893.79', '66']


3) 
"""
