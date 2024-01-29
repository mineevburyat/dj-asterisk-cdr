from django.db import models

# Create your models here.

class BillingContext(models.Model):
    name = models.CharField(
        verbose_name='контекст',
        max_length=30
    )
    description = models.TextField(
        verbose_name='описание контекста',
        max_length=300
    )
    
# {'from_phone': row[1],
#                  'to_phone': row[2],
#                  'context': row[3],
#                  'in_channel': row[5],
#                  'out_channel': row[6],
#                  'lastapp': f"{row[7].upper()}({row[8]})",
#                  'start_ring': row[9],
#                  'answer_ring': row[10] if row[10] else None,
#                  'end_ring': row[11],
#                  'duration_channel': row[12],
#                  'duration_speech': row[13],
#                  'status': row[14],
#                  'amaflag': row[15],
#                  'uniquedid': row[16]
#                  })

class RowCallDetaiRecord(models.Model):
    uniquedid = models.CharField(
        verbose_name='идентификатор вызова',
        max_length=30,
        unique=True
    )
    from_phone = models.CharField(
        max_length=16,
        verbose_name='Откуда'
    )
    to_phone = models.CharField(
        max_length=7,
        verbose_name='Куда'
    )
    context = models.CharField(
        max_length=80,
        verbose_name='контекст'
    )
    in_channel = models.CharField(
        verbose_name='входящий канал',
        max_length=80
    )
    out_channel = models.CharField(
        verbose_name='исходящий канал',
        max_length=80,
        blank=True,
        null=True
    )
    lastapp = models.CharField(
        verbose_name='последня команда',
        max_length=120
    )
    start_ring = models.DateTimeField(
        verbose_name='начало вызова'
    )
    answer_ring = models.DateTimeField(
        verbose_name='ответ на вызов',
        blank=True,
        null=True
    )
    end_ring = models.DateTimeField(
        verbose_name='завершение вызова'
    )
    duration_channel = models.IntegerField(
        verbose_name='Длительность всего вызова'
    )
    duration_speech = models.IntegerField(
        verbose_name='Длительность разговора'
    )
    status = models.CharField(
        verbose_name='статус',
        max_length=13
    )
    file_audio = models.FileField(
        verbose_name='Запись разговора',
        upload_to='monitor',
        blank=True,
        null=True,
    )
    
    def is_audio(self):
        return True if self.file_audio else False
    
    def is_audio_str(self):
        return 'yes' if self.is_audio() else 'no'

    def __str__(self):
        audio = self.is_audio_str()
        return f"{self.from_phone} to {self.to_phone} (audio {audio})"

# class CDR_Uniq(models.Model):
#     uniquedid = models.CharField(
#         verbose_name='идентификатор вызова',
#         max_length=15,
#         unique=True
#     )
#     from_phone = models.CharField(
#         max_length=16,
#         verbose_name='Откуда'
#     )
#     to_phone = models.CharField(
#         max_length=7,
#         verbose_name='Куда'
#     )
#     context = models.CharField(
#         max_length=80,
#         verbose_name='контекст'
#     )
#     file_audio = models.FileField(
#         verbose_name='Запись разговора',
#         upload_to='monitor',
#         blank=True,
#         null=True,
#     )

#     def is_audio(self):
#         return True if self.file_audio else False
    
#     def is_audio_str(self):
#         return 'yes' if self.is_audio() else 'no'

#     def __str__(self):
#         audio = self.is_audio_str()
#         return f"{self.from_phone} to {self.to_phone} (audio {audio})"


# class CDR_details(models.Model):
#     uniquedid = models.CharField(
#         verbose_name='идентификатор вызова',
#         max_length=15,
#         unique=True
#     )
#     to = models.CharField(
#         max_length=7,
#         verbose_name='Куда'
#     )
#     in_channel = models.CharField(
#         verbose_name='входящий канал',
#         max_length=80
#     )
#     out_channel = models.CharField(
#         verbose_name='исходящий канал',
#         max_length=80,
#         blank=True,
#         null=True
#     )
#     lastapp = models.CharField(
#         verbose_name='последня команда',
#         max_length=120
#     )
#     start_ring = models.DateTimeField(
#         verbose_name='начало вызова'
#     )
#     answer_ring = models.DateTimeField(
#         verbose_name='ответ на вызов',
#         blank=True,
#         null=True
#     )
#     end_ring = models.DateTimeField(
#         verbose_name='завершение вызова'
#     )
#     duration_channel = models.IntegerField(
#         verbose_name='Длительность всего вызова'
#     )
#     duration_speech = models.IntegerField(
#         verbose_name='Длительность разговора'
#     )
#     status = models.CharField(
#         verbose_name='статус',
#         max_length=13
#     )
#     cdr = models.ForeignKey(
#         CDR_Record_Uniq,
#         verbose_name='детализация связана с:',
#         on_delete=models.PROTECT
#     )
