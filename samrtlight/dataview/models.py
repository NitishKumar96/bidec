# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Area(models.Model):
    AreaID= models.CharField(max_length=50,unique=True)
    AreaName= models.CharField(max_length=100)
    AreaSize= models.IntegerField(default=0)
    NoOfPoles=models.IntegerField(default=0)
    AverageWatt= models.IntegerField(default=0)
    PowerSaved= models.IntegerField(default=0)

class LampInfo (models.Model):                                       # basic info table for the Lamp
    LightID=models.IntegerField(unique=True)                         # specific id for the pole of that area
    AreaID=models.ForeignKey(Area, on_delete=models.CASCADE)       # defines the area of the pole
    ZigbeeID=models.CharField(max_length=50)                         # id to connect to the given pole
    type= models.CharField(max_length=100)
    maximumWatt=models.IntegerField(default=0)
    DateOfPlantation=models.DateField(null=True)
    LastDateOfMaintainence=models.DateField(null=True)

class RunningLog(models.Model):                                     # tables to store the
    time=models.DateTimeField(null=True)
    InPol1=models.IntegerField(default=0)
    InPol2=models.IntegerField(default=0)
    InPol3=models.IntegerField(default=0)
    InPol4=models.IntegerField(default=0)
    InPol5=models.IntegerField(default=0)

class datalog(models.Model):
    time=models.DateTimeField(null=True)
    LightID=models.IntegerField(default=0)
    AreaID=models.CharField(max_length=100)
    current=models.IntegerField(default=.1)
    voltage=models.IntegerField(default=0)
    
