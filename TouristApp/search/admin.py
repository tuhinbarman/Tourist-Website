from django.contrib import admin
from .models import State,Location

# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display = ('id','name','image','description',)
    list_display_links = ('id','name',)
    list_editable = ('description',)
    list_per_page = 10


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','name','state','image','description')
    list_display_links = ('id','name',)
    list_editable = ('description',)
    list_per_page = 10

admin.site.register(State,StateAdmin)
admin.site.register(Location,LocationAdmin)
