from django import template

register = template.Library()

@register.inclusion_tag("wepost_main/album_body.html")
def get_explore_albums():
    return {

    }