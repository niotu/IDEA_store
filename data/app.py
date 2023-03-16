from random import shuffle


class Application():
    def __init__(self):
        pass


'''костыльный метод. нужно пофиксить чтобы каталог читался из базы'''


def get_hot_products():
    prefix = './static/images/'
    chair1 = ['Small lounge chair MD4', prefix + 'lounge-chair.jpg', 499, '#']
    table1 = ['Open-air Coffee table', prefix + 'open-air-coffee-table.jpg', 8999, '#']
    blanket = ['Wool blanket №4', prefix + 'wool-blanket.jpg', 159, '#']

    catalog = [chair1, table1, blanket]
    shuffle(catalog)
    return catalog, {'item': 'Love sofa 2-seater', 'image': prefix + 'love-sofa.jpg', 'cost': 6699, 'link': '#'}


def get_catalog():
    prefix = '../static/images/'
    chair1 = {'name': 'Small lounge chair MD4', 'image': (prefix + 'lounge-chair.jpg'), 'price': 499, 'link': '#'}
    chair2 = {'name': 'Gary Open-air chair', 'image': prefix + 'open-air-chair.jpg', 'price': 5499, 'link': '#'}
    table1 = {'name': 'Open-air Coffee table', 'image': prefix + 'open-air-coffee-table.jpg', 'price': 8999,
              'link': '#'}
    puff = {'name': 'Pouf', 'image': prefix + 'pouf.jpg', 'price': 199, 'link': '#'}
    blanket = {'name': 'Wool blanket №4', 'image': prefix + 'wool-blanket.jpg', 'price': 159, 'link': '#'}
    sofa1 = {'name': 'Love sofa 2-seater', 'image': prefix + 'love-sofa.jpg', 'price': 6699, 'link': '#'}

    catalog = [chair1, chair2, table1, puff, blanket, sofa1]
    shuffle(catalog)
    return catalog
