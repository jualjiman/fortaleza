# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Busqueda'
        db.create_table(u'administrador_busqueda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('palabra', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('repeticiones', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'administrador', ['Busqueda'])


    def backwards(self, orm):
        # Deleting model 'Busqueda'
        db.delete_table(u'administrador_busqueda')


    models = {
        u'administrador.acabado': {
            'Meta': {'object_name': 'Acabado'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'votos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'administrador.busqueda': {
            'Meta': {'object_name': 'Busqueda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palabra': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'repeticiones': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'administrador.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'votos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'administrador.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movil': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'notas': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'administrador.madera': {
            'Meta': {'object_name': 'Madera'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'votos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'administrador.mensaje': {
            'Meta': {'object_name': 'Mensaje'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 9, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.TextField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'administrador.mueble': {
            'Meta': {'object_name': 'Mueble'},
            'acabado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administrador.Acabado']", 'null': 'True', 'blank': 'True'}),
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administrador.Categoria']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen1': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen2': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen3': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen4': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagenPortada': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'madera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administrador.Madera']", 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'votos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'administrador.slider': {
            'Meta': {'object_name': 'Slider'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['administrador']
