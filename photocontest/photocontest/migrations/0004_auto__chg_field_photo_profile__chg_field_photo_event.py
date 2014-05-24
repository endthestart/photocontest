# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Photo.profile'
        db.alter_column(u'photocontest_photo', 'profile_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photocontest.Profile'], null=True))

        # Changing field 'Photo.event'
        db.alter_column(u'photocontest_photo', 'event_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photocontest.Event'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Photo.profile'
        raise RuntimeError("Cannot reverse this migration. 'Photo.profile' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Photo.profile'
        db.alter_column(u'photocontest_photo', 'profile_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photocontest.Profile']))

        # User chose to not deal with backwards NULL issues for 'Photo.event'
        raise RuntimeError("Cannot reverse this migration. 'Photo.event' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Photo.event'
        db.alter_column(u'photocontest_photo', 'event_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photocontest.Event']))

    models = {
        u'photocontest.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'photocontest.photo': {
            'Meta': {'object_name': 'Photo'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photocontest.Event']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photocontest.Profile']", 'null': 'True', 'blank': 'True'})
        },
        u'photocontest.profile': {
            'Meta': {'object_name': 'Profile'},
            'copyright': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['photocontest']