from __future__ import unicode_literals

from django.db import models

GENDERS = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)


class Person(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField()
    ssn = models.PositiveIntegerField(default=0, verbose_name="SSN")
    gender = models.CharField(max_length=1, choices=GENDERS)
    is_veteran = models.BooleanField(default=False)
    # last_shelter_at

    def __str__(self):
        return str(self.pk) + ": " + self.first_name + ' ' + self.last_name


class Feature(models.Model):
    name = models.CharField(default="feature", max_length=20)

    def __str__(self):
        return str(self.name)


class Shelter(models.Model):
    name = models.CharField(default="shelter", max_length=20)
    # TODO: Need shelter's logistical info (address, postal address, etc.)
    rating = models.FloatField(default=0.0)
    capacity = models.PositiveSmallIntegerField(default=0)
    num_guests = models.PositiveSmallIntegerField(default=0,
                                                  verbose_name="Number of current guests")
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return str(self.pk) + ': '+ self.name
