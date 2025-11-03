# Sistema de Chat simples Peer-to-Peer

## Descrição

Este projeto implementa um sistema de comunicação peer-to-peer (P2P) utilizando a linguagem Python.
O programa permite a troca de mensagens entre dois dispositivos conectados em rede, sem a necessidade de um servidor intermediário.
A comunicação é estabelecida diretamente entre as duas partes, sendo uma configurada como servidor e a outra como cliente.

## Tecnologias Utilizadas

- Python 3.12  
- Biblioteca `socket` (para a comunicação de rede)  
- Biblioteca `threading` (para execução simultânea de envio e recebimento de mensagens)

---


## Funcionamento

1. O usuário escolhe o modo de operação:
   - **Servidor (s)**: aguarda conexões de outros dispositivos.
   - **Cliente (c)**: conecta-se ao servidor através do endereço IP informado.

2. Após a conexão ser estabelecida, ambos os lados podem:
   - Enviar mensagens digitando no terminal.
   - Receber mensagens simultaneamente através de uma *thread* dedicada.

3. Para encerrar a comunicação, basta digitar o comando: 
```bash
sair
```

## Estrutura do Código

- **receber_mensagens(sock)**: função executada em *thread*, responsável por receber e exibir mensagens recebidas.
- **main()**: função principal que gerencia o modo de operação (servidor ou cliente), estabelece a conexão e controla o envio de mensagens.
- **__main__**: ponto de entrada do programa.

## Como Executar

1. Salve o código em um arquivo chamado `chat_p2p.py`.

2. Em dois terminais diferentes (ou em duas máquinas na mesma rede):

**No Servidor:**
```bash
python chat_p2p.py
```

Digite:

```bash
s
```

O programa aguardará uma conexão na porta 5000.

No Cliente, execute :

```bash
python chat_p2p.py
```

Digite:

```bash
c
```

Em seguida, informe o endereço IP do servidor.

Após a conexão, ambos poderão trocar mensagens livremente.

---

## Observações

- Ambos os dispositivos devem estar conectados à mesma rede local.

- A porta utilizada por padrão é 5000, mas pode ser alterada no código.

- O sistema não implementa recursos de segurança, como criptografia ou autenticação.

## Exemplo de Execução

Servidor:
```bash
Digite 's' para servidor ou 'c' para cliente: s
Aguardando conexão na porta 5000...
Conectado com ('192.168.0.5', 52310)
Peer: Olá!
```


Cliente:
```bash
Digite 's' para servidor ou 'c' para cliente: c
Digite o IP do servidor: 192.168.0.10
Conectado ao servidor!
Olá!
```