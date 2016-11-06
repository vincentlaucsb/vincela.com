import os
import sys
from django.utils.html import format_html
sys.path.append(os.path.realpath(__file__).replace("pytutorials\\menu.py",""))

CURRENT_DIR = os.path.realpath(__file__).replace('menu.py','')

def get_title(file):
    try:
        with open(file,'r') as html_doc:
            for line in html_doc:
                if line.startswith('{% block title %}'):
                    title = line.replace('{% block title %}','').replace('{% endblock %}','')
        
        # Strip new lines from title (??? where do they come from ???)
        return title.replace('\n','')
    except UnboundLocalError:
        # Simply return the filename if no title is found
        return file.split('/')[-1]

def get_description(file):
    try:
        desc = ""
        with open(file,'r') as html_doc:
            for line in html_doc:
                if line.startswith('{% block description %}'):
                    desc = line.replace('{% block description %}','').replace('{% endblock %}','')
        
        return desc.replace('\n','')
    except UnboundLocalError:
        return ''
        
def create_menu(dir):
    for item in os.scandir(CURRENT_DIR + dir):
        filename = item.name
        print(filename,get_title(filename))

# Input: Menu object consisting for tutorials for one section
# Output: A usable HTML list
def html_list(menu):
    html = ""
    
    for key, values in menu.items():
        style = ""
        html_cls = "page"
        
        if ('Quiz' in key):
            style += 'font-weight: 900'
        if (menu[key]['nested']):
            html_cls += " nested"
        
        html += '<h3 class="{0}" style="{1}"><a href="/python/{2}">{3}</a></h3>'.format(html_cls,style,values['url'],key)
        html += '<p class="description">{0}</p>'.format(values['description'])
    
    return format_html(html)