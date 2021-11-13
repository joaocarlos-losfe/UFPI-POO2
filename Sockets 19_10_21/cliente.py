import socket

try:

    print("---cliente---")

    host = "localhost"
    porta = 8000
    endereco = (host, porta)

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(endereco)

    mensagem_cliente = ''
    mensagem_servidor = ''

    while(mensagem_cliente != "~desconectar~"):

        mensagem_cliente = input("✉️: ")
        cliente_socket.send(mensagem_cliente.encode())

        if(mensagem_cliente != "~desconectar~"):
            mensagem_servidor = cliente_socket.recv(1024)
            mensagem_servidor = mensagem_servidor.decode()
            print(f"🗨️: {mensagem_servidor}")
        
    
    print("conexão encerrada...")
    cliente_socket.close()
        
except:
    print("servidor não está em execução...")