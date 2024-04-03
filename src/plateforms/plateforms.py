from abc import ABC, abstractmethod


class Plateform(ABC):

    PROJECT_PATH = "/home/administrateur/work/projects/crypto_bot"

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def get_assets(self):
        pass
