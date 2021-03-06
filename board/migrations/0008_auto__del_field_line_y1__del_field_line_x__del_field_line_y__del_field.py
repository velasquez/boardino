# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Line.y1'
        db.delete_column('board_line', 'y1')

        # Deleting field 'Line.x'
        db.delete_column('board_line', 'x')

        # Deleting field 'Line.y'
        db.delete_column('board_line', 'y')

        # Deleting field 'Line.x1'
        db.delete_column('board_line', 'x1')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Line.y1'
        raise RuntimeError("Cannot reverse this migration. 'Line.y1' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Line.x'
        raise RuntimeError("Cannot reverse this migration. 'Line.x' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Line.y'
        raise RuntimeError("Cannot reverse this migration. 'Line.y' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Line.x1'
        raise RuntimeError("Cannot reverse this migration. 'Line.x1' and its values cannot be restored.")

    models = {
        'board.board': {
            'Meta': {'object_name': 'Board'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        'board.line': {
            'Meta': {'object_name': 'Line'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['board.Board']"}),
            'color_l': ('django.db.models.fields.TextField', [], {'default': "'000000'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'stroke_w': ('django.db.models.fields.IntegerField', [], {})
        },
        'board.postit': {
            'Meta': {'object_name': 'PostIt'},
            'back_color': ('django.db.models.fields.TextField', [], {'default': "'#FFFF33'"}),
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['board.Board']"}),
            'color': ('django.db.models.fields.TextField', [], {'default': "'#FFFF99'"}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['board']