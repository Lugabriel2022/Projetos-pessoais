from rich.console import Console
from rich.table import Table
from os import system


def calculo_ponto(maxi, mini):
    pontos = [4, 8, 12, 16, 20]
    valores = []
    for i in pontos:
        valores.append(calcular_ma(maxi, mini, i))
    return valores


def calcular_ma(maxi: float, mini: float, read: float):
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


def calcular_span(maxi: int, mini: int):
    """Calcula o valor do span de um instrumento.

    Args:
        maxi (int): Valor maximo do range do instrumento
        mini (int): Valor minimo do range do instrumento.

    Returns:
        int: retorna o span do instrumento
    """
    return maxi - mini


def gerar_tabela_calibracao(maxi: float, mini: float, unit: str):
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


def calcular_densidade(massa, volume):
    densidade = massa / volume
    return densidade


def pressao_diferencial(h, d):
    """calculo depressão diferencial

    Args:
        h (Altura do fluido): nivel do fluido no tanque.
        d (densidade relativa): densidade relativado produto em relação a agua

    Returns:
        pressão diferencial: diferneçaentre a pressão do produto e a daagua
    """
    delta_p = h * d
    return delta_p


def Calcular_range_coluna(altura_tq: float, altura_coluna: float, densidade: float):
    """calcula o range para medição de nivelcomtransmissor abaixo do fundo do tanque, parasaber o range vazio
    utiliza altura de tanque 0, para o 100% use a altura real do tanque.

    Args:
        altura_tq (float): altura do tanque
        altura_coluna (float): altura da coluna dagua
        densidade (float): densidade relativa do produto

    Returns:
        float: retorna o valor de range
    """
    return (altura_tq + altura_coluna) * densidade


def lei_ohm(U: float = None, R: float = None, I: float = None):
    """Calcula Tensão, Resistencia e Corrente segundo a lei de Ohm

    Args:
        U (float, optional): Tensão aferida. Defaults to None.
        R (float, optional): Resistencia. Defaults to None.
        I (float, optional): Corrente. Defaults to None.

    Returns:
        float: retorna a grandeza faltante
    """
    if U == None:
        return R * I
    elif R == None:
        return U / I
    elif I == None:
        return U / R


def calculo_range_closetq(altura_tq: float, altura_coluna: float, densidade: float):
    """calcul oderange para tanques fechados

    Args:
        altura_tq (float): Altura do Tanque
        altura_coluna (float): Altura da colna
        densidade (float): Densidade relativado produto

    Returns:
        float: valor de range
    """
    return (altura_tq * densidade) - (altura_coluna * densidade)


if __name__ == "__main__":
    system("clear")
    vale = gerar_tabela_calibracao(4000, -4000, "mmH2O")
    print(calcular_densidade(0.994, 10))
    print(pressao_diferencial(1000, 1))
    print(pressao_diferencial(9000, 1))
    print(calculo_ponto(4000, 1000))

# delta_p = altura * densidade relativa
