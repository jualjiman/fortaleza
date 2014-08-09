# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slider'
        db.create_table(u'administrador_slider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('texto', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'administrador', ['Slider'])

        # Adding model 'Categoria'
        db.create_table(u'administrador_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('votos', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'administrador', ['Categoria'])

        # Adding model 'Acabado'
        db.create_table(u'administrador_acabado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('votos', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'administrador', ['Acabado'])

        # Adding model 'Madera'
        db.create_table(u'administrador_madera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('votos', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'administrador', ['Madera'])

        # Adding model 'Mueble'
        db.create_table(u'administrador_mueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('imagenPortada', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('imagen1', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
            ('imagen2', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
            ('imagen3', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
            ('imagen4', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['administrador.Categoria'])),
            ('acabado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['administrador.Acabado'], null=True, blank=True)),
            ('madera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['administrador.Madera'], null=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('votos', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'administrador', ['Mueble'])

        # Adding model 'Contacto'
        db.create_table(u'administrador_contacto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('movil', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('direccion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('notas', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'administrador', ['Contacto'])

        # Adding model 'Mensaje'
        db.create_table(u'administrador_mensaje', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mensaje', self.gf('django.db.models.fields.TextField')()),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 8, 6, 0, 0))),
        ))
        db.send_create_signal(u'administrador', ['Mensaje'])


    def backwards(self, orm):
        # Deleting model 'Slider'
        db.delete_table(u'administrador_slider')

        # Deleting model 'Categoria'
        db.delete_table(u'administrador_categoria')

        # Deleting model 'Acabado'
        db.delete_table(u'administrador_acabado')

        # Deleting model 'Madera'
        db.delete_table(u'administrador_madera')

        # Deleting model 'Mueble'
        db.delete_table(u'administrador_mueble')

        # Deleting model 'Contacto'
        db.delete_table(u'administrador_contacto')

        # Deleting model 'Mensaje'
        db.delete_table(u'administrador_mensaje')


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
        u'administrador.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 6, 0, 0)'}),
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