# Generated by Django 4.1.1 on 2022-09-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='id',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(default='000001', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]