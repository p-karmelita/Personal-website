# Generated by Django 4.2.6 on 2023-10-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mysite", "0003_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
