##Currency Software by Matheus Brianesi (version 1.0)

import requests
from tkinter import *

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

#Buttons
botao = Button(window, text="Buscar cotações", command=get_currency)
botao.grid(column=0, row=1, padx=10, pady=10)

#Labels
texto = Label(window, text="Clique no botão para ver a cotação das moedas")
texto.grid(column=0, row=0, padx=10, pady=10)
texto_resposta = Label(window, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

#Window Loop
window.mainloop()