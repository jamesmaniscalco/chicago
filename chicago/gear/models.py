from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

import time
import datetime

import conversion


# User account - stores preferences, etc.   TODO update this with custom users in Django 1.5
class UserAccount(models.Model):
    user = models.OneToOneField(User)   # FK to single User account
    
    UNIT_OF_WEIGHT_CHOICES = (          # choices for unit of weight displayed in gear lists
        ('g', 'grams'),
        ('k', 'kilograms'),
        ('o', 'ounces'),
        ('p', 'pounds'),
    )
    unit_of_weight = models.CharField(max_length=1, choices=UNIT_OF_WEIGHT_CHOICES, default='g')
    
    UNIT_OF_VOLUME_CHOICES = (          # choices for unit of volume displayed in gear lists
        ('m', 'milliliters'),
        ('l', 'liters'),
        ('c', 'cubic inches'),
    )
    unit_of_volume = models.CharField(max_length=1, choices=UNIT_OF_VOLUME_CHOICES, default='m')
    
    def __unicode__(self):
        return "%s's account" % self.user
        
# method for automatically creating UserAccount instances for new Users
def create_user_account(sender, instance, created, **kwargs):
    if created:
        profile, created = UserAccount.objects.get_or_create(user=instance)
post_save.connect(create_user_account, sender=User)

    


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
    
    #return weight in user's preferred unit
    def get_weight(self, user):
        #only execute if weight is not null
        if self.weight:
            unit = user.useraccount.unit_of_weight
            if unit == 'g':
                return self.weight
            if unit == 'k':
                return conversion.grams_to_kilgrams(self.weight)
            if unit == 'o':
                return conversion.grams_to_ounces(self.weight)
            if unit == 'p':
                return conversion.grams_to_pounds(self.weight)
        else:
            return None

    
    def __unicode__(self):
        return unicode("{0} ({1})".format(self.model, self.make))

