import logging
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
 
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')


###直接在终端打印，所以直接把日志生成到文件




#!/usr/bin/env python
#coding:utf-8

import logging,logging.handlers

def WriteLog(log_name):
    log_filename = "/tmp/testlog"
    log_level = logging.DEBUG
    format = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)2d]-%(funcName)s %(levelname)s %(message)s')
    handler = logging.handlers.RotatingFileHandler(log_filename, mode='a', maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(format)

    logger = logging.getLogger(log_name)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger         

if __name__ == "__main__":
    WriteLog("api").info("123")
#    writelog = WriteLog("api")
#    writelog.info("123")
