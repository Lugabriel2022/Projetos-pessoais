from nicegui import ui
import Instrumentação as it

def reset_table():
    tabela.rows = []
    range = []

def atualizar_tabela():
    reset_table()
    novas_linhas = []
    maximo = float(value_a.value)
    minimo = float(value_b.value)
    pontos = [4, 8, 12, 16, 20]
    porcentagem = [0, 25, 50, 75, 100]

    for c, v in zip(pontos, porcentagem):
        valor = it.calcular_ma(maximo, minimo, c)
        range.append(valor)
        novas_linhas.append({"porcentagem": v, "valor": valor, "corrente": c})
    tabela.rows = novas_linhas
    print(range)
    ui.notify("Tabela atualizada!", type='positive')

ui.button(text="set", on_click= atualizar_tabela)


columns = [
    {'name': "Porcentagem(%)", 'label': "Porcentagem(%)", 'field': 'porcentagem','required': True, 'align': 'center'},
    {'name': "Valor(mmH2O)", 'label': "Valor(mmH2O)", "field":'valor','required': True, 'align': 'center'},
    {'name': "Corrente(ma)", 'label': "Corrente(ma)", "field":'corrente','required': True, 'align': 'center'}
]

value_a = ui.input(label="Upper Range Limit", value=0)
value_b = ui.input(label="Lower Range Limit", value=0)

tabela = ui.table(columns=columns, rows=[], row_key="corrente")

novas_linhas = []
range = []




ui.button(text= "reset", on_click= reset_table)

ui.run()