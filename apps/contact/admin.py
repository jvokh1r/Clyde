from django.contrib import admin
from .models import ContactModel


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(ContactModel)
