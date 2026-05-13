def divisor(msg):
       
        print('=-=' *30)
        print(f' {msg}')
        print('=-=' *30)


"""
função para listar os clientes cadastrados sem panel
"""

def listar_clientes(clientes):
    #pergunta para o  cliente se ele quer ver todos os clientes cadastrados 
    ver = str(input("Deseja mesmo ver todos os clientes cadastrados?(s/n): "))
    if ver == 's' or  ver == 'S':

        divisor('TODOS OS CLIENTES CADASTRADOS')
        for c in clientes:
            print(f'Cliente {c.nome} com email {c.email}')
        divisor('Fim da listagem dos cl
