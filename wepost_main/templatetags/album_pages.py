from django import template

register = template.Library()

@register.inclusion_tag("components/album_body.html")
def get_explore_albums():
    return {

    }