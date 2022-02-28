from django import template


register = template.Library()

@register.inclusion_tag('wepost_main/navbar.html')
def navbar(current_tag=None):
    return {
        
    }
