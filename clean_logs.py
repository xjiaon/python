#!/usr/bin/env python
#coding:utf-8

#功能说明：删除指定目录下的日志文件，路径和正则表达式可以自定义
#编写日期：20180322
#作者：肖剑
#备注：如果需要使用send2trash模块，需额外安装。安装命令：pip install send2trash
#运行环境：python2.7、python3.6

import shutil,os,re,send2trash
import logging,time

ctime = time.strftime('%Y-%m-%d',time.localtime(time.time()))	#定义本地时间
logging.basicConfig(filename='clean_logs_%s.log'%ctime,level=logging.INFO,format=' %(asctime)s - %(levelname)s -  %(message)s')	#日志格式

logging.info('Start of program')
def rmlog(filePath,filenameRegex):
    for filename in os.listdir(filePath):
        fileRegex = filenameRegex.search(filename)
        if fileRegex == None:
            continue
	os.chdir(filePath)
	os.unlink(fileRegex.group())
        logging.info( filePath + fileRegex.group()  + ' 日志文件已经清理!')
        #send2trash.send2trash(fileRegex.group()) #删除到回收站
        
filePath = '/opt/local/tomcat8/logs/'
filenameRegex = re.compile(r'^\w.*\d{4}-\d{2}-\d{2}\.log|.*\d{4}-\d{2}-\d{2}\.txt')

rmlog(filePath,filenameRegex)

logging.info('End of program')
