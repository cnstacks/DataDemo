from django.db import models

# Create your models here.

from django.db import models
from datetime import datetime


class Return(models.Model):
    server_ip = models.CharField(max_length=50, verbose_name=u"服务器IP地址")
    xmt_data = models.IntegerField(default=100, verbose_name=u"发送的数据包大小")
    rcv_data = models.IntegerField(default=100, verbose_name=u"接收的数据包大小")  # datetime.now()不添加括号
    loss_percent = models.FloatField(max_length=30, verbose_name=u"丢包百分比")
    min_time = models.FloatField(max_length=30, verbose_name=u"PING的最小返回值")
    avg_time = models.FloatField(max_length=30, verbose_name=u"PING的平均返回值")
    max_time = models.FloatField(max_length=30, verbose_name=u"PING的最大返回值")
    timestamp = models.DateTimeField(default=datetime.now, verbose_name=u"命令执行时间")

    class Meta:
        verbose_name = u"PING的返回记录"
        verbose_name_plural = verbose_name
