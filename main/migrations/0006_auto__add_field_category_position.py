# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.position'
        db.add_column('main_category', 'position',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.position'
        db.delete_column('main_category', 'position')


    models = {
        'main.category': {
            'Meta': {'object_name': 'Category'},
            'article': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'background': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['main.Category']", 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'spling_code': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['main']