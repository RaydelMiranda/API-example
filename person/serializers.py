from rest_framework import serializers

from person.models import Address, Person


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('line_1', 'line_2', 'phone_number', 'person')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'first_name', 'birth_date', 'addresses')
