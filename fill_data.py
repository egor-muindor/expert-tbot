import json
import main
import requests

__all__ = ['main']
all_url = 'https://steamspy.com/api.php?request=all'

if __name__ == '__main__':
    from models import Attribute, Object

    try:
        with open("apps.json") as f:
            result = json.load(f)
    except IOError:
        r = requests.get(all_url)
        result = r.json()
        del r

    for game in list(result.values())[:20]:
        print('importing game:', game['name'])
        object = Object.find_or_new(game['appid'])
        object.appid = game['appid']
        object.name = game['name']
        object.save()

        app_details_url = f'http://store.steampowered.com/api/appdetails?appids={game["appid"]}&l=russian'
        app_details = requests.get(app_details_url).json()[f'{game["appid"]}']['data']
        genres = []
        for genre in app_details['genres']:
            id = Attribute.query() \
                .where('name', '=', 'genre') \
                .where('value', '=', genre['description']) \
                .get()
            id = id.get(0)
            if id is None:
                attribute = Attribute()
            else:
                attribute = Attribute.find_or_new(id.id)
            attribute.name = 'genre'
            attribute.type = 'string'
            attribute.value = genre['description']
            genres.append(attribute)
        object.attributes().save_many(genres)
        del genres

    print('Final')
