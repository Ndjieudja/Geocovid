# Generated by Django 2.2.20 on 2021-05-09 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('covididtest', models.CharField(auto_created=True, default='None', max_length=15, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='static/')),
                ('name', models.CharField(max_length=20)),
                ('id_code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name_hospital', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('result_test', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
    ]
