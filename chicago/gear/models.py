from django.db import models
from django.contrib.auth.models import User, Group

import time
import datetime


# Base gear item
class GearItem(models.Model):
    owner = models.ForeignKey(User, related_name='gear_owned')  # actual owner of the item
    holder = models.ForeignKey(User, related_name='gear_held')  # who is currently in possession
    make = models.CharField(max_length=200)             # name of gear manufacturer (e.g. "Granite Gear")
    model = models.CharField(max_length=200)            # name of gear model (e.g. "Blaze A.C. 60")
    description = models.TextField(blank=True)          # optional description of the gear (e.g. "60 liter backpack")
    weight = models.FloatField(blank=True, null=True)   # optional weight of the gear, in grams
    
    # current status of gear (e.g. "checked out", "missing")
    STATUS_CHOICES = (
        ('i', 'checked in'),
        ('o', 'checked out'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='i')
    
    
    def __unicode__(self):
        return unicode(self.model + "(" + self.make + ")")

