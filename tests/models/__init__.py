from django.db import models

from wagtailforms.fields import HookSelectField
from wagtailforms.models import AbstractFormSetting


class ValidFormSettingsModel(AbstractFormSetting):
    name = models.CharField(max_length=255)
    number = models.IntegerField()


class InvalidFormSettingsModel(models.Model):
    pass


class HookSelectModel(models.Model):
    hooks = HookSelectField(null=True, blank=True, help_text="Some hooks")
