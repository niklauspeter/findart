# Generated by Django 4.2.4 on 2023-09-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='starting_bid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
