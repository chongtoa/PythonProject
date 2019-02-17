#enconding:utf-8
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立链接
s.connect(('www.sina.com.cn', 80))

# 发送请求
s.send(b'GET / HTTP/1.1 Host: www.sina.com.cn Connection: close')

# 接受数据
buffer=[]
while True:
    # 每次最多接受1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
print(data)

