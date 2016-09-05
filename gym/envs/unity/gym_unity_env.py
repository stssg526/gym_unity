# -*- coding: utf-8 -*-

import websocket
import msgpack
import gym
from gym import error, spaces

import numpy as np

class GymUnityEnv(gym.Env):

    def __init__(self): #環境が作られたとき
        websocket.enableTrace(True)
    	self.ws = websocket.create_connection("ws://localhost:4649/CommunicationGym")
        self.action_space = spaces.Discrete(4)  # 4つのアクションをセット

    def step(self, action):  # ステップ処理 、actionを外から受け取る
        actiondata = msgpack.packb({"command": str(action)})  # アクションをpack
        self.ws.send(actiondata)  # 送信

        # Unity Process

        statedata = self.ws.recv()  # 状態の受信
        state = msgpack.unpackb(statedata)  # 受け取ったデータをunpack

        return np.array(state['image']), np.array([state['reward']]), False, {}

    def close(self):  # コネクション終了処理
        self.ws.close()  # コネクション終了
