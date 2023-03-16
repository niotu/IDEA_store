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

    catalog = [chair1, chair2, table1, puff, blanket, sofa1,
               {'name': 'Open-Air sofa table end (left or right)', 'image': prefix + 'vipp-720-open-air-sofa-open-end-left.jpg',
                'price': 5500.00, 'link': '#'},
               {'name': 'Lodge footstool curly', 'image': prefix + 'vipp-467-lodge-footstool-curly.jpg',
                'price': 6800.00, 'link': '#'},
               {'name': 'Dispenser', 'image': prefix + 'vipp-9-soap-dispenser-beige.jpg', 'price': 158.00,
                'link': '#'},
               {'name': 'Bath module, medium', 'image': prefix + 'vipp-982-bath-module_1.jpg', 'price': 6350.00,
                'link': '#'},
               {'name': 'Cabin round table, light oak base', 'image': prefix + 'vipp494_light-oak_jura_01-grey.jpg',
                'price': 6250.00, 'link': '#'}]
    shuffle(catalog)
    return catalog
