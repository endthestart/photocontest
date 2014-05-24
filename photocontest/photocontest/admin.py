from django.contrib import admin
from .models import Event, Profile


class EventAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Profile, ProfileAdmin)