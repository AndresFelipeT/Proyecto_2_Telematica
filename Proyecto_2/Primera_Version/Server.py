import socket 

host = '127.0.0.1'
port = 8
HEADER = 10


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
serversocket.bind((host , port))
serversocket.listen(1)
print('Servidor en el puerto',port)

while True:
    conn , addr = serversocket.accept()
    print(f"Connectado a {addr[0]}:{addr[1]}")
    data_len = conn.recv(HEADER)
    request = conn.recv(int(data_len)).decode('utf-8')
    string_list = request.split(' ')
    requesting_file = string_list[0]

    print('Client request',requesting_file)

    myfile = requesting_file.split('?')[0]
    myfile = myfile.lstrip('/')

    try:
        file = open(myfile , 'rb')
        response = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'

        if(myfile.endswith('.jpg')):
            mimetype = 'image/jpg'
        elif(myfile.endswith('.css')):
            mimetype = 'text/css'
        elif(myfile.endswith('.pdf')):
            mimetype = 'application/pdf'
        else:
            mimetype = 'text/html'

        header = 'Content-Type: '+ mimetype +'\n\n'
    except Exception as e:
        print("-")
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')   

    final_response = header.encode('utf-8')
    final_response += response
    conn.send(final_response)
    conn.close()
