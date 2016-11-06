import os
import sys
from menu import *
from shared import *

from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView

from django.utils.html import format_html

# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader

# For Tutorial Views and Menus
from pytutorials.views import *

# Current directory
BASE_DIR = os.path.dirname(__file__).replace('mysite','')
current_dir = os.path.dirname(__file__) + "\\"
sys.path.append(current_dir)
sys.path.append(BASE_DIR)

# Used for pages that use templates that are primarily hardcoded
# Home, About Me, etc...
class FlatPage(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(FlatPage, self).get_context_data(**kwargs)
	    # Modifying context passed to the template #
        context['menu'] = TOP_LEVEL_MENU
        return context