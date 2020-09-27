from django.contrib import admin
from shareds.models import Country, City, Stat


class CountryAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class StatsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)

admin.site.register(Stat, StatsAdmin)

admin.site.register(City, CityAdmin)
