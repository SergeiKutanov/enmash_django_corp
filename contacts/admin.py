from django.contrib import admin

# Register your models here.
from contacts.models import ContactService, PersonContact


class ContactInline(admin.StackedInline):
    model = PersonContact
    extra = 1


class ContactServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Название службы', {'fields': ['name']})
    ]
    inlines = [ContactInline]

admin.site.register(ContactService, ContactServiceAdmin)
admin.site.register(PersonContact)