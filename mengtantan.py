
# -*- coding: UTF-8 -*-
# coding= UTF-8


import streamlit as st
from streamlit_option_menu import option_menu



#from PIL import Image
# 设置页面配置
st.set_page_config(page_title="现代智能网站", page_icon="?", layout="wide")


# 配置左侧菜单项
with st.sidebar:
    choose = option_menu("现代智能网站", ["介绍","生成表格","AI聊天","国际地图", "功能查询","机器人成员",
                                          "颜值鉴定", "图片","翻译","电子书","发送邮件","地图","数据可视化",
                                          "在线语音合成","音乐/视频","聊天机器人"],
                         icons=["box-fill","bank","badge-ar-fill","award","activity",
                                "alarm","alexa","android2","apple",'house', 'book-half',
                                'bar-chart', 'badge-vo',"boombox-fill","cast","cloud-upload"],
                         menu_icon="bullseye", default_index=0)



