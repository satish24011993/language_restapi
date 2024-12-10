from django.contrib import admin
from .models import Language

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    list = ('name', 'paradigm', 'author')

    admin.site.register(Language)