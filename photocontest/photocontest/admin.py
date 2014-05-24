from django.contrib import admin
from .models import Event, Profile, Photo


class EventAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Photo, PhotoAdmin)