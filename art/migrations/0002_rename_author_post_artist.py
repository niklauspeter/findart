# Generated by Django 4.2.4 on 2023-09-01 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='Artist',
        ),
    ]
