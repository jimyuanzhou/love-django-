# Generated by Django 3.1 on 2021-09-08 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='vairation_value',
            new_name='variation_value',
        ),
    ]
