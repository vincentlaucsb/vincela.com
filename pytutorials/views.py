''' Bug Note:
* Calling "funct-quiz.html" "functions-quiz.html" causes an error '''

from mysite.menu import *
from mysite.shared import TOP_LEVEL_MENU

from django.shortcuts import render
from django.views.generic import View, TemplateView

from django.utils.html import format_html

from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader

# For Quiz Views
from quiz.quiz import *

# For Tutorials Templates Listings
import importlib
from .menu import *

# For Error Logging
from .logger import TUTORIALS_LOG

import os
BASE_DIR = os.path.dirname(__file__).replace('pytutorials','')

'''
Tutorial lists:

* Reads the contents.py from a specified subdirectory in the pytutorials dir
* Generates a Menu of tutorials in the order specified by that list

'''
def tutorial_menu(dir):
    menu = Menu()

    ''' In every folder should be a contents.py file with a LIST variable
        named CONTENTS listing every file in the order they should be 
        listed '''
    try:
        contents = importlib.import_module('pytutorials.{0}.contents'.format(dir))
    
    # If contents.py is not found --> ImportError
    except ImportError:
        raise FileNotFoundError("Missing contents.py file in /pytutorials/{0}/".format(dir))

    # If contents.py file is missing CONTENTS --> AttributeError
    except AttributeError:
        raise AttributeError("Misconfiguration in /pytutorials/{0}/. Perhaps CONTENTS is missing or mispelled?".format(dir))
        
    for filename in contents.CONTENTS:
        # For testing purposes
        dir = dir.replace('.','/')
    
        try:
            filepath = BASE_DIR + "pytutorials/{0}/".format(dir) + filename
            page_title = get_title(filepath)
            menu[page_title] = {}
            menu[page_title]["url"] = dir + "/" + filename[:-5]
            
            # Implement a way to read descriptions later
            menu[page_title]["description"] = get_description(filepath)
            
            menu[page_title]["section"] = dir
            menu[page_title]["template"] = dir + '/' + filename # Template location
            
            menu[page_title]["nested"] = False
            TUTORIALS_LOG.info('[{0}] Adding {1} to menu'.format(__name__,filename))
        
        # Usually triggered by a bad entry in the contents.py file
        except FileNotFoundError:
            raise FileNotFoundError("[{0}] No such file named {1}".format('pytutorials/'+dir+'/contents.py',filename))
        
    return menu

INTRO_MENU = tutorial_menu("intro")
BASICS_MENU = tutorial_menu("basics")
FUNC_MENU = tutorial_menu("functions")
CLASS_MENU = tutorial_menu("classes")
APPENDIX_MENU = tutorial_menu("appendix")
TUTS_MENU = INTRO_MENU + BASICS_MENU + FUNC_MENU + CLASS_MENU + APPENDIX_MENU
TUTORIALS_LOG.info('[{0}] TUTS_MENU: {1}'.format(__name__,TUTS_MENU))

# Decorator for Quiz class view get/post methods #
def tutorial_response(func):
    def wrapper(self, request="", *args,**kwargs):
        # Ex: request.path
        # '/python/basics/list-tuple-dict-quiz'
        url = self.request.path.split("/")[-2] + '/' + self.request.path.split("/")[-1]
        quiz_name = self.request.path.split("/")[-1]
        
        context = {}
        context["menu"] = TOP_LEVEL_MENU
        
        current_page = TUTS_MENU.get_item(url=url)        
        context["title"] = current_page
        template = loader.get_template(current_page.template)
        TUTORIALS_LOG.info("[{0}] Creating view for {1} with template {2}".format(__name__,current_page,current_page.template))
        
        # Auto-generate 'Related Tutorials' section
        section_name = current_page.section
        related_tutorials = TUTS_MENU.subset(field="section",param=section_name)
        context["related_tutorials"] = format_html(create_bulleted_list(related_tutorials))
        
        # Next and previous tutorials: Include pages from next/previous sections #
        context["prev"] = TUTS_MENU.prev_item(str(current_page))
        context["next"] = TUTS_MENU.next_item(str(current_page))
        
        # Load the questions for this quiz #
        questions = QuizKey(quiz_name)
        for qstn in questions:
            context[qstn] = questions[qstn]

        return func(self,template=template,context=context,questions=questions)
    return wrapper

# Generic tutorial view generator
class Tutorial(TemplateView):
    @tutorial_response
    def get_context_data(self, **kwargs):
        #context = super(Tutorial, self).get_context_data(**kwargs)
        context = kwargs['context']
        return context

## Quizzes ##
# Generic Quiz view
class Quiz(View):
    @tutorial_response
    def get(self, context="", template="",**kwargs):
        return HttpResponse(template.render(context, self.request))
    @tutorial_response
    def post(self, context="", template="",**kwargs):        
        form_data = self.request.POST
        
        # kwargs["questions"] is a QuizKey object
        scored = kwargs["questions"].score(attempt=form_data)
        for qstn in scored:
            context[qstn]["html"] = scored[qstn]["html"]
        
        return HttpResponse(template.render(context, self.request))