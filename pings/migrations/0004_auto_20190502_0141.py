# Generated by Django 2.2 on 2019-05-02 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pings', '0003_auto_20190502_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ping',
            old_name='greeting',
            new_name='subject',
        ),
    ]
