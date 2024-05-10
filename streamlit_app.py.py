
# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk


import streamlit as st
from streamlit_option_menu import option_menu



#from PIL import Image
# ����ҳ������
st.set_page_config(page_title="��̹̹����վ", page_icon="?", layout="wide")

# ͨ�� css��ʽ�������˵���ҳ��
hide_menu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(hide_menu,unsafe_allow_html=True)

# �������˵���
with st.sidebar:
    choose = option_menu("��̹̹����վ", ["����","���ɱ��","���ʵ�ͼ", "���ܲ�ѯ","�����˳�Ա","��ֵ����", "ͼƬ","����","������","�����ʼ�","��ͼ","���ݿ��ӻ�", "���������ϳ�","����/��Ƶ","���������"],
                         icons=["activity","alarm","alexa","android2","apple",'house', 'book-half', 'bar-chart', 'badge-vo',"boombox-fill","cast","cloud-upload"],
                         menu_icon="bullseye", default_index=0)
    st.video(r"E:\�˹�����\����.mp4")
    import streamlit as st
    import numpy as np
    import pandas as pd
    #������
    add_selectbox = st.sidebar.selectbox(
        "Which one?",
        ("C++", "Java", "Python")
    )
						 
if choose == "����":
    st.title("��ӭ������̹̹����վ")
    st.write("������Ƶ")
    st.video(r"E:\�˹�����\����.mp4")



if choose == "���ܲ�ѯ":

    tubiao = st.title('ͼ���ѯ')
    st.markdown('[ͼ������](https://icons.bootcss.com/#icons)')
    st.title('ʱ�������')
    date = st.date_input('����')
    st.title('ɫ���ѯ')
    color = st.color_picker('��ɫ')
    st.title("����˵����")
    gongneng = st.markdown('''��������˵����ָ���˿�Ϊ8882 ��ȡʹ��ͳ����Ϣ,ǰ�˲�ѯ�����ȴ���ֱ��ˢ��,
    ��������Ϊ��ɫ �������£�
    streamlit run --server.port 8882 --browser.gatherUsageStats True
    --runner.fastReruns True --theme.base dark --theme.font 'sans serif' 
    streamlit_function.py''')
    #########################################
    #������
    import time

    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
#############################################################
    ###��ʱ��ʾ��Ϣ ����
    import time

    with st.spinner('Wait for it...'):
        time.sleep(3)
    st.success('Done!')
    st.balloons()

    ##################################################



	
################################################################�����˳�Ա����	

