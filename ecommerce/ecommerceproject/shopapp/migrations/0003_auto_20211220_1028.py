# Generated by Django 3.2.9 on 2021-12-20 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_auto_20211220_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]
