# -*- conding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#新建一个模型类
# Create your models here.
from django.db import models

#新增元组用于设置消息类型枚举项
KIND_CHOICES=(
    ('Pyton技术','Python技术'),
    (' 数据库技术',' 数据库技术'),
    (' 经济学',' 经济学'),
    (' 文体咨询',' 经济学'),
    (' 个人心情',' 个人心情'),
    (' 其他',' 其他'),
)
class Moment(models.Model):
    content=models.CharField(max_length=300)  #内容
    user_name=models.CharField(max_length=20,default='匿名' )   #发布人姓名
    #修改kind，加入枚举
    kind=models.CharField(max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0] )    #消息类型
