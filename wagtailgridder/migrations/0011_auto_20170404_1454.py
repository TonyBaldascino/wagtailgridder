# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailgridder', '0010_auto_20170403_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='griditem',
            name='description_video',
            field=models.URLField(blank=True, help_text='This video will be embedded in the expanded area when populated.', null=True),
        ),
        migrations.AlterField(
            model_name='gridindexpage',
            name='featured_description',
            field=models.TextField(blank=True, help_text='Text to be displayed below the hero image next to the featured items.', null=True),
        ),
        migrations.AlterField(
            model_name='gridindexpage',
            name='featured_grid_item_1',
            field=models.ForeignKey(blank=True, help_text='First featured grid item underneath the hero image.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailgridder.GridItem', verbose_name='Featured Item One'),
        ),
        migrations.AlterField(
            model_name='gridindexpage',
            name='featured_grid_item_2',
            field=models.ForeignKey(blank=True, help_text='Second featured grid item underneath the hero image.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailgridder.GridItem', verbose_name='Featured Item Two,'),
        ),
        migrations.AlterField(
            model_name='gridindexpage',
            name='hero_background_image',
            field=models.ForeignKey(blank=True, help_text='The background image for the hero section. This triggers the section to be displayed if an image is selected.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='gridindexpage',
            name='hero_button_text',
            field=models.CharField(blank=True, help_text='Text for the call-to-action button beneath the text and logo over the background image.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='gridindexpage',
            name='hero_button_url',
            field=models.CharField(blank=True, help_text='URL for the call-to-action button beneath the text and logo over the background image.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='gridindexpage',
            name='hero_description',
            field=models.TextField(blank=True, help_text='Text to be displayed beneath the logo over the background image.', null=True),
        ),
        migrations.AlterField(
            model_name='gridindexpage',
            name='hero_logo_image',
            field=models.ForeignKey(blank=True, help_text='The logo image to be displayed over the background image.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='griditem',
            name='description_image',
            field=models.ForeignKey(blank=True, help_text='This image will appear in the expanded area when populated.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='griditem',
            name='description_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='This description will appear in the expanded area when populated.', null=True, verbose_name='Full Description'),
        ),
        migrations.AlterField(
            model_name='griditem',
            name='landing_page_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text="This is the text which will appear on the grid item's landing page.", null=True, verbose_name='Landing Page Text'),
        ),
    ]