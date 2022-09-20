# Generated by Django 4.1.1 on 2022-09-19 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tmsapp', '0004_ticket2_delete_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket2',
            name='ticketholder',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]