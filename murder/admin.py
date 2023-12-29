from django.contrib import admin

from murder.models import (
    City, CityForm, Organization, OrganizationForm,
    Theme, ThemeForm, Scenario, ScenarioForm
)


class CityAdmin(admin.ModelAdmin):
    form = CityForm
    list_display = ('name',)
    search_fields = ('name',)


class OrganizationAdmin(admin.ModelAdmin):
    form = OrganizationForm
    list_display = ('name',)
    search_fields = ('name',)


class ThemeAdmin(admin.ModelAdmin):
    form = ThemeForm
    list_display = ('name',)
    search_fields = ('name',)


class ScenarioAdmin(admin.ModelAdmin):
    form = ScenarioForm
    list_display = (
        'name',
        'organization',
        'description_short',
    )
    search_fields = (
        'name',
        'organization',
        'description_short',
    )


admin.site.register(City, CityAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Scenario, ScenarioAdmin)
