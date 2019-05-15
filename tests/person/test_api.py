import datetime

import pytest

from person.models import Person
from tests.fixtures.person.factories import PersonFactory


@pytest.mark.django_db()
class TestPersonAPI:
    """
    Some test examples on Person operations.
    """

    def test_add_person(self, api_client):
        data = {
            "name": "Raydel",
            "first_name": "Miranda",
            "birth_date": datetime.date(1985, 8, 6),
            "addresses": []
        }

        # Create API call.
        response = api_client.post('/person-api/persons/', data, format='json')

        # Assert the api status code is correct.
        assert response.status_code == 201

        # At least one created.
        assert Person.objects.count() == 1

    def test_delete_person(self, api_client):

        # Create an entry for Person.
        person = PersonFactory()

        # Assert the person exist in db.
        assert Person.objects.count() == 1

        # Delete API call
        response = api_client.delete('/person-api/persons/1/')

        # Assert response status.
        assert response.status_code == 204

        # Assert the user correctly deleted.
        assert Person.objects.count() == 0
