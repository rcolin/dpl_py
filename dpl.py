import shutil
import logging
import os
import sys, getopt

FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
#logging.basicConfig(format=FORMAT)
#logging.basicConfig(format=FORMAT,filename=nohup.log,level=logging.INFO)
#logging.basicConfig(format=FORMAT,level=logging.INFO)
LOG_FILENAME = 'nohup.log'
logging.basicConfig(format=FORMAT,filename=LOG_FILENAME,level=logging.DEBUG)

if __name__ == '__main__':
    #info batch starting 
    logging.info('****************** Batch starting')

    #retrive param
    logging.info('Retrive params')

    #check param
    logging.info('Checking params')

    #make recopy
    logging.info('copy files starting...')

    #logging.info('Working in %s' % 'start copy')
    shutil.copy("tests/source/file1.txt", "tests/target/")

    logging.info('copy files finished with sucess!')
    #make symbolic link
    logging.info('copy files starting...')
    #info batch ended
    logging.info('****************** End of batch')