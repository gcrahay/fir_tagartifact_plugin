from django.db import models
from django.utils.translation import ugettext_lazy as _

from incidents.models import IncidentCategory


class ValidTag(models.Model):
	name = models.CharField(max_length=30, verbose_name=_("Name"))
	description = models.CharField(max_length=100, verbose_name=_("Description"), null=True, blank=True)
	categories = models.ManyToManyField(IncidentCategory, related_name='valid_tags', verbose_name=_("Categories"))

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _("Valid tag")
		verbose_name_plural = _("Valid tags")
