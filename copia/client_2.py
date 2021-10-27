#basta ignorar --> descobrir como resolver o erro de: "EOF occurred in violation of protocol (_ssl.c:2472)"
#descobrir como matar a thread --> Feito, mas a função bloqueante recv atrapalha
#Envia e recebe, porém:
#       1) o output fica confuso
#       2) os dois scripts dependem um do outro para funcionar

import socket, ssl
from threading import *
from _thread import *
from time import sleep

HOST_1, PORT_1, CERT_1 = '192.168.0.106', 443, 'certificate_1.pem'
HOST_2, PORT_2, CERT_2 = '192.168.0.106', 4430, 'certificate_2.pem'

def enviar():
    global viva;
    
    sock = socket.socket(socket.AF_INET)
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH);
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    context.check_hostname = False;
    context.load_verify_locations(cafile=CERT_1);
    conn = context.wrap_socket(sock, server_hostname=HOST_2);
    
    while True:
        try:
            conn.connect((HOST_1, PORT_1));
            break;

        except:
            print("\n=====tentativa de conectar falhou=====\n");
            sleep(1);

    try:
        while True:
            x = input("--> ");
            x = bytes(x, "utf-8");
            conn.write(x)
            print(conn.recv().decode())

    except ssl.SSLError as e:
        print(e);
        viva = False;
        
    except Exception as e:
        print(e);
        viva = False;

    except KeyboardInterrupt:
        print("\n====Adeus!====\n");
        viva = False;

    if conn:
        conn.close();

###################

def receber():
  global viva;
  
  sock = socket.socket(); 
  sock.bind((HOST_2, PORT_2)); 
  sock.listen(5);  
  context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH);
  context.load_cert_chain(certfile=CERT_2, keyfile="private_2.pem")  # 1. key, 2. cert, 3. intermediates
  context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # optional
  context.set_ciphers('EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH')

  while True:
    conn = None;
    ssock, addr = sock.accept();
    try:
      conn = context.wrap_socket(ssock, server_side=True);
      while viva:
        print(conn.recv());
        conn.write(b'HTTP/1.1 200 OK\n\n%s' % conn.getpeername()[0].encode());
        
      break
    except ssl.SSLError as e:
      print(e)

    except Exception as e:
      print(e);
      if conn:
        conn.close();
        
    finally:
      if conn:
        conn.close()

  print("Servidor desligando!");

#####CÓDIGO PRINCIPAL
viva = True;

if __name__ == '__main__':
  start_new_thread(receber, ());#1
  start_new_thread(enviar, ());#2

