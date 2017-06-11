from django.contrib import admin
from post.models import Category, Page, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['nama']
  list_filter = ()
  search_fields = ['nama']
  list_per_page = 20

admin.site.register(Category,CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
  list_display = ['title','date_post','postman','publish']
  list_filter = ('date_post', 'postman', 'publish')
  search_fields = ['title', 'content']
  list_per_page = 20
  
  # go_publish if static's post already to air
  # go_draft if static's post already yet to air
  actions = ['go_publish','go_draft']
  
  def go_publish(self,request,queryset):
    queryset.update(publish=True) # set post to publish
    
  def go_draft(self,request,queryset):
    queryset.update(publish=False) # set post to draft
  
admin.site.register(Page,PageAdmin)

class PostAdmin(admin.ModelAdmin):
  list_display = ['title','date_post','category','postman','publish']
  list_filter = ('date_post','postman','publish')
  search_fields = ['title','content']
  list_per_page = 20
  
  # go_publish & go_draft are same like Page
  actions = ['go_publish','go_draft']
  
  def go_publish(self,request,queryset):
    queryset.update(publish=True)
    
  def go_draft(self,request,queryset):
    queryset.update(publish=False)
  
admin.site.register(Post,PostAdmin)
