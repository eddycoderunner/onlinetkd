from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Competitor

class CompetitorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'phone_number', 'club_name', 'nationality')
    search_fields = ('full_name', 'club_name', 'nationality')
    list_filter = ('age', 'nationality', 'club_name')
    ordering = ('full_name',)
    list_editable = ('phone_number',)
    actions = ['mark_as_verified']

    def mark_as_verified(self, request, queryset):
        queryset.update(verified=True)
    mark_as_verified.short_description = "Mark selected competitors as verified"

admin.site.register(Competitor, CompetitorAdmin)