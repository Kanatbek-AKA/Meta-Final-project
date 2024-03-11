from django.test import TestCase
from .models import MenuItem, Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)

    # Use the setup() method to add a few test instances of the Menu model.
    def setUp(self):
        Menu.objects.create(name="TestFood", price=15.5)
        Menu.objects.create(name="TestFood2", price=10.22)

    # Next, add another test_getall() instance method to retrieve all the Menu objects added for the test purpose.
    def test_getall(self):
        mls = Menu.objects.all()
        self.assertEqual(mls.get(name="TestFood").name, "TestFood")
