# Generated by Django 4.2.15 on 2025-03-29 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("perspectives", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="perspective",
            name="subject",
            field=models.CharField(default="Default Subject", max_length=255),
        ),
        migrations.AlterField(
            model_name="perspective",
            name="category",
            field=models.CharField(
                choices=[("cultural", "Cultural"), ("technic", "Technic"), ("subjective", "Subjective")],
                default="subjective",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="perspective",
            name="text",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="perspective",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
