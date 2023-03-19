import random

from data.CONSTANTS import PREFIX


class Product:
    def __init__(self, name, image, price, link='#', description='The furniture of new era', amount=1000, category='',
                 other_photos=[]):
        self.name = name
        self.image = PREFIX + image
        self.price = price
        self.link = '-'.join(map(str.lower, self.name.split(' ')))
        self.description = description
        self.amount = amount
        self.category = category
        self.other_photos = other_photos

    def get_card(self):
        return {'name': self.name, 'image': self.image, 'price': self.price, 'link': self.link}

    def get_title(self):
        return self.name

    def get_other_images(self):
        random.shuffle(self.other_photos)
        return self.other_photos


'''вот такой должен быть аутпут из бд'''
# prods = [Product('Small lounge chair MD4', 'lounge-chair.jpg', 499),
#          Product('Gary Open-air chair', 'open-air-chair.jpg', 5599),
#          Product('Open-air Coffee table', 'open-air-coffee-table.jpg', 8999),
#          Product('Pouf', 'pouf.jpg', 249),
#          Product('Wool blanket №4', 'wool-blanket.jpg', 169),
#          Product('Love sofa 2-seater', 'love-sofa.jpg', 6699),
#          Product('Open-air sofa table end', 'vipp-720-open-air-sofa-open-end-left.jpg', 1279),
#          Product('Lodge footstool curly', 'vipp-467-lodge-footstool-curly.jpg', 6819),
#          Product('Dispenser', 'vipp-9-soap-dispenser-beige.jpg', 159),
#          Product('Bath module, medium', 'vipp-982-bath-module_1.jpg', 6349),
#          Product('Cabin round table, light oak base', 'vipp494_light-oak_jura_01-grey.jpg', 6259)
#          ]
