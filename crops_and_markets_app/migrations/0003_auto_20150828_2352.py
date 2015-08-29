# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crops_and_markets_app', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact_number_1', models.IntegerField(null=True, blank=True)),
                ('contact_number_2', models.IntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('observations', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComercialInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zone', models.CharField(max_length=256, null=True, blank=True)),
                ('volume', models.CharField(max_length=256, null=True, blank=True)),
                ('varieties', models.CharField(max_length=256, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeographicInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.CharField(max_length=256, null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitud', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Geobject',
        ),
        migrations.AddField(
            model_name='client',
            name='comercial_info',
            field=models.ForeignKey(to='crops_and_markets_app.ComercialInfo'),
        ),
        migrations.AddField(
            model_name='client',
            name='type_of_client',
            field=models.ForeignKey(to='crops_and_markets_app.TypeOfClient'),
        ),
    ]
