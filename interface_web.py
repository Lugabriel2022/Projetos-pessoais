from nicegui import ui
import Instrumentação as it
from os import system



system("clear")
def reset_table():
    tabela.rows = []

def zerar():
    resultado = 0 
    display.set_text(resultado)
    print(resultado)


def calcular_sp():
    resultado = it.calcular_span(float(valor_maior.value), float(valor_menor.value))
    display.set_text(resultado)
    print(resultado)

def atualizar_tabela():
    reset_table()
    novas_linhas = []
    range = []
    maximo = float(value_a.value)
    minimo = float(value_b.value)
    unidade = value_c.value
    pontos = [4, 8, 12, 16, 20]
    porcentagem = [0, 25, 50, 75, 100]

    for c, v in zip(pontos, porcentagem):
        valor = it.calcular_ma(maximo, minimo, c)
        range.append(valor)
        novas_linhas.append({"porcentagem": v, "valor": valor, "corrente": c, "uni": unidade})
    tabela.rows = novas_linhas
    print(range)
    ui.notify("Tabela atualizada!", type='positive')

with ui.row():
    ui.label("Tabelas Range:")
    with ui.card().classes('bg-black text-white'):
        ui.label("Tabela Range")
        with ui.row():
            ui.button(text="set", on_click= atualizar_tabela)
            ui.button(text= "reset", on_click= reset_table)
        columns = [
            {'name': "Porcentagem(%)", 'label': "Porcentagem(%)", 'field': 'porcentagem','required': True, 'align': 'center'},
            {'name': "Valor", 'label': "Valor", "field":'valor','required': True, 'align': 'center'},
            {'name': "Corrente(ma)", 'label': "Corrente(ma)", "field":'corrente','required': True, 'align': 'center'},
            {'name': "Unidade", 'label': "Unidade", "field":'uni','required': True, 'align': 'center'}
        ]
        with ui.row():
            value_a = ui.input(label="Upper Range Limit", value=0).classes('bg-zinc-600 text-white px-3 rounded')
            value_b = ui.input(label="Lower Range Limit", value=0).classes('bg-zinc-600 text-white px-3 rounded')
            value_c = ui.input(label="Insira a unidade do processo", value="none").classes('bg-zinc-600 text-white px-3 rounded')

        tabela = ui.table(columns=columns, rows=[], row_key="corrente").props("dark")

        novas_linhas = []
        range = []

    with ui.card().classes('bg-black text-white'):
        ui.label("Calculo Span")
        with ui.row():
            ui.button("Calcular", on_click= calcular_sp)
            ui.button("Zerar", on_click= zerar)

        with ui.row():
            valor_maior = ui.input("Valor Maximo", value=0).classes('bg-zinc-600 text-white px-3 rounded')
            valor_menor = ui.input("Valor Minimo", value=0).classes('bg-zinc-600 text-white px-3 rounded')

        resultado = 0
        with ui.row():
            ui.label(text="Resultado: ")
            display = ui.label(resultado)


ui.run()