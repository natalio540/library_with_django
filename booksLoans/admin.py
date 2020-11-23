from django.contrib import admin

# Register your models here.

from .models import booksTable
admin.site.register(booksTable)