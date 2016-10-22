from django.contrib import admin

from .models import Person, Feature, Shelter


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['first_name', 'middle_name', 'last_name']}),
        ('Personal Info', {'fields': ['date_of_birth',
                                      'ssn', 'gender', 'is_veteran']}),
        ('Shelter Info', {'fields': ['last_shelter_visited', 'shelters_visited']})
    ]

    filter_horizontal = ['shelters_visited']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
    ]


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'google_place_id']}),
        ('Capabilities', {'fields': ['rating', 'capacity', 'num_guests']}),
        ('Features', {'fields': ['features']})
    ]
    filter_horizontal = ['features']
