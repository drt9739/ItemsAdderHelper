import json

import PyQt6
import requests

from Scripts.seventv import SevenTvApi


def main():
    apy = SevenTvApi()
    # a = apy.return_json("https://7tv.app/emotes/01J9PBTZKR0008SN4ZW8AGA3TC")
    # a = apy.return_json("https://7tv.app/emotes/01GS5HYR580005DK62WPX4DCGR")
    # print(json.dumps(a, indent=2, sort_keys=True))
    # b = apy.get_emote("https://7tv.app/emotes/01GS5HYR580005DK62WPX4DCGR")
    # print(b.get_image())
if __name__ == '__main__':
    main()
