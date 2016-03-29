from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Adopter(models.Model):
    #dwelling = models.ForeignKey(dwelling)
    number_of_kids = models.IntegerField()
    number_of_pets = models.IntegerField()
    patron = models.ForeignKey(patron)
    #own_rent = models.CharField(max_length=4,choices=#Guido
    
    def __unicode__(self):
        return self.id

class Dwelling(models.Model):
    #type_of_dwelling = models.#Guido
    
    def __unicode__(self):
        return self.id
        
class Patron(models.Model):
    first_name = models.
    last_name = models.
    street = models.
    city = models.
    state = models.
    zip_code = models.
    phone = models.
    email = models.
    
    def __unicode__(self):
        return self.id
        
class Donation(models.Model):
     patron = models.ForeignKey(patron)
     amount = models.IntegerField()
     date_of_donation = models.DateField()
     
     def __unicode__(self):
        return self.id
        
class Animal(models.Model):
    #type_id = models.ForeignKey(type_id)#Check
    breed = models.ForeignKey(breed)
    age = models.ForeignKey(age)
    name = models.Adopter
    gender = models.
    vaccination = models.
    
    def __unicode__(self):
        return self.id
        
class Age(models.Model):
    age_category = models.
    
    def __unicode__(self):
        return self.id
        
class Breed(models.Model):
    breed_category = models.
    
    def __unicode__(self):
        return self.id
        
class Type(models.Model):
    type_category = models.
    
    def __unicode__(self):
        return self.id

class Adoption(models.Model):
    patron = models.ForeignKey(patron)
    animal = models.ForeignKey(animal)
    date_of_adoption = models.DateField()
    
    def __unicode__(self):
        return self.id
        
