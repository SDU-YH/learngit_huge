import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(r'./MyData')
sys.path.append(r'./MyUI')
import UI
from UI import *
import login
from login import *
import Question
from Question import *
import Draw
from Draw import *
import GetData
from GetData import *
import tkinter
from tkinter import * 

#UI
user=login_page()
#stat_result=use_id_get_game_data.get_handled_data()
#获取用户数据，用户数据处理
#调用训练好的模型
#传出每个颜色的百分比
value_dic={
    '红色':0,
    '蓝色':0,
    '绿色':0,
    '白色':0,
    '黄色':0
}

'''
red_game_data=red_sta(game_data)
blue_game_data=blue_sta(game_data)
green_game_data=green_sta(game_data)
white_game_data=white_sta(game_data)
yellow_game_data=yellow_sta(game_data)
value_dic['红色']=red_tree(red_game_data)
value_dic['蓝色']=blue_tree(_blue_game_data)
value_dic['绿色']=green_tree(_green_game_data)
value_dic['白色1']=white_tree(_white_game_data)
value_dic['黄色']=yellow_tree(_yellow_game_data)

draw(value_dic)
ANA(value_dic)
'''