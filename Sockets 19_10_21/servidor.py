import socket

def operacao_servidor(operacao: str):
    
    dados = operacao.split('/')
    print(f"dados: {dados}")

    print("operação de: ")

    if dados[0] == "cadastro":
        print("cadastro")

    elif dados[0] == "saque":
        print("saque")

    elif dados[0] == "transferencia":
        print("transferencia")

    elif dados[0] == "deposito":
        print("deposito")
    
    else:
        print("operacao invalida")
    

print("---servidor---")

host = "localhost"
porta = 8000
endereco = (host, porta)

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor_socket.bind(endereco)
servidor_socket.listen(10)
print(" Aguardando conexão...")
conexao, cliente = servidor_socket.accept()
print("Conectado...")

dados_cliente = ''
mensagem_servidor = ''

while(True):

    dados_cliente = conexao.recv(1024)
    dados_cliente = dados_cliente.decode()
    
    if dados_cliente == "~desconectar~":
        print("⚠️Cliente desconectou\nAguardando nova conexão 🕑")
        conexao, cliente = servidor_socket.accept()
        print(f"conectado...")
    else:
        print(f"💬: {dados_cliente}")
        operacao_servidor(dados_cliente)

        mensagem_servidor = str("✔️")
        conexao.send(mensagem_servidor.encode())
        
    
print("conexão encerrada")
servidor_socket.close()
"""
mensagem_servidor = input('mensagem para o cliente: ')
        conexao.send(mensagem_servidor.encode())
"""