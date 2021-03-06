# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserLog'
        db.create_table('main_userlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['securesync.FacilityUser'])),
            ('activity_type', self.gf('django.db.models.fields.IntegerField')()),
            ('start_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_active_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('total_seconds', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('main', ['UserLog'])

        # Adding model 'UserLogSummary'
        db.create_table('main_userlogsummary', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
            ('counter', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=360, blank=True)),
            ('signed_version', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('signed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['securesync.Device'])),
            ('zone_fallback', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['securesync.Zone'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['securesync.Device'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['securesync.FacilityUser'])),
            ('activity_type', self.gf('django.db.models.fields.IntegerField')()),
            ('start_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('total_seconds', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('main', ['UserLogSummary'])


    def backwards(self, orm):
        # Deleting model 'UserLog'
        db.delete_table('main_userlog')

        # Deleting model 'UserLogSummary'
        db.delete_table('main_userlogsummary')


    models = {
        'main.exerciselog': {
            'Meta': {'object_name': 'ExerciseLog'},
            'attempts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'attempts_before_completion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completion_counter': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'completion_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exercise_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '360', 'blank': 'True'}),
            'signed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Device']"}),
            'signed_version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'streak_progress': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'struggling': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['securesync.FacilityUser']", 'null': 'True', 'blank': 'True'}),
            'zone_fallback': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Zone']"})
        },
        'main.languagepack': {
            'Meta': {'object_name': 'LanguagePack'},
            'lang_id': ('django.db.models.fields.CharField', [], {'max_length': '5', 'primary_key': 'True'}),
            'lang_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'lang_version': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'software_version': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'main.userlog': {
            'Meta': {'object_name': 'UserLog'},
            'activity_type': ('django.db.models.fields.IntegerField', [], {}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_active_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'total_seconds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['securesync.FacilityUser']"})
        },
        'main.userlogsummary': {
            'Meta': {'object_name': 'UserLogSummary'},
            'activity_type': ('django.db.models.fields.IntegerField', [], {}),
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['securesync.Device']"}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '360', 'blank': 'True'}),
            'signed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Device']"}),
            'signed_version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'total_seconds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['securesync.FacilityUser']"}),
            'zone_fallback': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Zone']"})
        },
        'main.videofile': {
            'Meta': {'ordering': "['priority', 'youtube_id']", 'object_name': 'VideoFile'},
            'cancel_download': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'download_in_progress': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged_for_download': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagged_for_subtitle_download': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'percent_complete': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'subtitle_download_in_progress': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subtitles_downloaded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        },
        'main.videolog': {
            'Meta': {'object_name': 'VideoLog'},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'completion_counter': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'completion_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '360', 'blank': 'True'}),
            'signed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Device']"}),
            'signed_version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'total_seconds_watched': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['securesync.FacilityUser']", 'null': 'True', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'zone_fallback': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Zone']"})
        },
        'securesync.device': {
            'Meta': {'object_name': 'Device'},
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'public_key': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_index': 'True'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '360', 'blank': 'True'}),
            'signed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Device']"}),
            'signed_version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'0.9.2'", 'max_length': '9', 'blank': 'True'}),
            'zone_fallback': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Zone']"})
        },
        'securesync.facility': {
            'Meta': {'object_name': 'Facility'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'address_normalized': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '60', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '360', 'blank': 'True'}),
            'signed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Device']"}),
            'signed_version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'zone_fallback': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Zone']"}),
            'zoom': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'securesync.facilitygroup': {
            'Meta': {'object_name': 'FacilityGroup'},
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['securesync.Facility']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '360', 'blank': 'True'}),
            'signed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Device']"}),
            'signed_version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'zone_fallback': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Zone']"})
        },
        'securesync.facilityuser': {
            'Meta': {'unique_together': "(('facility', 'username'),)", 'object_name': 'FacilityUser'},
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['securesync.Facility']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['securesync.FacilityGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'is_teacher': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '360', 'blank': 'True'}),
            'signed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Device']"}),
            'signed_version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'zone_fallback': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Zone']"})
        },
        'securesync.zone': {
            'Meta': {'object_name': 'Zone'},
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '360', 'blank': 'True'}),
            'signed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Device']"}),
            'signed_version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'zone_fallback': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['securesync.Zone']"})
        }
    }

    complete_apps = ['main']