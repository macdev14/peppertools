from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Post(models.Model):
    sender = models.CharField(_("remetente"), null=True, blank=True, max_length=500)
    receiver = models.CharField(_("destinatário"), null=True, blank=True, max_length=500)
    length = models.FloatField(_("comprimento"), null=True, blank=True)
    height = models.FloatField(_("altura"), null=True, blank=True)
    