from random import shuffle, choices

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
         Product('Dispenser', 'vipp-9-soap-dispenser-beige.jpg', 159,
                 description='The Vipp dispenser is a functional product for the bathroom or kitchen. A custom-designed pump ensures a proper amount of soap, sanitizer gel, or dishwashing liquid. A sturdy body with a solid base gives the Vipp dispenser stability for one-hand operation.'),
         Product('Bath module, medium', 'vipp-982-bath-module_1.jpg', 6349,
                 description='This is the medium-sized version of the Vipp bath modules, ideal for bathrooms where storage space is needed. All three available Vipp bath modules are fitted with a durable tabletop with an integrated sink. This bath module has one sink and three drawers.Vipp bathroom tap is included.'
                             'PLEASE NOTE that this product will ship on a pallet and be delivered to curb side.We will contact you within 5'
                             'days after the order has been placed to arrange delivery.',
                 other_photos=['https://vipp.com/sites/default/files/vipp-loft-bath05_20.jpg',
                               'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-981-983-bathmodule-detail-5_0.jpg?itok=sSIY8hQT',
                               'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-981-983-bathmodule-detail-1.jpg?itok=e_yTTVag']),
         Product('Cabin round table, light oak base', 'vipp494_light-oak_jura_01-grey.jpg', 6259)
         ]


def get_hot_products():
    catalog = choices(prods, k=3)
    # print(catalog)
    shuffle(catalog)
    return catalog, Product('Love sofa 2-seater', 'love-sofa.jpg', 6699)


def get_catalog():
    catalog = [x.get_card() for x in prods]
    shuffle(catalog)
    return catalog


def get_prod_by_link(link):
    for p in prods:
        if p.link == link:
            return p
