from random import shuffle

from data.product import Product

'''костыльный метод. нужно пофиксить чтобы каталог читался из базы'''

prods = [Product('Small lounge chair MD4', 'lounge-chair.jpg', 499),
         Product('Gary Open-air chair', 'open-air-chair.jpg', 5599),
         Product('Open-air Coffee table', 'open-air-coffee-table.jpg', 8999),
         Product('Pouf', 'pouf.jpg', 249),
         Product('Wool blanket №4', 'wool-blanket.jpg', 169),
         Product('Love sofa 2-seater', 'love-sofa.jpg', 6699),
         Product('Open-air sofa table end', 'vipp-720-open-air-sofa-open-end-left.jpg', 1279),
         Product('Lodge footstool curly', 'vipp-467-lodge-footstool-curly.jpg', 6819),
         Product('Dispenser', 'vipp-9-soap-dispenser-beige.jpg', 159),
         Product('Bath module, medium', 'vipp-982-bath-module_1.jpg', 6349),
         Product('Cabin round table, light oak base', 'vipp494_light-oak_jura_01-grey.jpg', 6259)
         ]


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


def get_prod_by_link(link):
    for p in prods:
        if p.link == link:
            return p