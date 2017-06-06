#!/usr/bin/python
#-*- coding: utf-8 -*-
# qhf 2017-6-2
# list all files in the folder
import sys
import os
import re
import random

#def walk(filepath):
#    files = os.listdir(filepath)
#    for fi in files:
#       fullfile = os.path.join(filepath, fi)
#   if os.path.isdir(fullfile):
#            walk(fullfile)
#        else:
#            file_list.append(fullfile)

with open('train.txt','w') as f_train_txt:
    img_dir = sys.argv[1]
    txt_dir = sys.argv[2]
    count = 0
    #file_list = []
    #walk(root_dir)
    #print(len(file_list))
    file_list = os.listdir(img_dir)
    inst = []
    for fi in file_list:
        fi.strip('\n')
        #if re.search('.txt', fi):
            #continue
        #else:
        count  +=  1
        #img_path_list = fi.split('/')
        #img_path = "/".join(img_path_list[:-1])
        img_name = os.path.join(img_dir, fi)
        print(img_name)
        txt_name = img_name.replace('TrainImage', 'PCAtrain80')
        txt_name = txt_name.replace('.jpg', '.txt')
        print(txt_name)
        param_list = []
        with open (txt_name, 'r') as params:
            for num in params:
                num.strip('\n')
                param_list.append(num[:10])
        parameters = "\t".join(param_list)
        #print(parameters)
        temp = img_name + '\t' + parameters
        inst.append(temp)

    random.shuffle(inst)
    for item in inst:
        f_train_txt.write('{}\n'.format(item))

    print(count)
