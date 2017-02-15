# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Curriculum(models.Model):
    #Datos del csv
    empresa = models.CharField('Empresa', max_length=100, blank=True, null=True)
    nombres = models.CharField('Nombre', max_length=100, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    formacion_inicial_anio = models.CharField('Formación desde anio', max_length=10, blank=True, null=True)
    formacion_ultima_anio = models.CharField('Formación hasta anio', max_length=10, blank=True, null=True)
    institucion = models.CharField('Institucion', max_length=100, blank=True, null=True)
    cargo = models.CharField('Cargo', max_length=100, blank=True, null=True)
    puesto = models.CharField('Puesto', max_length=100, blank=True, null=True)
    sexo = models.CharField('Sexo', max_length=10, blank=True, null=True)
    ruta_cv = models.CharField('Ruta del CV', max_length=200, blank=True, null=True)
    nivel_estudio = models.CharField('Nivel de estudio', max_length=100, blank=True, null=True)
    area_estudio = models.CharField('Area de estudio', max_length=100, blank=True, null=True)
    #Datos del algoritmo
    algoritmo_nombre_doc = models.CharField('Nombre del archivo', max_length=100)
    algoritmo_texto = models.TextField('Texto')
    algoritmo_numero_paginas = models.IntegerField('Numero de páginas', blank=True, null=True)
    algoritmo_formato_documento = models.CharField('Formato del documento', max_length=100)
    algoritmo_numero_saltos_linea = models.IntegerField('Numero de saltos de linea', blank=True, null=True)

    def __unicode__(self):
        return u'{0} {1}'.format(self.apellidos, self.nombres)

    class Meta:
        verbose_name = 'Curriculum'
        verbose_name_plural = 'Curriculums'
