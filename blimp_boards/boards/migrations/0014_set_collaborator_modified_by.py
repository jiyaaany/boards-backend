# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for collaborator in orm['boards.BoardCollaborator'].objects.all():
            collaborator.modified_by = collaborator.created_by
            collaborator.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'allow_signup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'disqus_shortname': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'email_domains': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['accounts.EmailDomain']", 'null': 'True', 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_color': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'account_modified_by'", 'to': "orm['users.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'unique': 'True', 'blank': 'True', 'max_length': '50', 'populate_from': "'name'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'accounts.emaildomain': {
            'Meta': {'ordering': "('-date_modified', '-date_created')", 'object_name': 'EmailDomain'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'domain_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'boards.board': {
            'Meta': {'object_name': 'Board'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Account']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'board_modified_by'", 'to': "orm['users.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('account',)", 'max_length': '50', 'populate_from': "'name'"}),
            'thumbnail_lg_path': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail_md_path': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail_sm_path': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'boards.boardcollaborator': {
            'Meta': {'object_name': 'BoardCollaborator', 'unique_together': "(('board', 'user'), ('board', 'invited_user'))"},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['boards.Board']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boardcollaborator_created_by'", 'to': "orm['users.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invitations.InvitedUser']", 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boardcollaborator_modified_by'", 'to': "orm['users.User']", 'null': 'True', 'blank': 'True'}),
            'permission': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'null': 'True', 'blank': 'True'})
        },
        'boards.boardcollaboratorrequest': {
            'Meta': {'object_name': 'BoardCollaboratorRequest', 'unique_together': "(('email', 'board'), ('user', 'board'))"},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['boards.Board']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'null': 'True', 'blank': 'True'})
        },
        'invitations.inviteduser': {
            'Meta': {'object_name': 'InvitedUser', 'unique_together': "(('account', 'email'),)"},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Account']"}),
            'board_collaborator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['boards.BoardCollaborator']", 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inviteduser_created_by'", 'to': "orm['users.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'null': 'True', 'blank': 'True'})
        },
        'users.user': {
            'Meta': {'object_name': 'User'},
            'avatar_path': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'gravatar_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'last_ip': ('django.db.models.fields.IPAddressField', [], {'null': 'True', 'blank': 'True', 'max_length': '15', 'default': "'127.0.0.1'"}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'UTC'"}),
            'token_version': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '36', 'default': "'10e28f67-dd17-4d80-a9c2-35f473925a2d'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['boards']
    symmetrical = True
