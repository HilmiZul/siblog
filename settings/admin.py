from django.contrib import admin
from settings.models import General

# Register your models here.
class GeneralAdmin(admin.ModelAdmin):
  list_display = ['title_web', 'tagline_web']
  list_filter = ()
  search_fields = []

admin.site.register(General, GeneralAdmin)
