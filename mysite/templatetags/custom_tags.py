from django import template
from django.utils.html import format_html

from mysite import views
from views import TUTS_MENU

register = template.Library()

#@register.simple_tag(takes_context=True)
#def ref(context,url,text=""):
#    address = context['request'].path_info
#    ref.ref_list[address]
#    print(address)
#    
#    if not text: 
#        text = url
#        
#    html = "<a href='{0}'>[{1}]</a>".format(url,text)
#    
#    return format_html(html)
    