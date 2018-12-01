# Generated by Django 2.0 on 2018-12-01 16:49
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confidentiality',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True, serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('total_docs', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True, serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                ('size', models.PositiveIntegerField()),
                (
                    'doc_file', models.FileField(
                        storage='/uploads',
                        upload_to='',
                    ),
                ),
                (
                    'confidentiality', models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to='api.Confidentiality',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True, serialize=False, verbose_name='ID',
                    ),
                ),
                ('total_docs', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True, serialize=False, verbose_name='ID',
                    ),
                ),
                ('total_docs', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('short', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='filetype',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='api.FileType',
            ),
        ),
        migrations.AddField(
            model_name='document',
            name='language',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='api.Language',
            ),
        ),
    ]
