import PySimpleGUI as sg


def tela_inicial():
    sg.theme('LightGrey2')

    cep = [
        [sg.Text('Informe o CEP:', font='Arial 12 bold', pad=(0, 0)),
         sg.Input(size=(20, 0), font='Arial 12', pad=(0, 0), key='cep')],
    ]

    coluna_esquerda = [
        [sg.Text('LOGRADOURO.:', font='Arial 12')],
        [sg.Text('BAIRRO.:', font='Arial 12')],
        [sg.Text('CIDADE.:', font='Arial 12')],
        [sg.Text('UF.:', font='Arial 12')],
        [sg.Text('IBGE.:', font='Arial 12')],
        [sg.Text('DDD.:', font='Arial 12')],
        [sg.Text('COMPLEMENTO.:', font='Arial 12')]
    ]

    coluna_direita = [
        [sg.Input(font='Arial 12 bold', size=(40, 1),
                  readonly=True, key='logradouro')],
        [sg.Input(font='Arial 12 bold', size=(
            40, 1), readonly=True, key='bairro')],
        [sg.Input(font='Arial 12 bold', size=(
            40, 1), readonly=True, key='localidade')],
        [sg.Input(font='Arial 12 bold', size=(
            40, 1), readonly=True, key='uf')],
        [sg.Input(font='Arial 12 bold', size=(
            40, 1), readonly=True, key='ibge')],
        [sg.Input(font='Arial 12 bold', size=(
            40, 1), readonly=True, key='ddd')],
        [sg.Input(font='Arial 12 bold', size=(40, 1),
                  readonly=True, key='complemento')],
    ]

    botoes = [
        [sg.Button('Consultar', font='Arial 12',
                   size=(10, 1), pad=((0, 15), 0)),
         sg.CButton('Sair', font='Arial 12', size=(8, 1), pad=((0, 15), 0))]
    ]

    layout = [
        [sg.Text('Consulta o CEP', font='Arial 18 bold')],
        [sg.Column(cep, justification='center',
                   element_justification='center')],
        [
            sg.Column(coluna_esquerda, pad=((0, 20), 0)),
            sg.Column(coluna_direita)
        ],
        [
            sg.Column(botoes, element_justification='center',
                      justification='center')
        ]
    ]

    tela_principal = sg.Window('ConsultaCEP', element_padding=(
        0, 10), layout=layout, size=(600, 500), finalize=True)
