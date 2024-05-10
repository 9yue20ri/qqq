
# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk


import streamlit as st
from streamlit_option_menu import option_menu



#from PIL import Image
# 设置页面配置
st.set_page_config(page_title="萌坦坦的网站", page_icon="?", layout="wide")

# 通过 css样式隐藏主菜单和页脚
hide_menu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(hide_menu,unsafe_allow_html=True)

# 配置左侧菜单项
with st.sidebar:
    choose = option_menu("萌坦坦的网站", ["介绍","生成表格","国际地图", "功能查询","机器人成员","颜值鉴定", "图片","翻译","电子书","发送邮件","地图","数据可视化", "在线语音合成","音乐/视频","聊天机器人"],
                         icons=["activity","alarm","alexa","android2","apple",'house', 'book-half', 'bar-chart', 'badge-vo',"boombox-fill","cast","cloud-upload"],
                         menu_icon="bullseye", default_index=0)
    st.video(r"E:\人工智能\介绍.mp4")
    import streamlit as st
    import numpy as np
    import pandas as pd
    #下拉单
    add_selectbox = st.sidebar.selectbox(
        "Which one?",
        ("C++", "Java", "Python")
    )
						 
if choose == "介绍":
    st.title("欢迎来到萌坦坦的网站")
    st.write("介绍视频")
    st.video(r"E:\人工智能\介绍.mp4")



if choose == "功能查询":

    tubiao = st.title('图标查询')
    st.markdown('[图标链接](https://icons.bootcss.com/#icons)')
    st.title('时间和日历')
    date = st.date_input('日历')
    st.title('色块查询')
    color = st.color_picker('颜色')
    st.title("功能说明：")
    gongneng = st.markdown('''功能启动说明：指定端口为8882 获取使用统计信息,前端查询，不等待，直接刷新,
    主题设置为黑色 命令如下：
    streamlit run --server.port 8882 --browser.gatherUsageStats True
    --runner.fastReruns True --theme.base dark --theme.font 'sans serif' 
    streamlit_function.py''')
    #########################################
    #进度条
    import time

    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
#############################################################
    ###临时显示消息 气球
    import time

    with st.spinner('Wait for it...'):
        time.sleep(3)
    st.success('Done!')
    st.balloons()

    ##################################################



	
################################################################机器人成员介绍	

