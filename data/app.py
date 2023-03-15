from random import shuffle


class Application():
    def __init__(self):
        pass


'''костыльный метод. нужно пофиксить чтобы каталог читался из базы'''


def get_hot_products():
    prefix = './static/images/'
    chair1 = ['Small lounge chair MD4', prefix + 'lounge-chair.jpg', 499]
    table1 = ['Open-air Coffee table', prefix + 'open-air-coffee-table.jpg', 8999]
    blanket = ['Wool blanket №4', prefix + 'wool-blanket.jpg', 159]

    catalog = [chair1, table1, blanket]
    shuffle(catalog)
    return catalog


def get_catalog():
    prefix = './static/images/'
    chair1 = ['Small lounge chair MD4', prefix + 'lounge-chair.jpg', 499]
    chair2 = ['Gary Open-air chair', prefix + 'open-air-chair.jpg', 5499]
    table1 = ['Open-air Coffee table', prefix + 'open-air-coffee-table.jpg', 8999]
    puff = ['Pouf', prefix + 'pouf.jpg', 199]
    blanket = ['Wool blanket №4', prefix + 'wool-blanket.jpg', 159]

    catalog = [chair1, chair2, table1, puff, blanket]
    shuffle(catalog)
    return catalog
