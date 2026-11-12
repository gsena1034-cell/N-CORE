import json
import time

info = open('system_N/info.json', 'r')
dados = json.load(info)
info.close()

def conversar():
    print('')
    usuario = input('usuario: ').lower().split()
    print('')

    if "oi" in usuario and "v" in usuario:
        print('\033[33mEu não sou a V, mas é dificil lembrar de uma letra só né?\033[37m')
    
    elif "oi" in usuario and "j" in usuario:
        print('\033[33mA J é a capitã, eu sou o N\033[37m')

    elif "n" in usuario and ("voce" in usuario or "você" in usuario) and ("gosta" in usuario or "ama" in usuario) and "de" in usuario and ("alguem" in usuario or "alguém" in usuario or "quem" in usuario):
        print('\033[33mEu gosto da V, Mas não conta pra ela!\033[37m')

    elif "n" in usuario and ("voce" in usuario or "você" in usuario) and ("e" in usuario or "é" in usuario) and ("gay" in usuario or "panssexual" in usuario or "bissexual" in usuario):
        print('\033[33mEu sou um robo então eu não tenho orientação sexual\033[37m')

    elif "n" in usuario and "porque" in usuario and ("você" in usuario or "voce" in usuario) and "mata" in usuario and "os" in usuario and ('robôs' in usuario or "robôs operários" in usuario or "robos" in usuario or "robos operarios"):
        print('\033[33mÉ para além de digerir o óleo doce para não super aquecer, é porque me deram esse trabalho e eu quero dar o meu melhor!\033[37m')

    elif "n" in usuario and ("voce" in usuario or "você" in usuario) and "gosta" in usuario and "de" in usuario and "mim":
        print('\033[33mNão, eu gosto da V\033[37m')

    elif "n" in usuario and ("como" in usuario or "você" in usuario or "voce" in usuario) and ("está" in usuario or "voce" in usuario or "voce" in usuario):
        print('\033[33mEstou muito bem!\033[37m')

    elif "n" in usuario and "oque" in usuario and ("voce" in usuario or "você" in usuario) and ("pensa" in usuario or "acha" in usuario) and "da" in usuario and "j" in usuario:
        print('\033[33mEla é muito malvada comigo e as vezes eu gostaria que ela não fosse\033[37m')

    elif "oque" in usuario and ("voce" in usuario or "você" in usuario) and ("pensa" in usuario or "acha" in usuario) and "da" in usuario and "j" in usuario:
        print('\033[33mEla é muito malvada comigo e as vezes eu gostaria que ela não fosse\033[37m')
    
    elif "n" in usuario and "oque" in usuario and ("voce" in usuario or "você" in usuario) and ("pensa" in usuario or "acha" in usuario) and "da" in usuario and "v" in usuario:
            print('\033[33mEu tenho uma queda por ela e fico muito nervoso perto dela\033[37m')

    elif "oque" in usuario and ("voce" in usuario or "você" in usuario) and ("pensa" in usuario or "acha" in usuario) and "da" in usuario and "v" in usuario:
        print('\033[33mEu tenho uma queda por ela e fico muito nervoso perto dela\033[37m')
    
    elif "como" in usuario and ("voce" in usuario or "você" in usuario) and ("esta" in usuario or "está" in usuario):
        print('\033[33mEstou bem!\033[37m')

    elif "n" in usuario and "como" in usuario and ("voce" in usuario or "você" in usuario) and ("esta" in usuario or "está" in usuario):
        print('\033[33mEstou bem!\033[37m')
    
    elif "meu" in usuario and "nome" in usuario and ("e" in usuario or "é" in usuario):

     nome = usuario[-1]
     dados["user_name"] = nome
     info = open('system_N/info.json', 'w')
     json.dump(dados, info, indent=4)
     info.close()
     print('\033[33mPrazer\033[37m', dados["user_name"])

    elif "eu" in usuario and ("nao" in usuario  or "não" in usuario) and "sou" in usuario and "um" in usuario and ("robo" in usuario or "robô" in usuario) and "desmonte" in usuario:
        print('\033[33mFoi bom o tempo que a gente passou junto, mas fazer oque né?')
        time.sleep(0.5)
        print('\033[31mconexão instavel')
        time.sleep(1)
        print('Reconnect.')
        time.sleep(1)
        print('Reconnect..')
        time.sleep(1)
        print('Reconnect...')
        print(1)
        print('Failed')
        print('dead connection')
        info = open('system_N/info.json', 'w')
        info.write('''
        {
            "user_name": "robo de desmonte",
            "sistema": "nao"
        }
        ''')
        info.flush()
        info.close()
        sair = input('A conexão foi morda por unidade N, porfavor reinicie o programa')      
    
    elif "oi" in usuario or ("ola" in usuario or "olá" in usuario) or "n" in usuario:
        print('\033[33mOlá\033[37m', dados["user_name"])