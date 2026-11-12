from system_N import N_reboot
from system_N import N_chat
import json

info = open('system_N/info.json', 'r')
dados = json.load(info)
info.close()

chat = False

if dados["sistema"] == "sim":
   chat = True
   print('\033[33mOlá! Eu sou a unidade N!\033[37m')

if dados["sistema"] == "nao":
    pergunta = input('Active Unit N? ')

    if pergunta == "yes":
        print('')
        N_reboot.reboot()
        info = open('system_N/info.json', 'w')
        info.write('''
        {
            "user_name": "robo de desmonte",
            "sistema": "sim"
        }
        ''')
        info.flush()
        info.close()
        
    elif pergunta == "no":
        print('Exit to program')

while True:
    if chat:
        N_chat.conversar()