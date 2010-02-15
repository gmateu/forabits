# -*- coding: utf-8 -*-
# Create your views here.

from django.template import Context, loader
from django.db.models import Q
from django.shortcuts import render_to_response

#models
from forabits.portal.models import Seccio

#json_list
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers

def principal(request):
    print "main"
    seccions=Seccio.objects.filter(activa=1)
    
    return render_to_response('portal.html', {'seccions': seccions})