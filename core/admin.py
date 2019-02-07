from __future__ import unicode_literals

from django.contrib import admin

from core.models import BeerType, Beer
from django.utils.translation import gettext_lazy as _


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    def get_beer_type_name(self, obj):
        return obj.beer_type.name
    get_beer_type_name.short_description = _('beer type')

    list_display = ('name', 'get_beer_type_name',)


# Register your models here.
admin.site.register(BeerType)
# admin.site.register(Beer, BeerAdmin)
