#! -*- coding: utf-8 -*-

from django.db import models
from django.db.models import SET_NULL
from django.utils.translation import ugettext as _
from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    """ Representation for an address. """

    line_1 = models.CharField(_("Line 1"), max_length=255)
    line_2 = models.CharField(_("Line 2"), max_length=255)
    phone_number = PhoneNumberField(_("Phone number"), max_length=16, blank=True, null=True)
    person = models.ForeignKey("Person", related_name="addresses", on_delete=SET_NULL, null=True)

    def __str__(self) -> str:
        """
        String representation for a Address instance.
        """

        return f'{self.line_1}, {self.line_2}.'


class Person(models.Model):
    """ Representation for a Person. """
    name = models.CharField(_("Name"), max_length=64)
    first_name = models.CharField(_("First name"), max_length=64)
    birth_date = models.DateField(_("Birth date"))

    def __str__(self) -> str:
        """
        String representation for a Person.
        """
        return f'{self.name}, {self.first_name}'
