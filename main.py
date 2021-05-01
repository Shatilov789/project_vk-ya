import requests
import json

URL = 'https://api.vk.com/method/photos.get'
params = {
    'owner_id': '552934290',
    'album_id': 'profile',
    'extended': '1',
    'access_token': '',
    'v':'5.130',
}

folder_name = params["owner_id"]
res = requests.get(URL, params=params)
dict_vk = res.json()

if 'error' in str(dict_vk):
    print()
    print(dict_vk['error']['error_msg'])

if 'response' in str(dict_vk):
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Connect-type': 'application/json', 'Authorization': ''}
    params = {"path": folder_name}
    response = requests.put(upload_url, headers=headers, params=params)

    len_foto = 0
    for key in dict_vk['response']['items']:
        dict_vk['response']['items'][len_foto]['likes']
        len_foto += 1

    counter = 0
    max_foto = 0
    best_url: str
    size_url = []
    cv2 = []
    list_likes =[]
    size_foto: str

    list_foto = []
    dict_foto = {}
    upload_url1 = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    print()
    print(f'Скачиваем фото с профиля VK: {folder_name}')
    print("-------------------------------------")
    print(f'На загрузку получили {len_foto} фото:')
    for key in dict_vk['response']['items']:
        xp = dict_vk['response']['items'][counter]['sizes']
        size_url.append(xp)
        for val in size_url:
            for key in val:
                if int(key['height']) > int(max_foto):
                    max_foto = key['height']
                best_url = key['url']
                size_foto  = key['type']
        cv2.append(best_url)
        url = best_url

        list_likes.append(dict_vk['response']['items'][counter]['likes']['count'])
        params = {"path": f'{folder_name}/{list_likes[counter]}', "url": url, "overwrite": "true"}
        response = requests.post(upload_url1, headers=headers, params=params)
        dict_foto["file_name"] = f'{list_likes[counter]}.jpg'
        dict_foto["size"] = size_foto
        list_foto.append(dict_foto)
        print(f'Фото "{list_likes[counter]}.jpg" отпралено на YandexDisk.\n'
              f'Фото {counter+1} из {len_foto} ')

        counter += 1
    print()
    print(f'Успешная загрузка, все фото на YandexDisk!')

    with open('log.txt', "a") as file:
        file.write(json.dumps(list_foto, sort_keys = True, indent = 4))
