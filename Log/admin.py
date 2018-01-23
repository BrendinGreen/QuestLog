from django.contrib import admin

from .models import Objective
from .models import Location
from .models import Skill
from .models import Game


class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']


admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Game, GameAdmin)

