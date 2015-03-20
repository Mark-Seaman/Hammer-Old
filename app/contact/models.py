from django.db import models
from django.contrib import admin

# Class for contact records

class Contact(models.Model):
    name  = models.CharField (max_length=40)
    address  = models.CharField (max_length=100)
    phone = models.CharField (max_length=15)


# Admin interface for contact records

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)