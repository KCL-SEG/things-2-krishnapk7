"""Tests for the solution of your exercise."""
"""DO NOT CHANGE THIS FILE!"""

from django import forms
from django.test import TestCase
from things.forms import ThingForm

class ThingFormTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.input = {
            'name': 'Thing',
            'description': "Thing's description",
            'quantity': 2
        }

    def test_valid_form(self):
        form = ThingForm(data=self.input)
        self.assertTrue(form.is_valid())

    def test_form_has_name_field(self):
        form = ThingForm()
        self.assertIn('name', form.fields.keys())

    def test_form_has_description_field(self):
        form = ThingForm()
        self.assertIn('description', form.fields.keys())
        field = form.fields['description']
        self.assertTrue(isinstance(field.widget, forms.Textarea))

    def test_form_has_quantity_field(self):
        form = ThingForm()
        self.assertIn('quantity', form.fields.keys())
        field = form.fields['quantity']
        self.assertTrue(isinstance(field.widget, forms.NumberInput))

    def test_form_has_no_created_at_field(self):
        form = ThingForm()
        self.assertNotIn('created_at', form.fields.keys())

    def test_form_name_can_be_35_characters(self):
        self.input['name'] = 'x' * 35
        form = ThingForm(data=self.input)
        self.assertTrue(form.is_valid())

    def test_form_name_cannot_be_36_characters(self):
        self.input['name'] = 'x' * 36
        form = ThingForm(data=self.input)
        self.assertFalse(form.is_valid())

    def test_form_quantity_cannot_be_negative(self):
        self.input['quantity'] = -1
        form = ThingForm(data=self.input)
        self.assertFalse(form.is_valid())

    def test_form_quantity_can_be_0(self):
        self.input['quantity'] = 0
        form = ThingForm(data=self.input)
        self.assertTrue(form.is_valid())

    def test_form_quantity_cannot_be_over_50(self):
        self.input['quantity'] = 50
        form = ThingForm(data=self.input)
        self.assertTrue(form.is_valid())

    def test_form_quantity_cannot_be_over_50(self):
        self.input['quantity'] = 51
        form = ThingForm(data=self.input)
        self.assertFalse(form.is_valid())
