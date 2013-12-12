# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.show_in_menu'
        db.add_column('main_category', 'show_in_menu',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Category.show_in_video'
        db.add_column('main_category', 'show_in_video',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Category.show_in_shop'
        db.add_column('main_category', 'show_in_shop',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.show_in_menu'
        db.delete_column('main_category', 'show_in_menu')

        # Deleting field 'Category.show_in_video'
        db.delete_column('main_category', 'show_in_video')

        # Deleting field 'Category.show_in_shop'
        db.delete_column('main_category', 'show_in_shop')


    models = {
        'main.category': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Category'},
            'article': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'background': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['main.Category']", 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_shop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_in_video': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'spling_code': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['main']