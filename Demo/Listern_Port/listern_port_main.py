#enconding:utf-8
import socket, time, threading

# set timeout 3s
socket.setdefaulttimeout(3)

def socket_port(ip, port):
    """
    输入ip和端口号，判断端口号是否被占用
    """
    try:
        if port > 65534:
            print("端口扫描结束")
            return
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            print(ip, ":", port, "端口被占用")
            lock.release()
    except:
        print("端口扫描异常")


def ip_scan(ip):
    """
    输入ip， 扫描IP的端口号0-65534
    """
    try:
        print('开始扫描%s' %ip)
        start_time=time.time()
        for i in range(0, 65534):
            socket_port, (ip, int(i))
        print("扫描端口完成，共用时：%.2f" %(time.time()-start_time))
    except:
        print("扫描ip失败")

if __name__=='__main__':
    url=input('Input the ip you want to scan: ')
    ip_scan(url)