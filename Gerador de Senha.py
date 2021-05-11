import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        # Layout
        sg.theme('Dark Amber 5')
        layout = [
            [sg.Text('Site ou Software', size=(15, 1)),
             sg.Input(key='site', size=(25, 1))],
            [sg.Text('E-mail ou Usuário', size=(15, 1)),
             sg.Input(key='usuario', size=(25, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(31)), key='total_chars', default_value=1, size=(4, 1))],
            [sg.Output(size=(42, 5))],
            [sg.Button('Gerar Senha')]
        ]
        # Declarar janela
        self.janela = sg.Window(
            "Gerador de Senha",
            layout=layout,
            icon=(r"icon\icones.ico")
        )


    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"!@#$%¨&*()'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}")

        print('Senha salva')


gen = PassGen()
gen.Iniciar()