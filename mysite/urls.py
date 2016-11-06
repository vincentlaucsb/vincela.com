"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite import views
from mysite import menu

# ==== Logging ==== #

# Used for tutorial-specific logging debugging messages to tutorials.log
from pytutorials.logger import TUTORIALS_LOG

# ==== Begin URL Configuration ==== #

urlpatterns = [
    url(r'^$', views.FlatPage.as_view(template_name="index.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^aboutme/', views.FlatPage.as_view(template_name="aboutme.html")),
    url(r'^blog/', views.FlatPage.as_view(template_name="blog.html")),
    url(r'^projects/', views.FlatPage.as_view(template_name="projects.html")),
    url(r'^resume/$', views.FlatPage.as_view(template_name="resume.html")),
    url(r'^resume/research', views.FlatPage.as_view(template_name="resume_research.html")),
    url(r'^python/$', views.Python.as_view())
]

# Tutorials Table of Contents Pages
sections = ["intro","basics","functions","classes","appendix"]
for section in sections:
    urlpatterns.append(url(r'^python/' + section + '/$',views.SectionTOC.as_view()))

# Auto-create tutorial URL mappings #
for tutorial in views.TUTS_MENU:
    menu = views.TUTS_MENU
    tutorial_url = menu[tutorial]["url"]
    
    filename = tutorial_url + ".html"
    if ('quiz' in tutorial_url):
        TUTORIALS_LOG.info('[{0}] Mapping to quiz view at {1}'.format(__name__,tutorial_url))
        urlpatterns.append(url(r'^python/' + tutorial_url + '/', views.Quiz.as_view()))
        # Note: The "+ '/'" after tutorial_url prevents, for example, /loop/ and /loop-practice/ 
        # from mapping to the same template
    
    # Regular tutorials #
    else:
        template = menu[tutorial]["template"]
        TUTORIALS_LOG.info('[{0}] Mapping to tutorial view at {1} with template {2}'.format(__name__,tutorial_url,template))
        urlpatterns.append(url(r'^python/' + tutorial_url + '/', views.Tutorial.as_view(template_name=template)))