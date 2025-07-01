from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import (
    Gallery, Event, Profile, Member, Memory, Topic,
    Comment, TeamMember, PremiumEvent, PremiumEventImage
)

@admin.register(PremiumEvent)
class PremiumEventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # Slug is auto-generated from title
    list_display = ('title', 'slug', 'date', 'location')
    search_fields = ('title', 'location')
    list_filter = ('date',)

@admin.register(PremiumEventImage)
class PremiumEventImageAdmin(admin.ModelAdmin):
    list_display = ('event', 'caption')

admin.site.register(TeamMember)
admin.site.register(Topic)
admin.site.register(Comment)

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'death_date')
    search_fields = ('name',)
    list_filter = ('birth_date', 'death_date')

admin.site.register(Member, MPTTModelAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone_number', 'pin_code')
    search_fields = ('user__username', 'full_name', 'phone_number')
    list_filter = ('pin_code',)
    ordering = ('user__username',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'subhead')
    search_fields = ('headline', 'subhead')
    ordering = ('headline',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('headline', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('headline', 'subhead')
    ordering = ('-date',)
