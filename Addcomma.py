#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:ZRui
# datetime:2018/6/27 11:46
# software:PyCharm
import requests
import paramiko
import re


def addcommoa():
    content = requests.get(r'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt').text
    f1 = re.sub('(\n\n)', ',', content.strip())
    with open(r'\\RT-N56U_B1\Media\AiDisk_b1\aria\config\aria2 - backup.conf', encoding='utf-8') as f:
        f2 = f.read()
    trackers = re.compile('\nbt-tracker=(.*)\n').findall(f2)[0]
    conf = re.sub(trackers, f1, f2)
    # print(type(f2))
    with open(r'\\RT-N56U_B1\Media\AiDisk_b1\aria\config\aria2.conf', 'w', encoding='utf-8', newline='\n') as f:
        f.write(conf)
    print('trackers更新完成')

def ssh_cilent():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.123.1', 22, 'admin', 'admin')
    stdin, stdout, stderr = ssh.exec_command('sh /usr/bin/aria.sh restart')
    print(stdout.read())


addcommoa()
ssh_cilent()