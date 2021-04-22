import requests

import config as cfg

class Bot:
    """
    1. TODO: перевести прямые коннекты по http на rpc
    2. TODO: вспомнить, что конкретно хотелось сделать
    3. TODO: учитывая разные апи мессенджеров, реализовать менеджмент юзер-аккаунтов в отдельном классе
    """
    def register_user(self, nickname: str, chat_token: str, phone=""):
        new_user = requests.post(cfg.ROOMS_URL + '/register_user').json()
