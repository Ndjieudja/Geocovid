# Generated by Django 2.2.20 on 2021-05-10 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0004_auto_20210509_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidTest',
            fields=[
                ('covididtest', models.CharField(auto_created=True, default='None', max_length=15, unique=True)),
                ('id_code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name_hospital', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('result_test', models.CharField(max_length=10)),
            ],
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]