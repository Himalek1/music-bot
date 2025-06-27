import vk_api

# Подключение к VK API
def get_vk_session(token):
    vk_session = vk_api.VkApi(token=token)
    return vk_session

def get_top_tracks(vk):
    response = vk.audio.get(count=10)
    return response['items']

def get_new_tracks(vk):
    response = vk.audio.get(count=10, sort=1)
    return response['items']

def search_tracks(vk, query):
    response = vk.audio.search(q=query, count=10)
    return response['items']

def get_user_music(vk, user_id):
    response = vk.audio.get(owner_id=user_id)
    return response['items']