if choose == "颜值鉴定":
    import os
    selecte = option_menu(None, ["开始鉴定", "查看结果"],
                          icons=["file-music-fill", "badge-vo-fill"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    st.write(r"请将图片放进此处E:\xingbiejianding\xingbiejianding或者上传")
    st.file_uploader(label='选择你要鉴定的图片', accept_multiple_files=True, help="上传图片类型等等等等")
    if selecte == "开始鉴定":
        pass


        # os.system(r"E:\xingbiejianding\Scripts\python.exe E:\xingbiejianding\xingbiejianding\xingbiejianding_jiaoben.py")

    elif selecte == "查看结果":
        import streamlit as st
        from PIL import Image

        image = Image.open(r'E:\xingbiejianding\xingbiejianding\demo.jpg')

        st.image(image,
                 caption='标题',
                 width=500
                 )





        #
        #
        # image = Image.open(r"E:\xingbiejianding\xingbiejianding\demo.jpg")
        #
        # st.image(image,
        #          caption='标题',
        #          width=500
        #          )



		
#################################################数据分析
elif choose == "数据可视化":
    # 结合Plotly来添加柱状图、饼图和折线图
    import plotly.express as px
    # 将图表分为三种
    selecte = option_menu(None, ["柱状图","饼图","折线图"],
                           icons=["bar-chart-fill","pie-chart-fill","graph-up"],
                           menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "柱状图":
        # px.data.tips()`是Plotly Express提供的一个示例数据集，其中包含有关餐厅小费的数据它是一个DataFrame对象
        data_bar = px.data.tips()
        fig_bar = px.bar(data_bar, x='day', y='total_bill', color='sex')
        st.plotly_chart(fig_bar)

    elif selecte == "饼图":
        data_pie = px.data.tips()
        fig_pie = px.pie(data_pie, names='day')
        st.plotly_chart(fig_pie)

    elif selecte == "折线图":
        data_line = px.data.gapminder().query("country=='China'")
        fig_line = px.line(data_line, x='year', y='pop')
        st.plotly_chart(fig_line)
#################################################语音合成
elif choose == "在线语音合成":
    import pyttsx3  # 引入说话程序
    # 设置语速、语言类型
    st.header("在线语音合成使用")
    st.info(
        "使用说明：\n\n 输入一段文本会返回一段语音;输入完后按回车键，会自动播放语音！！\n\n 注：输入框的内容有变动时，按空格才会有效哦!!")
    text = st.text_input("请输入一段文字")
    if len(text) != 0 and text != None:
        def shuohua():
            engine = pyttsx3.init()
            engine.setProperty("rate", 180)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[2].id)  # 设置当前声音为“男性”，当前声音可读中文也可读英文
            engine.say(text)
            engine.runAndWait()
        shuohua()


    # 结合百度api进行在线语音合成
    # import BaiduRead as baidu
    # # 页面文字说明
    # st.header("在线语音合成使用")
    # st.info("使用说明：\n\n 输入一段文本会返回一段语音;输入完后按回车键，会自动播放语音！！\n\n 注：输入框的内容有变动时，按空格才会有效哦!!")
    # text = st.text_input("请输入一段文字")
    # if len(text) != 0 and text != None:
    #     baidu.read_text(text)

		
################################################播放音乐视频
elif choose == "音乐/视频":
    selecte = option_menu(None, ["音乐", "视频"],
                          icons=["file-music-fill", "badge-vo-fill"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "音乐":
        st.write("1. 像针锥一样")
        st.audio(r"D:\KuGou\未知歌手 - 像针锥一样 (伴奏).mp3")
        st.write("2. 阿勒比")
        st.audio(r"C:\Users\Administrator.lenovo1\Documents\WeChat Files\wxid_fhd3tqt78y9022\FileStorage\File\2023-07\阿勒比(1).mp3")
        st.write("3. 阿拉斯加海湾")
        st.audio("D:\KuGou\程溪颜 - 阿拉斯加海湾 (伴奏).mp3")

    elif selecte == "视频":
        st.video(r"E:\人工智能\介绍.mp4")

#####################################################聊天机器人


elif choose == "聊天机器人":
    import mkcloud
    import pyttsx3  # 引入说话程序
    option_menu(None, ["聊天对话"],
                          icons=["list-task"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    st.header("聊天框")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What's your message?"):
        # Display user message in chat message container
        dafu = mkcloud.robot.chat(prompt)
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"{dafu}"
        # Display assistant response in chat message container

        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        def shuohua():
            engine = pyttsx3.init()
            engine.setProperty("rate", 180)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)  # 设置当前声音为“男性”，当前声音可读中文也可读英文
            engine.say(response)
            engine.runAndWait()
        shuohua()
##############################################################################################
elif choose == "翻译":
    import requests
    import json
    selecte3 = option_menu(None, ["单词翻译"],
                           icons=['house'],
                           menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte3 == "单词翻译":
        st.header("中英单词互翻神器")
        st.info("要翻译中文单词，请输入中文，会返回对应英文；\n\n\n\n要翻译英文单词，请输入英文，会返回对应中文;")

        danci = st.text_input("请输入要查找的中文单词或英文单词")
        fanhui = requests.get("http://dict.iciba.com/dictionary/word/suggestion?word=" + danci)
        data1 = fanhui.text
        data2 = json.loads(data1)
        for i in range(len(data2["message"])):
            st.write(data2["message"][i]["key"], data2["message"][i]["paraphrase"])

        # 隐藏按钮及底部链接
        sysmenu = '''
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        '''
        st.markdown(sysmenu, unsafe_allow_html=True)
###########################################################################
if choose=="图片":

    import streamlit as st
    from PIL import Image

    image = Image.open(r'E:\xiazai\pic\2.png')

    st.image(image,
             caption='标题',
             width=500
             )
#############################################################################

if choose == "地图":
    import pandas as pd

    st.title("大庆地图")

    # 大庆市中心的经纬度
    beijing_coords = [[46.0390,124.8105 ]]
    df = pd.DataFrame(beijing_coords, columns=['lat', 'lon'])
    # 使用 st.map 显示地图
    st.map(df, zoom=11)
#############################################################################
if choose == "电子书":


    st.markdown('''
    # 静夜思
    床前**明月**光，疑是地上霜。
    举头望**明月**，低头思故乡。
    ''')

    st.text('''
    静夜思
    床前明月光，疑是地上霜。
    举头望明月，低头思故乡。
    ''')
    def dianzishu():
        try:


            textt = "静夜思床前明月光，疑是地上霜。举头望明月，低头思故乡。"
            import pyttsx3  # 引入说话程序
            pyttsx3.speak(textt)
        except Exception as e:
            print("等待上个任务完成！")
    dianzishu()
#######################################################################
if choose == "国际地图":
    import pandas as pd
    import numpy as np
    import streamlit as st

    df = pd.DataFrame(np.random.randn(1, 1) / [50, 50] + [37.76, -122.4],
                      columns=['lat', 'lon'])
    st.map(df)

elif choose == "发送邮件":


    text = st.text_input("请输入邮件标题")
    text1= st.text_input("请输入邮件内容")

    selecte = option_menu(None, ["发送"],
                          icons=["send"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "发送":

        import smtplib
        from email.mime.text import MIMEText
        from email.header import Header
        from email.utils import formataddr

        # 设置要登录的邮箱
        smtp_obj = smtplib.SMTP('smtp.qq.com')
        # 登录邮箱
        smtp_obj.login('550840562@qq.com', 'pmfmbenfmblwbfff')
        # 编辑内容
        mail_text = f'{text1}'
        # plain 原生文本模式
        msg_body = MIMEText(mail_text, 'plain', 'utf-8')
        # 设置从哪发送的
        msg_body['From'] = formataddr((str(Header('萌坦坦', 'utf-8')), '550840562@qq.com'))
        msg_body['Subject'] = Header(f'{text}', 'utf-8')
        # 发送邮件
        # smtp_obj.sendmail('550840562@qq.com', '550840562@qq.com', msg_body.as_string())
    else:
        pass