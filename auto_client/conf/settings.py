
import os
PLUGIN_ITEMS = {
    "nic": "src.plugins.nic.Nic",
    "disk": "src.plugins.disk.Disk",
    "memory": "src.plugins.memory.Memory",
    "basic": "src.plugins.basic.Basic",
    "board": "src.plugins.board.Board",

}
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# api接口地址
API = "http://127.0.0.1:8000/api/server.html"

TEST = True

MODE = "AGENT"  # 有三种模式 agent/ssh/salt

HOSTNAME = '1.1.1.1'
PORT = '22'
PASSWORD = 'redhat'
USERNAME = 'root'
