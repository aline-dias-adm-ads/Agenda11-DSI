
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis e as situações do reservatório
niveis_agua = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]


# Define a cor conforme o nível da água
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Exibe a situação do reservatório
def monitorar_reservatorio(nivel):
    if nivel < 1 or nivel > 5:
        print(Fore.WHITE + "Nível inválido!" + Style.RESET_ALL)
        return

    cor = definir_cor(nivel)
    mensagem = niveis_agua[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)


# Simulação do monitoramento
print("=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===")
print()

for nivel in range(1, 6):
    monitorar_reservatorio(nivel)
