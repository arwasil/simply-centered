# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Category.slug'
        db.alter_column('main_category', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))
        # Adding index on 'Category', fields ['slug']
        db.create_index('main_category', ['slug'])

        # Adding unique constraint on 'Category', fields ['slug']
        db.create_unique('main_category', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Category', fields ['slug']
        db.delete_unique('main_category', ['slug'])

        # Removing index on 'Category', fields ['slug']
        db.delete_index('main_category', ['slug'])


        # Changing field 'Category.slug'
        db.alter_column('main_category', 'slug', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        'main.category': {
            'Meta': {'object_name': 'Category'},
            'article': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'background': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['main.Category']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'spling_code': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['main']