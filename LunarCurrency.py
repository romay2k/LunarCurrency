##Currency Software by Matheus Brianesi (version 1.0)

import requests
from tkinter import *
import os
import sys
import importlib
import time


##Update Area
# URLs dos arquivos no GitHub (substitua pelos URLs reais)
URL_SCRIPT = "https://raw.githubusercontent.com/romay2k/LunarCurrency/refs/heads/main/LunarCurrency.py"
URL_VERSION = "https://raw.githubusercontent.com/romay2k/LunarCurrency/refs/heads/main/version.txt"

# Função para checar a versão
def check_for_updates(local_version_file="version.txt"):
    try:
        # Baixa a versão online
        response = requests.get(URL_VERSION)
        online_version = response.text.strip()

        # Lê a versão local
        with open(local_version_file, "r") as f:
            local_version = f.read().strip()

        # Compara as versões
        if online_version != local_version:
            print("Nova versão detectada! Atualizando...")
            return online_version  # Retorna a versão nova para atualização
        else:
            print("Já está na versão mais recente.")
            return None
    except Exception as e:
        print(f"Erro ao verificar atualizações: {e}")
        return None

# Função para baixar o script atualizado
def download_new_script(new_version, local_script="LunarCurrency.py", local_version_file="version.txt"):
    try:
        # Baixa o novo script
        response = requests.get(URL_SCRIPT)
        with open(local_script, "wb") as f:
            f.write(response.content)

        # Atualiza o arquivo de versão
        with open(local_version_file, "w") as f:
            f.write(new_version)

        print("Script atualizado com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao baixar a nova versão: {e}")
        return False

# Função principal que checa e atualiza o script se necessário
def main():
    new_version = check_for_updates()
    if new_version:
        if download_new_script(new_version):
            print("Reiniciando o aplicativo para aplicar as atualizações...")
            time.sleep(2)  # Tempo para salvar e fechar
            os.execl(sys.executable, sys.executable, *sys.argv)  # Reinicia o script
    else:
        # Aqui vai o seu código principal caso não haja atualização
        import LunarCurrency
        LunarCurrency.main()  # Substitua pelo nome da função principal do seu script

if __name__ == "__main__":
    main()



#Def's
def get_currency():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    #Currency Request and save in SETS
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    #Currency Text
    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    #Button Text Update
    botao ["text"] = "Atualizar Cotação"


#Window Configs
window = Tk()
window.title("Lunar Currency")
window.iconbitmap("C:\\Users\\mathe\\Documents\\ScriptsVSC\\LunarCurrency\\lunarcurrency.ico")

#Buttons
botao = Button(window, text="Buscar cotações", command=get_currency)
botao.grid(column=0, row=1, padx=10, pady=10)

#Labels
texto = Label(window, text="Clique no botão para ver a cotação das moedas(Updated)")
texto.grid(column=0, row=0, padx=10, pady=10)
texto_resposta = Label(window, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

#Window Loop
window.mainloop()
