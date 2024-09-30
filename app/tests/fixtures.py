from punq import Container

from logic.init import init_container

def init_dummy_container() -> Container:
    container = init_container()
    container.register()