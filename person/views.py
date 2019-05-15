from rest_framework import viewsets

from person.models import Person, Address
from person.serializers import PersonSerializer, AddressSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    Endpoint for view or editing persons.
    """

    # Convenience ordering by birth_date.
    queryset = Person.objects.all().order_by("-birth_date")
    serializer_class = PersonSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    Endpoint for view or editing addresses.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
