# Generated by Django 4.0.2 on 2022-02-23 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labresult',
            old_name='result',
            new_name='data',
        ),
    ]
