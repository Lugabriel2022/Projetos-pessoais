from rich.console import Console
from rich.table import Table

def calcular_ma(maxi:float, mini:float, read:float):
    """Calcula os valores lidos de ma para seu equivalente na unidade do range

    Args:
        maxi (float): range maximo.
        mini (float): range minimo.
        read (float): valor lido em miliamperes.

    Returns:
        float: retorna o valor lido em miliamepres convertido para o valor na escala do range.
    """
    x = (mini) + (read - 4) * (maxi - mini) / (20 - 4)
    return x

def calcular_span(maxi:int, mini:int):
    """Calcula o valor do span de um instrumento.

    Args:
        maxi (int): Valor maximo do range do instrumento
        mini (int): Valor minimo do range do instrumento.

    Returns:
        int: retorna o span do instrumento
    """
    return maxi - mini

def gerar_tabela_calibracao(maxi:float, mini:float, unit:str):
    """Gera tabela de calibração para intrumentos

    Args:
        maxi (float): Range maximo configurado no instrumento
        mini (float): Range minimo configurado no intrumento
        unit (str): Unidade da escala do aparelho
    """
    console = Console()
    table = Table(title=f"Tabela calibração {mini} a {maxi} {unit}")

    table.add_column(f"Porcentagem(%)", justify="center", style="blue")
    table.add_column(f"Valor ({unit})", justify="left", style="green")
    table.add_column("Corrente(mA)", justify="center", style="cyan", no_wrap=True)
    
    pontos = [4, 8, 12, 16, 20]
    porcentagem = [0, 25, 50, 75, 100]


    for ma, pct in zip(pontos, porcentagem):
        valor = calcular_ma(maxi, mini, ma)
        table.add_row(f"{pct}", f"{valor:.3f}", f"{ma}")


    console.print(table)

vale = gerar_tabela_calibracao(30, -25, "Psi")

