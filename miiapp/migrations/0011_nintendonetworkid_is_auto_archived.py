# Generated by Django 4.1.7 on 2023-10-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miiapp', '0010_alter_nintendonetworkid_archived_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nintendonetworkid',
            name='is_auto_archived',
            field=models.BooleanField(default=True),
        ),
    ]
