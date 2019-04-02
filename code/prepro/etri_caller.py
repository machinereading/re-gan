import socket
import json


def getETRI(text):
    host = '143.248.135.146'
    port = 33344

    ADDR = (host, port)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientSocket.connect(ADDR)
        clientSocket.sendall(text.encode('utf-8'))
        chunks = []
        while True:
            data = clientSocket.recv(4096)
            if len(data) == 0:
                break
            chunks.append(data.decode('utf-8'))
        result = json.loads(''.join(chunks))
        clientSocket.close()
        return result
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    inTxt = '앨런아이버슨은 미국의 선수이고, 주 포지션은 슈팅가드로서, 조지타운 대학교를 졸업하였으며, 필라델피아 세븐티식서스에 지명되었다.'
    print(getETRI(inTxt))
