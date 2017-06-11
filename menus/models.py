from __future__ import unicode_literals

from django.db import models
from post.models import Page, Post, Category

# Create your models here.

# Menu type=page (halaman statis)
class MainMenu(models.Model):
  TYPE_CHOICES = (
    ('link', 'Link'),
    ('page', 'Page'),
    ('category', 'Category'),
  )
  type_menu = models.CharField(max_length=40, choices=TYPE_CHOICES)
  id_page = models.ForeignKey(Page, null=True, blank=True)
  id_category = models.ForeignKey(Category, null=True, blank=True)
  label_menu = models.CharField(max_length=40)
  slug_menu = models.CharField(max_length=40)
  publish = models.BooleanField(default=True)
  
  def __unicode__(self):
    return self.label_menu

# Sub-Menu 
class SubMenu(models.Model):
  TYPE_CHOICES = (
    ('link', 'Link'),
    ('page', 'Page'),
    ('category', 'Category'),
  )
  type_menu = models.CharField(max_length=40, choices=TYPE_CHOICES)
  id_page = models.ForeignKey(Page, null=True, blank=True)
  id_category = models.ForeignKey(Category, null=True, blank=True)
  label_menu = models.CharField(max_length=40)
  slug_menu = models.CharField(max_length=40, null=True, blank=True)
  parent = models.ForeignKey(MainMenu, null=True, blank=True)
  publish = models.BooleanField(default=True)
  
  def __unicode__(self):
    return self.label_menu
    
