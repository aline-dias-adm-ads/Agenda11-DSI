
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com as mensagens dos níveis
niveis_agua = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Lista com as cores correspondentes
cores = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE
]


# Define a cor conforme o nível
def definir_cor(nivel):
    if nivel < 1 or nivel > 5:
        return Fore.WHITE

    return cores[nivel - 1]


# Exibe a situação do reservatório
def monitorar_reservatorio(nivel):
    if nivel < 1 or nivel > 5:
        print("Nível inválido!")
        return

    mensagem = niveis_agua[nivel - 1]
    cor = definir_cor(nivel)

    print(f"{cor}Nível {nivel} - {mensagem}{Style.RESET_ALL}")


# Simulação do monitoramento
print("=== MONITORAMENTO DO RESERVATÓRIO DE ÁGUA ===")
print()

for nivel in range(1, 6):
    monitorar_reservatorio(nivel)

