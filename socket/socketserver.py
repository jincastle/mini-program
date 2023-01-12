import socket

HOST = '127.0.0.1'

PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()
print('서버가 실행되었습니다.')

client_socket, addr = server_socket.accept()

print('접속한 클라이언트 주소입니다.')
print('Connected by', addr)
# 무한루프
while True:
    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다. # 1024 받을 문자열의 크기 메모리크기 인듯
    data = client_socket.recv(1024)

    # 빈 문자열을 수신하면 루프를 중지합니다.
    if not data:
        break


    # 수신받은 문자열을 출력합니다.
    print('Received from', addr, data.decode())

    # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코)
    client_socket.sendall(data)


# 소켓을 닫습니다.
client_socket.close()
server_socket.close()