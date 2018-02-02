# -*- coding: utf-8 -*- 
# # Created by liangqian@xxxx.com on 2017/6/17.
# Description   : global value

import sys
sys.path.append('../common')

# 根目录路径
BASE_PATH = sys.path[0] + '/../'

# log配置文件路径
LOG_CONF_PATH = BASE_PATH + 'conf/logger.conf'

#30.192库数据库配置类
# local_db = cm.DBInfo("pro_idc")

############# hive #################
HIVE_HOME = "/usr/local/sxt/hive/apache-hive-1.2.2-bin"
#hiveserver2的所在服务器IP
HIVE_DB_HOST = "192.168.46.101"
#hiveserver2的端口
HIVE_PORT = "10000"
#hive连接元信息数据库mysql所需要的账号密码
HIVE_USER = "hive"
HIVE_PWD = "hive"
#hive的库
HIVE_DB = "user_image"
#HIVE_AUTH_MECHANISM = "PLAIN"
HIVE_AUTH_MECHANISM = "NOSASL"

