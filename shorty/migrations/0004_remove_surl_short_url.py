# Generated by Django 4.1.7 on 2023-02-27 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorty', '0003_alter_surl_alias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surl',
            name='short_url',
        ),
    ]
