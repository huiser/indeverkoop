# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IdvUser'
        db.create_table(u'profiles_idvuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255, db_index=True)),
            ('voorletters', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('roepnaam', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('tussenvoegsel', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('achternaam', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('geslacht', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('telefoonnummer1', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('telefoonnummer2', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'profiles', ['IdvUser'])

        # Adding M2M table for field groups on 'IdvUser'
        m2m_table_name = db.shorten_name(u'profiles_idvuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('idvuser', models.ForeignKey(orm[u'profiles.idvuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['idvuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'IdvUser'
        m2m_table_name = db.shorten_name(u'profiles_idvuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('idvuser', models.ForeignKey(orm[u'profiles.idvuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['idvuser_id', 'permission_id'])


    def backwards(self, orm):
        # Deleting model 'IdvUser'
        db.delete_table(u'profiles_idvuser')

        # Removing M2M table for field groups on 'IdvUser'
        db.delete_table(db.shorten_name(u'profiles_idvuser_groups'))

        # Removing M2M table for field user_permissions on 'IdvUser'
        db.delete_table(db.shorten_name(u'profiles_idvuser_user_permissions'))


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
        }
    }

    complete_apps = ['profiles']