# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 18:13
from __future__ import unicode_literals

from django.db import migrations


def build_dst(src, destination, property_type):
    dst = None
    if property_type == 'house':
        dst = destination(
            created_at=src.created_at,
            updated_at=src.updated_at,
            featured=src.featured,
            num_record=src.num_record,
            intent=src.intent,
            obs=src.obs,
            price=src.price,
            city=src.city,
            neighborhood=src.neighborhood,
            user=src.user,
            conditions=src.conditions,
            address=src.address,
            total_bedroom=src.total_bedroom,
            total_maids_room=src.total_maids_room,
            total_maids_wc=src.total_maids_wc,
            total_lavatory=src.total_lavatory,
            total_room=src.total_room,
            total_kitchen=src.total_kitchen,
            total_hall=src.total_hall,
            total_service_area=src.total_service_area,
            total_leisure_area=src.total_leisure_area,
            total_suite=src.total_suite,
            total_bathroom=src.total_bathroom,
            total_coffe_room=src.total_coffe_room,
            total_pantry=src.total_pantry,
            total_office=src.total_office,
            total_garage=src.total_garage,
        )
    elif property_type == 'apartment':
        dst = destination(
            created_at=src.created_at,
            updated_at=src.updated_at,
            featured=src.featured,
            num_record=src.num_record,
            intent=src.intent,
            obs=src.obs,
            price=src.price,
            conditions=src.conditions,
            city=src.city,
            neighborhood=src.neighborhood,
            user=src.user,
            address=src.address,
            area=src.area,
            total_bedroom=src.total_bedroom,
            total_maids_room=src.total_maids_room,
            total_maids_wc=src.total_maids_wc,
            total_lavatory=src.total_lavatory,
            total_room=src.total_room,
            total_kitchen=src.total_kitchen,
            total_hall=src.total_hall,
            total_service_area=src.total_service_area,
            total_suite=src.total_suite,
            total_bathroom=src.total_bathroom,
            total_coffe_room=src.total_coffe_room,
            total_pantry=src.total_pantry,
            total_office=src.total_office,
            total_garage=src.total_garage,
        )
    elif property_type == 'commercial':
        dst = destination(
            created_at=src.created_at,
            updated_at=src.updated_at,
            featured=src.featured,
            num_record=src.num_record,
            intent=src.intent,
            obs=src.obs,
            price=src.price,
            conditions=src.conditions,
            city=src.city,
            neighborhood=src.neighborhood,
            user=src.user,
            address=src.address,
            area=src.area,
            total_room=src.total_room,
            total_kitchen=src.total_kitchen,
            total_office=src.total_office,
            total_bathroom=src.total_bathroom,
            total_garage=src.total_garage,
            total_service_area=src.total_service_area,
        )
    elif property_type == 'land':
        dst = destination(
            created_at=src.created_at,
            updated_at=src.updated_at,
            featured=src.featured,
            num_record=src.num_record,
            intent=src.intent,
            obs=src.obs,
            price=src.price,
            conditions=src.conditions,
            city=src.city,
            neighborhood=src.neighborhood,
            user=src.user,
            address=src.address,
            area=src.area,
        )
    return dst


def copy_source_to_destination(apps, model_src, model_dst, property_type):
    source = apps.get_model('properties', model_src)
    destination = apps.get_model('properties', model_dst)

    content_type = apps.get_model('contenttypes', 'ContentType')
    source_content_type = content_type.objects.get_for_model(source)
    destination_content_type = content_type.objects.get_for_model(destination)

    photo = apps.get_model('properties', 'Photo')

    for src in source.objects.all():
        dst = build_dst(src, destination, property_type)
        dst.save()

        photos = photo.objects.filter(content_type_id=source_content_type.id)
        for photo_item in photos:
            photo_item.content_type_id = destination_content_type.id
            photo_item.object_id = dst.id
            photo_item.save()

        src.delete()


def forward_abc_to_mti(apps, schema_editor):
    models = [('HouseOld', 'House', 'house'),
              ('ApartmentOld', 'Apartment', 'apartment'),
              ('CommercialOld', 'Commercial', 'commercial'),
              ('LandOld', 'Land', 'land')]
    for model_src, model_dst, property_type in models:
        copy_source_to_destination(apps, model_src, model_dst, property_type)


def backward_abc_to_mti(apps, schema_editor):
    models = [('House', 'HouseOld', 'house'),
              ('Apartment', 'ApartmentOld', 'apartment'),
              ('Commercial', 'CommercialOld', 'commercial'),
              ('Land', 'LandOld', 'land')]
    for model_src, model_dst, property_type in models:
        copy_source_to_destination(apps, model_src, model_dst, property_type)


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_auto_20170630_1643'),
    ]

    operations = [
        migrations.RunPython(forward_abc_to_mti,
                             backward_abc_to_mti)
    ]
