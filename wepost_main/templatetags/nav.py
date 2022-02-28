from django import template


register = template.Library()

@register.inclusion_tag('wepost_main/nav.html')
def nav(current_tag=None):
    return {
        
    }
