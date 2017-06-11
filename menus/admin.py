from django.contrib import admin
from menus.models import *

# Register your models here.

class MainMenu_Admin(admin.ModelAdmin):
  list_display = ['id', 'id_page', 'id_category', 'label_menu', 'slug_menu', 'type_menu', 'publish']
  list_filter = ('type_menu',)
  search_fields = ['label_menu', 'slug_menu']
  list_per_page = 20
  
  # go_publish if static's post already to air
  # go_draft if static's post already yet to air
  actions = ['go_publish','go_draft']
  
  def go_publish(self,request,queryset):
    queryset.update(publish=True) # set post to publish
    
  def go_draft(self,request,queryset):
    queryset.update(publish=False) # set post to draft
  
admin.site.register(MainMenu, MainMenu_Admin)

class SubMenu_Admin(admin.ModelAdmin):
  list_display = ['id', 'id_page', 'id_category', 'label_menu', 'slug_menu', 'type_menu', 'parent', 'publish']
  list_filter = ('type_menu',)
  search_fields = ['label_menu', 'slug_menu']
  list_per_page = 20
  
  # go_publish if static's post already to air
  # go_draft if static's post already yet to air
  actions = ['go_publish','go_draft']
  
  def go_publish(self,request,queryset):
    queryset.update(publish=True) # set post to publish
    
  def go_draft(self,request,queryset):
    queryset.update(publish=False) # set post to draft
  
admin.site.register(SubMenu, SubMenu_Admin)
