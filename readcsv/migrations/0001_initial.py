# Generated by Django 5.0.1 on 2024-01-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BillingContext",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="контекст")),
                (
                    "description",
                    models.TextField(max_length=300, verbose_name="описание контекста"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RowCallDetaiRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uniquedid",
                    models.CharField(
                        max_length=15, unique=True, verbose_name="идентификатор вызова"
                    ),
                ),
                ("from_phone", models.CharField(max_length=16, verbose_name="Откуда")),
                ("to_phone", models.CharField(max_length=7, verbose_name="Куда")),
                ("context", models.CharField(max_length=80, verbose_name="контекст")),
                (
                    "in_channel",
                    models.CharField(max_length=80, verbose_name="входящий канал"),
                ),
                (
                    "out_channel",
                    models.CharField(
                        blank=True,
                        max_length=80,
                        null=True,
                        verbose_name="исходящий канал",
                    ),
                ),
                (
                    "lastapp",
                    models.CharField(max_length=120, verbose_name="последня команда"),
                ),
                ("start_ring", models.DateTimeField(verbose_name="начало вызова")),
                (
                    "answer_ring",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="ответ на вызов"
                    ),
                ),
                ("end_ring", models.DateTimeField(verbose_name="завершение вызова")),
                (
                    "duration_channel",
                    models.IntegerField(verbose_name="Длительность всего вызова"),
                ),
                (
                    "duration_speech",
                    models.IntegerField(verbose_name="Длительность разговора"),
                ),
                ("status", models.CharField(max_length=13, verbose_name="статус")),
                (
                    "file_audio",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="monitor",
                        verbose_name="Запись разговора",
                    ),
                ),
            ],
        ),
    ]
