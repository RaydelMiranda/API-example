import datetime

import factory

from person.models import Person


class PersonFactory(factory.DjangoModelFactory):
    """Factory for Person instances. Useful in tests. """

    birth_date = datetime.date(1985, 8, 6)

    class Meta:
        model = Person

