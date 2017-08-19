# -*- coding:utf-8 -*-
from ConfigParser import ConfigParser
#初始化
config_txt='config.conf'
config=ConfigParser()
#读取配置文件
config.read(config_txt)
# 打印初始的问候语，要查看的区段是messages
print config.get('messages','greeting')
# 使用配置文件中的一个问题获取半径
radius=input(config.get('messages','question')+':\n')
# 打印配置文件中的结果信息
print config.get('messages','result')
# getfloat()将config的值转换为float类型
print config.getfloat('numbers','Pi')*radius**2

cp=ConfigParser() #得到一个配置config对象
cp.read('dbconfig.conf')# 配置的内容就读到config对象里面
print 'all sections:', cp.sections()        # sections: ['db', 'ssh']
print 'options of [db]:', cp.options('db')  # options of [db]: ['host', 'port', 'user', 'pass']
print 'items of [ssh]:', cp.items('ssh')    # items of [ssh]: [('host', '192.168.1.101'), ('user', 'huey'), ('pass', 'huey')]
