from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Service)
admin.site.register(Intro)
# admin.site.register(Featurette)
@admin.register(Featurette)
class FeaturetteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    list_filter = ('is_active', 'date_created')
    search_fields = ('title', 'description')