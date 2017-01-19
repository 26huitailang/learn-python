# -*- coding: utf-8 -*-
import numpy
import Image
import os
import sys

'''
parser = argparse.ArgumentParser(description=encodeChinese('检测给定的文件夹中的png图片是否包含alpha通道'))
parser.add_argument('--dir', action='store', dest='image_dir',help=encodeChinese('保存图片的路径'))
parser.add_argument('--log', action='store', dest='log_filename',help=encodeChinese('输出错误日志'))
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()
# 判断必须给定的参数
if args.image_dir is None :
    print encodeChinese('没有输入保存图片文件的文件夹')
    sys.exit()
if args.log_filename is None :
    print encodeChinese('没有输入保存错误信息的日志文件名称')
    sys.exit()
rootdir = args.image_dir
errLogDir = args.log_filename
'''

def encodeChinese(msg):
    type = sys.getfilesystemencoding()
    return msg.decode('UTF-8').encode(type)

def check_imgMode(filedir):
    try:
        img = Image.open(filedir)
        return img.mode
    except:
        errInfo = encodeChinese('这不是图片: ') + str(filedir) + '\n'
        print errInfo
        return errInfo
def check_fileMode(filedir):
    fPostfix = os.path.splitext(filedir)[1]
    return fPostfix

def open_imgFile(filedir):
    im = Image.open(filedir)
    im.load()
    return im

def input_rootdir():
    print encodeChinese('请输入要检测的文件夹路径: ')
    rootdir = raw_input()
    print rootdir
    return rootdir

def input_logdir():
    print encodeChinese('请输入错误日志路径: ')
    logdir = raw_input()
    print logdir
    return logdir

def input_targetdir():
    print encodeChinese('请输入处理完成后文件保存路径: ')
    targetdir = raw_input()
    return targetdir

def check_png_alpha(rootdir,errLogDir):
    errFile = open(errLogDir,'w')
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            fName = filename
            filename = rootdir + os.sep + filename
            if check_fileMode(filename) == '.png':
                if check_imgMode(filename) == 'RGBA':
                    print filename
                    try:
                        img = open_imgFile(filename)
                    except:
                        filename = parent + os.sep + fName
                        print encodeChinese('这不是图片: ') + str(filename) +'\n'
                        errFile.write(encodeChinese('这不是图片: ') + '\n')
                        errFile.write(str(filename) + '\n')
                        errFile.write('\n')
                    alpha = img.split()[3]
                    arr = numpy.asarray(alpha)
                    count = 0
                    for i in range(0,img.size[0]-1):
                        for j in range(0,img.size[1]-1):
                            if arr[j][i] < 128:
                                count += 1
                                if count > 10:
                                    break
                    if count > 10:
                        filename = parent + os.sep + fName
                        print str(filename) + ' is have alpha,count = ' + str(count)
                    else:
                        filename = parent + os.sep + fName
                        errFile.write(encodeChinese('这张图片约等于没有alpha通道: ') + '\n')
                        errFile.write(str(filename) + '\n')
                        errFile.write('\n')
                else:
                    filename = parent + os.sep +fName
                    errFile.write(encodeChinese('虽然这是一张png图片,但是它没有alpha通道: ') + '\n')
                    errFile.write(str(filename) + '\n')
                    errFile.write('\n')
            else:
                filename = parent + os.sep +fName
                errFile.write(encodeChinese('这不是png格式的文件: ') + '\n')
                errFile.write(str(filename) + '\n')
                errFile.write('\n')
    errFile.close()

rootdir = input_rootdir()
errLogDir = input_logdir()
check_png_alpha(rootdir,errLogDir)