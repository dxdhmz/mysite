# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Mete:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title

class Product(models.Model):
    sku = models.CharField(max_length=10)
    price = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=50)
    SIZES = (('S', 'Small'), ('M', 'Middle'), ('L', 'Large'),)
    size = models.CharField(max_length=1,choices=SIZES)

    def __unicode__(self):
        return self.name+"_"+self.sku

class Family(models.Model):
    name = models.CharField(max_length=20)
    nano_name = models.CharField(max_length=10,default=None)
    age = models.PositiveIntegerField()
    GEN = (('男','Male' ), ('女','Female' ),)

    gender = models.CharField(max_length=2, choices=GEN)

    def __unicode__(self):
        return self.name