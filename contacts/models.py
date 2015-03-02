from django.db import models
from django.contrib import admin

class ContactService(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название службы')

    def __str__(self):
        return self.name

class PersonContact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя контакта')
    interofficePhone = models.CharField(max_length=100, null=True, blank=True, verbose_name='Внутренний телефон')
    landlinePhone = models.CharField(max_length=100, null=True, blank=True, verbose_name='Внешний телефон')
    service = models.ForeignKey(ContactService)

    class Meta:
        permissions = (
            ("view_contact", "Can view a contact"),
        )

    def __str__(self):
        return self.name