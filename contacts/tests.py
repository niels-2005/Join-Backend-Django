from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Contact


class ContactTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.test_user)
        self.api_authentication()
        self.test_contact = Contact.objects.create(
            name="Test Name", email="test@email.com", phone="1234567890"
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_contact(self):
        url = reverse("contacts-list")
        data = {
            "name": "Neuer Kontakt",
            "email": "neu@email.com",
            "phone": "0987654321",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Contact.objects.count(), 2)

    def test_update_contact(self):
        url = reverse("contacts-detail", kwargs={"pk": self.test_contact.id})
        data = {
            "name": "Geänderter Name",
            "email": "geandert@email.com",
            "phone": "1122334455",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.test_contact.refresh_from_db()
        self.assertEqual(self.test_contact.name, data["name"])
        self.assertEqual(self.test_contact.email, data["email"])
        self.assertEqual(self.test_contact.phone, data["phone"])

    def test_delete_contact(self):
        url = reverse("contacts-detail", kwargs={"pk": self.test_contact.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Contact.objects.count(), 0)
