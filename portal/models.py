# -*- coding: utf-8 -*-
from itertools import chain

from django.db import models
from django.utils.translation import ugettext_lazy
from django.utils.translation import ugettext as _

# Create your models here.


class Seccio (models.Model):
    nom = models.CharField (max_length=50)
    descripcio = models.CharField(max_length = 255)
    mare = models.ForeignKey('self', verbose_name=ugettext_lazy('Parent'), null=True, blank=True)
    url = models.URLField(max_length=255,blank=True)
    activa = models.IntegerField (ugettext_lazy('Activada'),default=1)
    
    class Meta:
        verbose_name = _('Seccio')
        verbose_name_plural = _('Seccions')
    
    def __unicode__(self):
        return self.nom
    

  
