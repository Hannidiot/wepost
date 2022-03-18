import os


def eu_header_img(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.user.username, instance.eu_id, ext)
    path = os.path.join(instance.user.username, filename)
    return path