from django.db import models
from django.contrib import admin

class ContactService(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PersonContact(models.Model):
    name = models.CharField(max_length=200)
    interofficePhone = models.CharField(max_length=20, null=True, blank=True)
    landlinePhone = models.CharField(max_length=20, null=True, blank=True)
    service = models.ForeignKey(ContactService)

    class Meta:
        permissions = (
            ("view_contact", "Can view a contact"),
        )

    def __str__(self):
        return self.name

admin.site.register(ContactService)
admin.site.register(PersonContact)