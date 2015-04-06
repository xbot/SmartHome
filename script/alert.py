#!/usr/bin/env python2
# encoding: utf-8

####################################################
#
# Description:  Alert for invasion using pushbullet.
# Author:       Donie Leigh<donie.leigh at gmail.com>
# License:      MIT
#
####################################################

import sys, getopt, time
from yapbl import PushBullet

API_KEY = ''

def send_alert(image):
    pb = PushBullet(API_KEY)
    timePoint = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    pb.push_note('入侵警报', timePoint + '，发现入侵者！！！')
    pb.push_file(open(image, 'rb'))

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "f:")
    imageFile = ''
    for op, value in opts:
        if op == "-f":
            imageFile = value

    if len(imageFile) == 0:
        sys.stderr.write("Image file missing.\n")
        sys.exit()

    send_alert(imageFile)