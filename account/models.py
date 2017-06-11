from __future__ import unicode_literals
#from tinymce.models import HTMLField

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  nama_lengkap = models.CharField(max_length=40)
  email = models.EmailField(max_length=50, blank=True)
  website = models.CharField(max_length=40, blank=True)
  biodata = models.TextField()
  
  def __unicode__(self):
    return self.nama_lengkap

class User(models.Model):
  ROLE_CHOICES = (
    ('kontributor', 'Kontributor'),
    ('staff', 'Staff'),
  )
  uname = models.ForeignKey(User)
  nama = models.ForeignKey(Profile)
  role = models.CharField(max_length=11, choices=ROLE_CHOICES)
  
  def __unicode__(self):
    return self.nama.nama_lengkap
