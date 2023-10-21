import requests
import json
from io import BytesIO


class SevenTvEmote:
    url = 'https://cdn.7tv.app/emote/'

    def __init__(self, name: str, author: str, animated: bool, resolution: list, emote_id: str):
        self.name = name
        self.author = author
        self.animated = animated
        self.resolution = resolution
        self.emote_id = emote_id

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def if_animated(self) -> bool:
        return self.animated

    def emote_name(self) -> str:
        return self.name

    def get_better_res(self):
        return max(self.resolution, key=lambda x: x['width'] and x['height'])

    def get_image(self):
        resolution = self.get_better_res()
        url = self.url + self.emote_id + '/' + resolution['name']
        print(url)
        response = requests.get(url)
        return response.content


class SevenTvApi:
    api = 'https://7tv.io/v3/'

    def __init__(self):
        pass

    def get_emote(self, url: str) -> SevenTvEmote:
        """
        Получает ссылку и обращается по id эмоута к 7tv api
        После создаёт объект класса `SevenTvEmote()` и возвращает его пользователю
        :param url: str
        :return: SevenTvEmote()
        """
        emote_id = url[16:]
        result = requests.get(self.api + emote_id).json()

        author = result["owner"]["display_name"]
        name = result["name"]
        animated = result["animated"]
        resolution = result["host"]["files"]
        emote_id = result["id"]

        return SevenTvEmote(name, author, animated, resolution, emote_id)

    def get_emote_set(self, url: str) -> list:
        """
        Получает ссылку и обращается к сету эмотов по id
        Возращает список создержащий объекты эмоутов `SevenTvEmotes()`
        :param url: str
        :return: [SevenTvEmotes()...]
        """
        set_id = url[16:]
        result = requests.get(self.api + set_id).json()

        emote_list = list()

        for emote in result["emotes"]:
            author = emote["data"]["owner"]["display_name"]
            name = emote["name"]
            animated = emote["data"]["animated"]
            resolution = emote["data"]["host"]["files"]
            emote_id = emote["data"]["id"]
            emote_list.append(SevenTvEmote(name, author, animated, resolution, emote_id))

        return emote_list
