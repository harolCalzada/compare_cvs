# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Curriculum


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ['algoritmo_nombre_doc', 'algoritmo_formato_documento', 'algoritmo_numero_paginas', 'algoritmo_numero_saltos_linea']

