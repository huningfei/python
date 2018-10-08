from conf import settings
from src.client import AgentClient
from src.client import SaltSshClient


def start():
    if settings.MODE == 'AGENT':
        obj = AgentClient()
    elif settings.MODE == 'SSH' or settings.MODE == 'SALT':
        obj = SaltSshClient()
    else:
        raise Exception("仅支持agent,ssh,salt")
    obj.exec()
