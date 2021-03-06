# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Cidade', 'verbose_name_plural': 'Cidades'},
        ),
        migrations.AlterModelOptions(
            name='neighborhood',
            options={'verbose_name': 'Bairro', 'verbose_name_plural': 'Bairros'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Imóvel', 'verbose_name_plural': 'Imóveis'},
        ),
        migrations.AddField(
            model_name='property',
            name='num_record',
            field=models.IntegerField(null=True, verbose_name='ficha'),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='endereço'),
        ),
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.CharField(blank=True, max_length=30, verbose_name='área'),
        ),
        migrations.AlterField(
            model_name='property',
            name='conditions',
            field=models.CharField(blank=True, max_length=50, verbose_name='condições'),
        ),
        migrations.AlterField(
            model_name='property',
            name='in_front_of',
            field=models.TextField(blank=True, verbose_name='em frente a'),
        ),
        migrations.AlterField(
            model_name='property',
            name='intent',
            field=models.CharField(choices=[('alugar', 'Alugar'), ('comprar', 'Comprar')], max_length=10, verbose_name='finalidade'),
        ),
        migrations.AlterField(
            model_name='property',
            name='obs',
            field=models.TextField(blank=True, verbose_name='observações'),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('casa', 'Casa'), ('apartamento', 'Apartamento'), ('comercial', 'Comercial'), ('terreno', 'Terreno')], max_length=15, verbose_name='tipo de propriedade'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_bathroom',
            field=models.IntegerField(default=0, verbose_name='banheiros'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_bedroom',
            field=models.IntegerField(default=0, verbose_name='dormitórios'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_coffe_room',
            field=models.IntegerField(default=0, verbose_name='copas'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_dining_room',
            field=models.IntegerField(default=0, verbose_name='salas de refeição'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_garage',
            field=models.IntegerField(default=0, verbose_name='garagens'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_hall',
            field=models.IntegerField(default=0, verbose_name='halls'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_kitchen',
            field=models.IntegerField(default=0, verbose_name='cozinhas'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_lavatory',
            field=models.IntegerField(default=0, verbose_name='lavabos'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_leisure_area',
            field=models.IntegerField(default=0, verbose_name='ranchos'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_living_room',
            field=models.IntegerField(default=0, verbose_name='salas de estar'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_maids_room',
            field=models.IntegerField(default=0, verbose_name='dormitórios de empregada'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_maids_wc',
            field=models.IntegerField(default=0, verbose_name='banheiros de empregada'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_office',
            field=models.IntegerField(default=0, verbose_name='escritórios'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_other',
            field=models.IntegerField(default=0, verbose_name='outros'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_pantry',
            field=models.IntegerField(default=0, verbose_name='despensas'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_service_area',
            field=models.IntegerField(default=0, verbose_name='áreas de serviço'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_suite',
            field=models.IntegerField(default=0, verbose_name='suítes'),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_tv_room',
            field=models.IntegerField(default=0, verbose_name='salas de tv'),
        ),
    ]
