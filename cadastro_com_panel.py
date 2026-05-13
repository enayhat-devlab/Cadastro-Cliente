def divisor(msg):
       
        print('=-=' *30)
        print(f' {msg}')
        print('=-=' *30)
        
from rich import print
from rich.panel import Panel

"""
funçao de listar clientes dentro de um panel
"""
def listar_clientes(clientes):
    for i,c in enumerate(clientes, start=1):
        conteudo = f"{i}º cliente\n"
        conteudo += f"NOME:{c.nome}\n"
        conteudo += f"{'=-=' *3}\n"
        conteudo += f"EMAIL:{c.email}"
        listar_clientes = Panel(conteudo, title = "LISTA DE CLIENTES")
        print(listar_clientes)

