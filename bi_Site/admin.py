from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Service)
# admin.site.register(Intro)
# admin.site.register(Featurette)
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'image', 'date_created', 'date_updated')
    list_filter = ( 'date_created', 'date_updated')
    search_fields = ('title', 'description')

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')


@admin.register(Featurette)
class FeaturetteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    list_filter = ('is_active', 'date_created')
    search_fields = ('title', 'description')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    list_filter = ('date_created',)
    search_fields = ('title', 'description')