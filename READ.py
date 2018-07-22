#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import logging
import datetime
import os
import time

source_folder_path = "/Users/binghe/Downloads/zoe/"
output_folder_path = "/Users/binghe/Downloads/zoe/" + datetime.datetime.today().strftime('%Y%m%d%H%M%S')
VERSION = "0.0.1"


def init():
    set_logging()
    if not os.path.exists(source_folder_path):
        logging.error("Source folder " + source_folder_path + " does not exist, please check.")
        exit(1)

    if not os.path.exists(output_folder_path):
        logging.warning("Destination output folder " + output_folder_path + " does not exist, create it.")
        os.mkdir(output_folder_path, 0o777)


def menu():
    while True:
        print("-" * 30)
        print("Enter your option:")
        print("1.IBS")
        print("2.WSO")
        print("3.ALL")
        print("-" * 30)
        choose = int(input("Choose your option please :"))
        if 1 == choose:
            print("Preparing IBS data...")
            process_ibs_dir(source_folder_path + "IBS/")
        elif 2 == choose:
            print("Preparing WSO data...")
            process_wso_dir(source_folder_path + "WSO/")
        elif 3 == choose:
            print("Preparing data for all source...")
            process_ibs_dir(source_folder_path + "IBS/")
            process_wso_dir(source_folder_path + "WSO/")
        else:
            print("Your input is incorrect.")
            continue


def set_logging():
    """设置日志输出格式
    :param: none
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s : %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='./jie.log',
                        filemode='w')
    # 设置同时输出日志到日志文件以及Console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def get_file_lists(folder_path):
    """usage: 查找指定目录下指定类型的文件列表
    :param folder_path: 要查找的文件夹
    :return: result_file_list: 符合条件的文件列表
    """
    result_file_list = []
    # result_file_list.extend(glob.glob(folder_path + extension))
    if not result_file_list:
        logging.warning(folder_path + " found 0 file, please check.")
    return result_file_list


def parse_single_file(file_path):
    """解析一个文件
    :param file_path: 文件路径
    """
    data = []
    filename = os.path.basename(file_path)
    try:
        with open(file_path, 'r') as f:
            data = f.readlines(-1)
    except Exception as e:
        logging.error("Exception while reading " + file_path, e)

    try:
        with open(os.path.join(output_folder_path, filename), 'w') as ff:
            # 这里可以按照你的意愿修改源文件内容
            data[0] = data[0].replace("g", "j")
            ff.writelines(data)
    except Exception as e:
        logging.error("Exception while writing " + output_folder_path + filename, e)


def process_ibs_dir(ibs_dir_path):
    """usage: 处理ibs目录下所有文件
     :param ibs_dir_path: ibs文件夹
     :return:
     """
    print("Processing IBS " + ibs_dir_path + ", please wait.")
    time.sleep(5)
    print("Congratulations, IBS " + ibs_dir_path + " process done.")


def process_wso_dir(wso_dir_path):
    """usage: 处理ibs目录下所有文件
     :param wso_dir_path: wso文件夹
     :return:
     """
    print("Processing WSO " + wso_dir_path + ", please wait")
    time.sleep(3)
    print("Congratulations, WSO " + wso_dir_path + " process done")


def main():
    menu()
    init()
    all_file_lists = get_file_lists(source_folder_path)
    for f in all_file_lists:
        parse_single_file(f)
    logging.info("Process done, please check " + output_folder_path)


if __name__ == '__main__':
    main()