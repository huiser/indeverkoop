# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'IdvUser'
        db.delete_table(u'profiles_idvuser')

        # Removing M2M table for field groups on 'IdvUser'
        db.delete_table(db.shorten_name(u'profiles_idvuser_groups'))

        # Removing M2M table for field user_permissions on 'IdvUser'
        db.delete_table(db.shorten_name(u'profiles_idvuser_user_permissions'))


    def backwards(self, orm):
        # Adding model 'IdvUser'
        db.create_table(u'profiles_idvuser', (
            ('roepnaam', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('geslacht', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('telefoonnummer1', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('voorletters', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('telefoonnummer2', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('achternaam', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('actief', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('tussenvoegsel', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50, unique=True, db_index=True)),
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


    models = {
        
    }

    complete_apps = ['profiles']