# Generated by Django 2.0.3 on 2018-03-22 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearchapp', '0002_auto_20180322_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadpost',
            name='corporate_phone_number',
        ),
    ]
