# Generated by Django 5.0.7 on 2024-08-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0007_alter_articlepost_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="articlepost",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
