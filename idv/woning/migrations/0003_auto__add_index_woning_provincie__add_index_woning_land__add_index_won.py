# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Woning', fields ['provincie']
        db.create_index(u'woning_woning', ['provincie'])

        # Adding index on 'Woning', fields ['land']
        db.create_index(u'woning_woning', ['land'])

        # Adding index on 'Woning', fields ['created_at']
        db.create_index(u'woning_woning', ['created_at'])

        # Adding index on 'Woning', fields ['modified_at']
        db.create_index(u'woning_woning', ['modified_at'])

        # Adding index on 'Woning', fields ['published_at']
        db.create_index(u'woning_woning', ['published_at'])

        # Adding index on 'Woning', fields ['gemeente']
        db.create_index(u'woning_woning', ['gemeente'])

        # Adding index on 'Woning', fields ['plaats']
        db.create_index(u'woning_woning', ['plaats'])


    def backwards(self, orm):
        # Removing index on 'Woning', fields ['plaats']
        db.delete_index(u'woning_woning', ['plaats'])

        # Removing index on 'Woning', fields ['gemeente']
        db.delete_index(u'woning_woning', ['gemeente'])

        # Removing index on 'Woning', fields ['published_at']
        db.delete_index(u'woning_woning', ['published_at'])

        # Removing index on 'Woning', fields ['modified_at']
        db.delete_index(u'woning_woning', ['modified_at'])

        # Removing index on 'Woning', fields ['created_at']
        db.delete_index(u'woning_woning', ['created_at'])

        # Removing index on 'Woning', fields ['land']
        db.delete_index(u'woning_woning', ['land'])

        # Removing index on 'Woning', fields ['provincie']
        db.delete_index(u'woning_woning', ['provincie'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.idvuser': {
            'Meta': {'object_name': 'IdvUser'},
            'achternaam': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'geslacht': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'roepnaam': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefoonnummer1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefoonnummer2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'tussenvoegsel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'voorletters': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'woning.woning': {
            'Meta': {'ordering': "['published_at']", 'object_name': 'Woning'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'gemeente': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'huisnummer': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'land': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'plaats': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'provincie': ('django.db.models.fields.CharField', [], {'default': "'NL'", 'max_length': '5', 'db_index': 'True'}),
            'published_at': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'straat': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'verkoper': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.IdvUser']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['woning']