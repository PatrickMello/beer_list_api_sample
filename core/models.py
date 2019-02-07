from __future__ import unicode_literals
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class BeerType(models.Model):
    class Meta:
        verbose_name = _("Beer Type")
        verbose_name_plural = _("Beer Types")

    name = models.CharField(
        _("beer type"), max_length=128,
        help_text=_('provide a beer type like lagger, pilsen, etc.'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BeerType_detail", kwargs={"pk": self.pk})


class Beer(models.Model):
    class Meta:
        verbose_name = _("Beer")
        verbose_name_plural = _("Beers")

    name = models.CharField(
        _("name"), max_length=128,
        help_text=_("provide a beer name"))
    beer_type = models.ForeignKey(
        to='core.BeerType',
        on_delete=models.PROTECT,
        related_name='beers'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Beer_detail", kwargs={"pk": self.pk})
