from django.contrib import admin

# Register your models here.
from .models import Category, FillInTheBlank, MultipleChoice

admin.site.register(Category)
admin.site.register(FillInTheBlank)
admin.site.register(MultipleChoice)