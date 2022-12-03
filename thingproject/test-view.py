"""Tests for the solution of your exercise."""
"""DO NOT CHANGE THIS FILE!"""

from django import forms
from with_asserts.case import TestCase
from django.urls import reverse
from things.forms import ThingForm


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('home')

    def test_get_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_has_csrf_token(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, 'input[name="csrfmiddlewaretoken"]') as (element,):
                self.assertEqual(element.type, 'hidden')
        except:
            self.fail("Could not find csrf_token in the view!  Did you forget to add the csrf_token?")

    def test_home_has_name(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, 'input[type="text"][maxlength="35"]') as (element,):
                pass
        except:
            self.fail("Could not find an input matching the specifications of the name field.")

    def test_home_has_description(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, 'textarea[maxlength="120"]') as (element,):
                pass
        except:
            self.fail("Could not find an input matching the specifications of the description field.")

    def test_home_has_quantity(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, 'input[type="number"]') as (element,):
                pass
        except:
            self.fail("Could not find an input matching the specifications of the quantity field.")

    def test_home_has_submit(self):
        response = self.client.get(self.url)
        try:
            with self.assertHTML(response, '[type="submit"]') as (element,):
                pass
        except:
            self.fail("Could not find a submit button or input in the form!  Did you forget the submit button at the bottom of the form?")
