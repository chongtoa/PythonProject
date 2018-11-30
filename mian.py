#!/usr/bin／env python
# -*- coding: utf-8 -*-
import tkinter
import pygeoip


class FindIpLocation(object):
    ''' 根据IP来查找IP的位置
    基于：https://dev.maxmind.com/geoip/legacy/geolite/下载的数据
    作者：chongtao
    日期：2018.11.30
    版本：v1
    说明：该脚本仅仅学习使用，参考其他人写的修改，
    '''

    def __init__(self):

        # 创建主窗口
        self.root = tkinter.Tk()
        # 添加窗口的标题
        self.root.title('IP定位')

        # 创建一个输入框，并设置大小，用于输入IP
        self.ip_input = tkinter.Entry(self.root, width=30)

        # 创建一个显示列表
        self.display_info = tkinter.Listbox(self.root, width=50)

        # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command=self.find_ip_position, text="查询")

        # 将数据库信息获取
        self.geoip = pygeoip.GeoIP("GeoLiteCity.dat")

    # 包装到主窗口上
    def gui_layout(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()

    # 根据ip查找物理位置
    def find_ip_position(self):
        # 获取查询的IP
        self.ip_addr = self.ip_input.get()
        # 通过ip来从数据库中查询
        ip_information = self.geoip.record_by_addr(self.ip_addr)
        if ip_information is None:
            self.display_info.insert(0, "没有查到相应的IP地址")
            pass
        else:
            city = ip_information['city']
            country = ip_information['country_name']
            region_code = ip_information['region_code']
            longitude = ip_information['longitude']
            latitude = ip_information['latitude']
            ip_list_info = ["纬度:" + str(latitude), "经度:" + str(longitude), "地域编号:" + str(region_code),
                            "城市:" + str(city), "国家:" + str(country), "查询的ip:" + str(self.ip_addr)]

            for item in range(10):
                self.display_info.insert(0, "")

            for item in ip_list_info:
                self.display_info.insert(0, item)

            return ip_list_info


def main():
    search_ip_position = FindIpLocation()
    search_ip_position.gui_layout()
    tkinter.mainloop()


if __name__ == "__main__":
    main()
