# Generated by Django 3.1.3 on 2020-12-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bagiapi', '0010_auto_20201130_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='materi',
        ),
        migrations.AddField(
            model_name='course',
            name='deskripsi',
            field=models.TextField(blank=True, null=True),
        ),
    ]