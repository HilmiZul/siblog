from __future__ import unicode_literals
from tinymce.models import HTMLField

from django.db import models
from account.models import Profile

# Create your models here.

# Category
class Category(models.Model):
  nama = models.CharField(max_length=50)
  
  def __unicode__(self):
    return self.nama

# Page (Statis)
class Page(models.Model):
  date_post = models.DateField()
  postman = models.ForeignKey(Profile)
  title = models.CharField(max_length=80)
  #slug digantu sama id (link)
  content = HTMLField()
  #content = models.TextField()
  publish = models.BooleanField(default=True)
  
  def __unicode__(self):
    return self.title
  
# Post (Dinamis)
class Post(models.Model):
  date_post = models.DateField()
  postman = models.ForeignKey(Profile)
  title = models.CharField(max_length=80)
  #slug diganti sama id (buat bikin link)
  category = models.ForeignKey(Category)
  content = HTMLField()
  #content = models.TextField()
  feature_image = models.FileField()
  publish = models.BooleanField(default=True)
  
  def __unicode__(self):
    return self.title
