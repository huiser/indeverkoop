# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Profiel.voorletters'
        db.add_column(u'profiles_profiel', 'voorletters',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Profiel.roepnaam'
        db.add_column(u'profiles_profiel', 'roepnaam',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Profiel.tussenvoegsel'
        db.add_column(u'profiles_profiel', 'tussenvoegsel',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'Profiel.achternaam'
        db.add_column(u'profiles_profiel', 'achternaam',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Profiel.voorletters'
        db.delete_column(u'profiles_profiel', 'voorletters')

        # Deleting field 'Profiel.roepnaam'
        db.delete_column(u'profiles_profiel', 'roepnaam')

        # Deleting field 'Profiel.tussenvoegsel'
        db.delete_column(u'profiles_profiel', 'tussenvoegsel')

        # Deleting field 'Profiel.achternaam'
        db.delete_column(u'profiles_profiel', 'achternaam')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.profiel': {
            'Meta': {'object_name': 'Profiel'},
            'achternaam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'geslacht': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_huisnummer': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'post_land': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'post_plaats': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'post_postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'post_straat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'post_toevoeging': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'roepnaam': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'telefoonnummer1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefoonnummer2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'tussenvoegsel': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profiel'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'voorletters': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['profiles']