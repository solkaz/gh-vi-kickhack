from django.contrib import admin

from .models import Person, Feature, Shelter


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['first_name', 'middle_name', 'last_name']}),
        ('Personal Info', {'fields': ['date_of_birth',
                                      'ssn', 'gender', 'is_veteran']}),
    ]


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
    ]


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Capabilities', {'fields': ['rating', 'capacity', 'num_guests']}),
        ('Features', {'fields': ['features']})
    ]
    filter_horizontal = ['features']
