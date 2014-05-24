# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'photocontest_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photocontest.Event'])),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photocontest.Profile'])),
        ))
        db.send_create_signal(u'photocontest', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table(u'photocontest_photo')


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
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photocontest.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photocontest.Profile']"})
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