from unittest.mock import MagicMock

from tests.utils import MockedLoggerTestCase as TestCase, SetTestCase
from zoop_wrapper.models.base import Person, Address
from tests.factories.base import PersonFactory


class PersonTestCase(TestCase, SetTestCase):
    def test_required_fields(self):
        self.assertEqual(
            {
                "first_name",
                "last_name",
                "email",
                "taxpayer_id",
                "phone_number",
                "address",
            },
            Person.get_required_fields(),
        )

    def test_non_required_fields(self):
        self.assertEqual({"birthdate"}, Person.get_non_required_fields())

    def test_create(self):
        instance = PersonFactory()
        self.assertIsInstance(instance, Person)

    def test_full_name(self):
        instance = PersonFactory(first_name="foo", last_name="bar")
        self.assertIsInstance(instance, Person)

        self.assertEqual(instance.full_name, "foo bar")

    def test_init_custom_fields(self):
        instance = MagicMock()

        Person.init_custom_fields(instance)
        self.assertIsInstance(instance.address, Address)
