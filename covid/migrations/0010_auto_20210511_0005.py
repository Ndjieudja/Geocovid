# Generated by Django 2.2.20 on 2021-05-11 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0009_auto_20210510_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='gender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='covid.Gender'),
        ),
    ]