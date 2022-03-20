import os


def name_header_img(instance, filename):
    """
        a util method to give header picture a name to avoid conflict
    """
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.user.username, instance.id, ext)
    path = os.path.join(instance.user.username, filename)
    return path