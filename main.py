import socket

import threading
 
# Função para receber mensagens

def receber_mensagens(sock):

    while True:
        try:
            data = sock.recv(1024)
            if not data:

                break
            print("\nPeer:", data.decode())
        except:
            break
 
# Função principal

def main():
    modo = input("Digite 's' para servidor ou 'c' para cliente: ")
    if modo == 's':
        host = '0.0.0.0'  # Aceita conexões de qualquer IP
        port = 5000
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(1)
        print(f"Aguardando conexão na porta {port}...")
        conn, addr = sock.accept()
        print(f"Conectado com {addr}")

    else:

        host = input("Digite o IP do servidor: ")
        port = 5000
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((host, port))
        print("Conectado ao servidor!")
 
    # Thread para receber mensagens

    threading.Thread(target=receber_mensagens, args=(conn,), daemon=True).start()
 
    # Enviar mensagens

    while True:

        msg = input()
        if msg.lower() == 'sair':
            break

        conn.send(msg.encode())
 
    conn.close()

    print("Conexão encerrada.")
 
if __name__ == "__main__":

    main()

 