from random import shuffle, choices

from data.product import Product

'''костыльный метод. нужно пофиксить чтобы каталог читался из базы'''

prods = [Product('Small lounge chair MD4', 'lounge-chair.jpg', 499,
                 description='The Vipp Lodge lounge chair is suited for the living room or lounge area. This lounge chair features a molded soft shell and legs of solid oak. Here shown in predefined variants with dark oak legs.'
                             'PLEASE NOTE that this product will ship on a pallet and be delivered to curb side. We will contact you within 5 days after the order has been placed to arrange delivery.',
                 other_photos=['https://vipp.com/sites/default/files/vipp-466-lodge-lounge-curly09-03.jpg',
                               'https://vipp.com/sites/default/files/vipp466-lodge-lounge-curly-01_5.jpg',
                               'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp466-lodge-lounge-curly-02_4.jpg?itok=IRZgCOfo']),
         Product('Gary Open-air chair', 'open-air-chair.jpg', 5599,
                 description='The Vipp711 Open-Air chair is modelled after the very first Vipp chair – the Vipp451 Chair. Shaped by the well-known solid aluminum frame with rounded, rattan-covered armrests and a padded backrest, the Open-Air chair offers the same airy expression despite the solidity of the components, completed by the comfortable, durable cushions.',
                 other_photos=['https://vipp.com/sites/default/files/vipp-711-outdoor-chair-02_1.jpg',
                               'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-711-outdoor-chair-detail-02.jpg?itok=bLzRAQ60',
                               'https://vipp.com/sites/default/files/vipp-711-outdoor-chair-03_0.jpg']),
         Product('Open-air Coffee table', 'open-air-coffee-table.jpg', 8999,
                 description='The Vipp716 Open-Air coffee table is modelled after the indoors Vipp425 Coffee table. Consisting of a three-legged aluminum frame with a Ø90 tabletop consisting of teak lamellas, the coffee table offers a durable and elegant look for the lounge area. It can be combined with the Vipp714 Ø60 coffee table.',
                 other_photos=[
                     'https://vipp.com/sites/default/files/vipp-716-outdoor-coffee-table-o90-teak-01-detail.jpg',
                     'https://vipp.com/sites/default/files/_vipp-714-716-outdoor-coffee-tables-ceramic-teak-01_2.jpg',
                     'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-716-open-air-coffee-table-o90-teak-detail-01_0.jpg?itok=OYHrcVxa']),
         Product('Pouf', 'pouf.jpg', 249,
                 description="With its geometric, six-piece construction in Soprano upholstery, the Vipp655 pouf furnishes the living room with a sculpture of comfort. Intended as an extra seat or side table, the pouf is a versatile addition to the Vipp furniture collection.",
                 other_photos=['https://vipp.com/sites/default/files/2022_06_15_vipp127944.jpg',
                               'https://vipp.com/sites/default/files/dscf2380.jpg',
                               'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-655-pouf-soprano03-01_1.jpg?itok=cg2-59RI']),
         Product('Wool blanket №4', 'wool-blanket.jpg', 169,
                 description='The Vipp wool blanket is warm and ultra-soft addition for the living room or bedroom. This wool blanket is woven from all-natural wool and features a discreetly woven pattern. Available in two colour options.',
                 other_photos=['https://vipp.com/sites/default/files/vipp-112-116-textiles-living-03_web1_8.jpg']),
         Product('Love sofa 2-seater', 'love-sofa.jpg', 6699,
                 description='The Vipp Loft Sofa is one of the two models available in the Vipp sofa series. The Loft sofa features a wide, angular shape with a wood and steel construction, carried by a slender frame of powder-coated steel. One cushion per unit is included. This version is a 3-seater configuration. For more modules options, click details below.',
                 other_photos=[
                     'https://vipp.com/sites/default/files/vipp-610-sofa-loft-saxophonecol002-lifestyle-01-web1_1.jpg',
                     'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/safire_04_sandwhite_portrait_1280x1706.jpg?itok=t7oR0elR',
                     'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-610-sofa-loft-saxophonecol002-detail-03.jpg?itok=PVIBQ_rc']),
         Product('Open-air sofa table end', 'vipp-720-open-air-sofa-open-end-left.jpg', 1279,
                 description='The Open-Air sofa table end is available with both a left- and right-oriented open end with an integrated side table in teak lamellas.'
                             'NOTE:The side-orientation is to be seen as if you are facing the sofa from the front; so if you want the teak-side table to be located on your right hand when sitting in the sofa, buy the left-oriented variant.',
                 other_photos=['https://vipp.com/sites/default/files/vipp-outdoor-campaign-sofa-detail1.jpg']),
         Product('Lodge footstool curly', 'vipp-467-lodge-footstool-curly.jpg', 6819,
                 description='The Lodge footstool is a free-standing footrest to be paired with the Lodge lounge chair. This footstool features a molded soft shell and legs in solid oak.'
                             'PLEASE NOTE that this product will ship on a pallet and be delivered to curb side. We will contact you within 5 days after the order has been placed to arrange delivery.',
                 other_photos=['https://vipp.com/sites/default/files/vipp-467-lodge-footstool-curly09-01.jpg',
                               'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-467-lodge-footstool-curly07-detail-01_0.jpg?itok=BV7WHnB90',
                               'https://vipp.com/sites/default/files/vipp-466-lodge-lounge-curly07-02_1.jpg']),
         Product('Dispenser', 'vipp-9-soap-dispenser-beige.jpg', 159,
                 description='The Vipp dispenser is a functional product for the bathroom or kitchen. A custom-designed pump ensures a proper amount of soap, sanitizer gel, or dishwashing liquid. A sturdy body with a solid base gives the Vipp dispenser stability for one-hand operation.',
                 other_photos=['https://vipp.com/sites/default/files/vipp-9-soap-dispenser-beige-v2_1.jpg',
                               'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-9-soap-dispencer-black-white-01_6.jpg?itok=hTrKH5dr',
                               'https://vipp.com/sites/default/files/vipp-7-10-bathroom-combo-white-01_3.jpg']),
         Product('Bath module, medium', 'vipp-982-bath-module_1.jpg', 6349,
                 description='This is the medium-sized version of the Vipp bath modules, ideal for bathrooms where storage space is needed. All three available Vipp bath modules are fitted with a durable tabletop with an integrated sink. This bath module has one sink and three drawers.Vipp bathroom tap is included.'
                             'PLEASE NOTE that this product will ship on a pallet and be delivered to curb side.We will contact you within 5'
                             'days after the order has been placed to arrange delivery.',
                 other_photos=['https://vipp.com/sites/default/files/vipp-loft-bath05_20.jpg',
                               'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-981-983-bathmodule-detail-5_0.jpg?itok=sSIY8hQT',
                               'https://vipp.com/sites/default/files/styles/hero_hotel__2/public/vipp-981-983-bathmodule-detail-1.jpg?itok=e_yTTVag']),
         Product('Cabin round table, light oak base', 'vipp494_light-oak_jura_01-grey.jpg', 6259,
                 description='The Vipp Cabin round table is a medium-sized table for the dining room or kitchen. This table features a base of solid, oiled light oak with a marble tabletop.'
                             'PLEASE NOTE that this product will ship as a white glove delivery. This is included in the price. We will contact you within 5 days after the order has been placed to arrange delivery.',
                 other_photos=['https://vipp.com/sites/default/files/vipp-495-cabin-round-table-lightoak-01.jpg',
                               'https://vipp.com/sites/default/files/vipp-495-cabin-round-table-lightoak-02_1.jpg',
                               'https://vipp.com/sites/default/files/vipp462-lodge-chair-barnum-01-high_1.jpg'])
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


def get_user_by_id(user_id):
    for u in users:
        if u.id == user_id:
            return u
