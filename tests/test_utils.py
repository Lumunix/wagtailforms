from django.core.exceptions import ImproperlyConfigured
from django.test import override_settings

from tests.models import ValidFormSettingsModel
from wagtailforms.utils.loading import get_advanced_settings_model

from .test_case import AppTestCase


class AdvancedSettingsTests(AppTestCase):
    @override_settings(WAGTAILFORMS_ADVANCED_SETTINGS_MODEL=None)
    def test_default_none(self):
        self.assertIsNone(get_advanced_settings_model())

    @override_settings(WAGTAILFORMS_ADVANCED_SETTINGS_MODEL="foo")
    def test_invalid_string(self):
        msg = "must be of the form 'app_label.model_name'"
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            get_advanced_settings_model()

    @override_settings(WAGTAILFORMS_ADVANCED_SETTINGS_MODEL="foo.Bar")
    def test_invalid_import(self):
        msg = "refers to model 'foo.Bar' that has not been installed"
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            get_advanced_settings_model()

    @override_settings(WAGTAILFORMS_ADVANCED_SETTINGS_MODEL="tests.InvalidFormSettingsModel")
    def test_invalid_model_inheritance(self):
        msg = "must inherit from 'wagtailforms.models.AbstractFormSetting'"
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            get_advanced_settings_model()

    @override_settings(WAGTAILFORMS_ADVANCED_SETTINGS_MODEL="tests.ValidFormSettingsModel")
    def test_valid_model_returns_class(self):
        self.assertIs(get_advanced_settings_model(), ValidFormSettingsModel)
