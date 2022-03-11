from django import template

register = template.Library()

@register.inclusion_tag("wepost_main/components/album_body.html")
def get_explore_albums():
    return {

    }