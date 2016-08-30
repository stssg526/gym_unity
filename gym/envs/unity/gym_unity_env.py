import websocket
import msgpack
import gym
from gym import error, spaces


class GymUnityEnv(gym.Env):

    def __init__(self): #環境が作られたとき
        ws = create_connection("ws://127.0.0.1", http_proxy_port=3000)  # wsコネクション作成
        space = spaces.Discrete(4)  # 4つのアクションをセット

    def step(self,action):  # ステップ処理 、actionを外から受け取る
        actiondata = msgpack.packb({"command": str(action)})  # アクションをpack
        ws.send(actiondata)  # 送信

        # Unity Process

        statedata = ws.recv()  # 状態の受信
        state = msgpack.unpackb(statedata)  # 受け取ったデータをunpack

    def close(self):  # コネクション終了処理
        ws.close()  # コネクション終了
