# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Woning'
        db.create_table(u'woning_woning', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('straat', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('huisnummer', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('plaats', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gemeente', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('provincie', self.gf('django.db.models.fields.CharField')(default='NL', max_length=5)),
            ('land', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('published_at', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'woning', ['Woning'])


    def backwards(self, orm):
        # Deleting model 'Woning'
        db.delete_table(u'woning_woning')


    models = {
        u'woning.woning': {
            'Meta': {'ordering': "['published_at']", 'object_name': 'Woning'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gemeente': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'huisnummer': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'plaats': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'provincie': ('django.db.models.fields.CharField', [], {'default': "'NL'", 'max_length': '5'}),
            'published_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'straat': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['woning']