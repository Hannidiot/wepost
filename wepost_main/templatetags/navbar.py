from django import template


register = template.Library()

@register.inclusion_tag('components/navbar.html')
def navbar(current_tag=None):
    return {
        
    }
