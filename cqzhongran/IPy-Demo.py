#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 一个模块'

__author__ = 'HakunaMatata'

from IPy import IP

def PrintIP():
    ip_s = input('Please input an IP or net-range: ')
    ips = IP(ip_s)
    if len(ips) > 1:
        print('\nnet: %s'%ips.net()) #输出网络地址
        print('\nnetmask: %s'%ips.netmask()) #输出网络掩码地址
        print('\nbroadcast: %s'%ips.broadcast()) #输出网络广播地址
        print('\nsubnet: %s'%len(ips))
        for i in ips:
            print(i)
        print('\nreverse address:') #输出地址反向解析
        for i in ips.reverseNames():
            print(i)
    else:
        print('\nreverse address: %s'%ips.reverseNames)
    print ('\nhexadecimal: %s'%ips.strHex())
    print ('\nbinary ip: %s'%ips.strBin())
    print ('\niptype: %s'%ips.iptype())
if __name__=='__main__':
    PrintIP()
    input()