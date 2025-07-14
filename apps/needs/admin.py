from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import Needs

@admin.register(Needs)
class NeedsAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'price_min', 'price_max']