if choose == "��ֵ����":
    import os
    selecte = option_menu(None, ["��ʼ����", "�鿴���"],
                          icons=["file-music-fill", "badge-vo-fill"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    st.write(r"�뽫ͼƬ�Ž��˴�E:\xingbiejianding\xingbiejianding�����ϴ�")
    st.file_uploader(label='ѡ����Ҫ������ͼƬ', accept_multiple_files=True, help="�ϴ�ͼƬ���͵ȵȵȵ�")
    if selecte == "��ʼ����":
        pass


        # os.system(r"E:\xingbiejianding\Scripts\python.exe E:\xingbiejianding\xingbiejianding\xingbiejianding_jiaoben.py")

    elif selecte == "�鿴���":
        import streamlit as st
        from PIL import Image

        image = Image.open(r'E:\xingbiejianding\xingbiejianding\demo.jpg')

        st.image(image,
                 caption='����',
                 width=500
                 )





        #
        #
        # image = Image.open(r"E:\xingbiejianding\xingbiejianding\demo.jpg")
        #
        # st.image(image,
        #          caption='����',
        #          width=500
        #          )



		
#################################################���ݷ���
elif choose == "���ݿ��ӻ�":
    # ���Plotly�������״ͼ����ͼ������ͼ
    import plotly.express as px
    # ��ͼ���Ϊ����
    selecte = option_menu(None, ["��״ͼ","��ͼ","����ͼ"],
                           icons=["bar-chart-fill","pie-chart-fill","graph-up"],
                           menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "��״ͼ":
        # px.data.tips()`��Plotly Express�ṩ��һ��ʾ�����ݼ������а����йز���С�ѵ���������һ��DataFrame����
        data_bar = px.data.tips()
        fig_bar = px.bar(data_bar, x='day', y='total_bill', color='sex')
        st.plotly_chart(fig_bar)

    elif selecte == "��ͼ":
        data_pie = px.data.tips()
        fig_pie = px.pie(data_pie, names='day')
        st.plotly_chart(fig_pie)

    elif selecte == "����ͼ":
        data_line = px.data.gapminder().query("country=='China'")
        fig_line = px.line(data_line, x='year', y='pop')
        st.plotly_chart(fig_line)
#################################################�����ϳ�
elif choose == "���������ϳ�":
    import pyttsx3  # ����˵������
    # �������١���������
    st.header("���������ϳ�ʹ��")
    st.info(
        "ʹ��˵����\n\n ����һ���ı��᷵��һ������;������󰴻س��������Զ�������������\n\n ע�������������б䶯ʱ�����ո�Ż���ЧŶ!!")
    text = st.text_input("������һ������")
    if len(text) != 0 and text != None:
        def shuohua():
            engine = pyttsx3.init()
            engine.setProperty("rate", 180)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[2].id)  # ���õ�ǰ����Ϊ�����ԡ�����ǰ�����ɶ�����Ҳ�ɶ�Ӣ��
            engine.say(text)
            engine.runAndWait()
        shuohua()


    # ��ϰٶ�api�������������ϳ�
    # import BaiduRead as baidu
    # # ҳ������˵��
    # st.header("���������ϳ�ʹ��")
    # st.info("ʹ��˵����\n\n ����һ���ı��᷵��һ������;������󰴻س��������Զ�������������\n\n ע�������������б䶯ʱ�����ո�Ż���ЧŶ!!")
    # text = st.text_input("������һ������")
    # if len(text) != 0 and text != None:
    #     baidu.read_text(text)

		
################################################����������Ƶ
elif choose == "����/��Ƶ":
    selecte = option_menu(None, ["����", "��Ƶ"],
                          icons=["file-music-fill", "badge-vo-fill"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "����":
        st.write("1. ����׶һ��")
        st.audio(r"D:\KuGou\δ֪���� - ����׶һ�� (����).mp3")
        st.write("2. ���ձ�")
        st.audio(r"C:\Users\Administrator.lenovo1\Documents\WeChat Files\wxid_fhd3tqt78y9022\FileStorage\File\2023-07\���ձ�(1).mp3")
        st.write("3. ����˹�Ӻ���")
        st.audio("D:\KuGou\��Ϫ�� - ����˹�Ӻ��� (����).mp3")

    elif selecte == "��Ƶ":
        st.video(r"E:\�˹�����\����.mp4")

#####################################################���������


elif choose == "���������":
    import mkcloud
    import pyttsx3  # ����˵������
    option_menu(None, ["����Ի�"],
                          icons=["list-task"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    st.header("�����")

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
            engine.setProperty('voice', voices[0].id)  # ���õ�ǰ����Ϊ�����ԡ�����ǰ�����ɶ�����Ҳ�ɶ�Ӣ��
            engine.say(response)
            engine.runAndWait()
        shuohua()
##############################################################################################
elif choose == "����":
    import requests
    import json
    selecte3 = option_menu(None, ["���ʷ���"],
                           icons=['house'],
                           menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte3 == "���ʷ���":
        st.header("��Ӣ���ʻ�������")
        st.info("Ҫ�������ĵ��ʣ����������ģ��᷵�ض�ӦӢ�ģ�\n\n\n\nҪ����Ӣ�ĵ��ʣ�������Ӣ�ģ��᷵�ض�Ӧ����;")

        danci = st.text_input("������Ҫ���ҵ����ĵ��ʻ�Ӣ�ĵ���")
        fanhui = requests.get("http://dict.iciba.com/dictionary/word/suggestion?word=" + danci)
        data1 = fanhui.text
        data2 = json.loads(data1)
        for i in range(len(data2["message"])):
            st.write(data2["message"][i]["key"], data2["message"][i]["paraphrase"])

        # ���ذ�ť���ײ�����
        sysmenu = '''
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        '''
        st.markdown(sysmenu, unsafe_allow_html=True)
###########################################################################
if choose=="ͼƬ":

    import streamlit as st
    from PIL import Image

    image = Image.open(r'E:\xiazai\pic\2.png')

    st.image(image,
             caption='����',
             width=500
             )
#############################################################################

if choose == "��ͼ":
    import pandas as pd

    st.title("�����ͼ")

    # ���������ĵľ�γ��
    beijing_coords = [[46.0390,124.8105 ]]
    df = pd.DataFrame(beijing_coords, columns=['lat', 'lon'])
    # ʹ�� st.map ��ʾ��ͼ
    st.map(df, zoom=11)
#############################################################################
if choose == "������":


    st.markdown('''
    # ��ҹ˼
    ��ǰ**����**�⣬���ǵ���˪��
    ��ͷ��**����**����ͷ˼���硣
    ''')

    st.text('''
    ��ҹ˼
    ��ǰ���¹⣬���ǵ���˪��
    ��ͷ�����£���ͷ˼���硣
    ''')
    def dianzishu():
        try:


            textt = "��ҹ˼��ǰ���¹⣬���ǵ���˪����ͷ�����£���ͷ˼���硣"
            import pyttsx3  # ����˵������
            pyttsx3.speak(textt)
        except Exception as e:
            print("�ȴ��ϸ�������ɣ�")
    dianzishu()
#######################################################################
if choose == "���ʵ�ͼ":
    import pandas as pd
    import numpy as np
    import streamlit as st

    df = pd.DataFrame(np.random.randn(1, 1) / [50, 50] + [37.76, -122.4],
                      columns=['lat', 'lon'])
    st.map(df)

elif choose == "�����ʼ�":


    text = st.text_input("�������ʼ�����")
    text1= st.text_input("�������ʼ�����")

    selecte = option_menu(None, ["����"],
                          icons=["send"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "����":

        import smtplib
        from email.mime.text import MIMEText
        from email.header import Header
        from email.utils import formataddr

        # ����Ҫ��¼������
        smtp_obj = smtplib.SMTP('smtp.qq.com')
        # ��¼����
        smtp_obj.login('550840562@qq.com', 'pmfmbenfmblwbfff')
        # �༭����
        mail_text = f'{text1}'
        # plain ԭ���ı�ģʽ
        msg_body = MIMEText(mail_text, 'plain', 'utf-8')
        # ���ô��ķ��͵�
        msg_body['From'] = formataddr((str(Header('��̹̹', 'utf-8')), '550840562@qq.com'))
        msg_body['Subject'] = Header(f'{text}', 'utf-8')
        # �����ʼ�
        # smtp_obj.sendmail('550840562@qq.com', '550840562@qq.com', msg_body.as_string())
    else:
        pass