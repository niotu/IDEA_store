from random import shuffle
from data.product import prods

class Application():
    def __init__(self):
        pass


'''костыльный метод. нужно пофиксить чтобы каталог читался из базы'''


def get_hot_products():
    prefix = '../static/images/'
    chair1 = ['Small lounge chair MD4', prefix + 'lounge-chair.jpg', 499, '#']
    table1 = ['Open-air Coffee table', prefix + 'open-air-coffee-table.jpg', 8999, '#']
    blanket = ['Wool blanket №4', prefix + 'wool-blanket.jpg', 159, '#']

    catalog = [chair1, table1, blanket]
    shuffle(catalog)
    return catalog, {'item': 'Love sofa 2-seater', 'image': prefix + 'love-sofa.jpg', 'cost': 6699, 'link': '#'}


def get_catalog():
    catalog = [x.get_card() for x in prods]
    shuffle(catalog)
    return catalog
