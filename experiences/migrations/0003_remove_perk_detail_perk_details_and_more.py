# Generated by Django 4.1.1 on 2022-10-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0002_rename_experiences_experience"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="perk",
            name="detail",
        ),
        migrations.AddField(
            model_name="perk",
            name="details",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="perk",
            name="explanation",
            field=models.TextField(blank=True, null=True),
        ),
    ]
