from __future__ import unicode_literals

from django.db import models

# Create your models here.
class General(models.Model):
  title_web = models.CharField(max_length=30)
  tagline_web = models.CharField(max_length=50, null=True, blank=True)
  description_web = models.TextField(null=True, blank=True)
  logo_web = models.FileField(null=True, blank=True)
  
  def __unicode__(self):
    return self.title_web
