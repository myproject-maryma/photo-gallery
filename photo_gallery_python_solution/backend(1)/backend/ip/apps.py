from django.apps import AppConfig
from django.core.cache import cache

from backend.settings import BASE_DIR


def compare_dimension(l):
    l = l.split('x')
    return int(l[0]) * int(l[1])


class IpConfig(AppConfig):
    name = 'ip'

    # This function is called each time when django app is loaded
    # By doing this,we don't have to read this file every request
    def ready(self):
        with open(BASE_DIR + '\\data.csv') as f:
            urls = f.read()
            # set it to cache
            cache.set('urls', urls, None)
            urls = urls.split('\n')
            # Dimension of the image
            dimension = []
            for url in urls:
                # The last two parameters represent width and height
                dimension_list = url.split('/')[-2:]
                # format to axb
                dimension.append('x'.join(dimension_list[0:2]))
            # remove duplicate dimension,then order dimension by width
            sorted_list = sorted(list(set(dimension)), key=(lambda x: x.split('x')))
            # set cache
            cache.set('dimension', sorted_list, None)
