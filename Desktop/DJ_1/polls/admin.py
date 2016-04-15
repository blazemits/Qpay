from django.contrib import admin
from polls.models import Person

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, AuthorAdmin)

