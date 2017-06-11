from django.contrib import admin
from account.models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['nama_lengkap','email','website']
  list_filter = ()
  search_fields = ['nama_lengkap']
  list_per_page = 20
  
admin.site.register(Profile,ProfileAdmin)

class UserAdmin(admin.ModelAdmin):
  list_display = ['uname','role']
  list_filter = ('role',)
  search_fields = ['uname']
  list_per_page = 20
  
admin.site.register(User,UserAdmin)
