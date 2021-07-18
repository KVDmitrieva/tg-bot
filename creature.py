from google_images_search import GoogleImagesSearch
from bs4 import BeautifulSoup
import requests
import random

import cnf


class RandomCreature:
    def __init__(self):
        self.animals = []
        self.api = cnf.API_KEY_GOOGLE
        self.cx = cnf.CX
        self.get_list()

    def get_list(self):
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЯ'
        for ind in range(0, 29):
            url = f'https://kupidonia.ru/spisok/spisok-zhivotnyh/bukva/{alphabet[ind]}'
            try:
                response = requests.get(url, timeout=20)
            except:
                break
            soup = BeautifulSoup(response.content, 'html.parser')
            animal_list_html = soup('table', 'lists_category list-three')[0]
            names = animal_list_html.find_all('div')
            animal_names = [name.text.strip() for name in names]
            self.animals += animal_names

    def get_creatures(self):
        choice = random.choices(self.animals, k=3)
        return choice

    def get_photos(self, choice):
        gis = GoogleImagesSearch(self.api, self.cx)
        images = []
        for i in range(3):
            try:
                gis.search({'q': choice[i] + " животное ", 'num': 1})
                images.append(gis.results()[0].url)
            except:
                images.append("Не нашел")
        return images
