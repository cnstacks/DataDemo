from django.shortcuts import render

# Create your views here.

import pymysql
import paramiko
from datetime import datetime
import time

# timestamp
timestamp = datetime.now

# 创建SSH对象;
ssh = paramiko.SSHClient()

# 把要连接的机器添加到known_hosts文件中;
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器;
ssh.connect(hostname='47.95.234.20', port=22, username='root', password='Tqtl911!))*^')
hosts = ['47.95.234.20', '47.95.234.23']
memCmd = "fping -A -u -c 4 47.95.234.20 47.95.234.23 47.95.234.23"
# cmd = 'ls -l;ifconfig'       #多个命令用;隔开

stdin, stdout, stderr = ssh.exec_command(memCmd)

memResult = stdout.read()
print(memResult)
if not memResult:
    memResult = stderr.read()
ssh.close()
print("memResult.decode:", memResult.decode('utf8'))

result_list = memResult.decode('utf8').split('\n')
print("result_list:", result_list)
del result_list[-1]
for i in result_list:
    server_ip = i.split()[0]
    xmt_data = i.split()[4].split('/')[0]
    rcv_data = i.split()[4].split('/')[1]
    loss_percent = i.split()[4].split('/')[-1].split('%')[0]
    min_time = i.split()[-1].split('/')[0]
    avg_time = i.split()[-1].split('/')[1]
    max_time = i.split()[-1].split('/')[2]
    # 创建数据库连接；
    conn = pymysql.connect(host='localhost', user='root', password='Tqtl911!@#)^', database='DataDemo', charset='utf8')
    cursor = conn.cursor()

    # 执行sql语句；
    sql = "insert into ReturnedRecord(server_ip,xmt_data,rcv_data,loss_percent,min_time,avg_time,max_time,time) values('%s','%s','%s','%s','%s','%s','%s')" % (
        server_ip, xmt_data, rcv_data, loss_percent, min_time, avg_time, max_time)  # 注意%s需要加引号

    res = cursor.execute(sql)  # 执行sql语句，返回sql查询成功的记录数目
    conn.commit()
    cursor.close()
    conn.close()
