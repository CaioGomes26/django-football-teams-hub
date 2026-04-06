from django.contrib import admin
from .models import Time


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano_fundacao', 'pais', 'estado', 'cidade')
    list_filter = ('pais', 'estado')
    search_fields = ('nome', 'cidade')