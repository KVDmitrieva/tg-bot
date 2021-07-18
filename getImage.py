from pexels_api import API
import random

import cnf


class PexelsImages:
    def __init__(self):
        self.photos = []
        self.api = API(cnf.API_KEY_PEXELS)
        self.get_list()
        self.ind = -1
        self.last = False

    def get_list(self):
        categories = ['архитектура', 'природа', 'животные',
                      'цветы', 'кошки', 'собаки', 'люди']
        self.find_image(random.choice(categories))

    def find_image(self, key_word='вдохновение'):
        api = API(cnf.API_KEY_PEXELS)
        api.search(key_word, page=1, results_per_page=10)

        # Get photos
        photos = api.get_entries()
        self.photos = []
        for photo in photos:
            self.photos.append(photo.large)

        self.ind = -1
        self.last = False

    def send_image(self):
        self.ind += 1
        if self.ind + 1 == len(self.photos):
            self.last = True
        return self.photos[self.ind]
