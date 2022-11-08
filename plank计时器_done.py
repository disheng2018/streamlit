import streamlit as st
import pandas as pd
import numpy as np
import time, datetime
# import plotly.figure_factory as ff

def history():
    df = pd.DataFrame(pd.read_csv(r"数据.csv"))
    #设置date列为时间格式
    df['Date'] = pd.to_datetime(df.Date, format = '%Y-%m-%d')
    sum_time = 0
    for i in range(1,7):
        h = df['Time' + str(i)].sum()
        sum_time = sum_time +h 
    st.write("锻炼时长合计", round(sum_time, 2), "分钟")
    #将date列作为index
    df.index = df['Date']
    st.bar_chart(df[["Time6","Time5","Time4","Time3","Time2","Time1"]])
    st.dataframe(df)

st.sidebar.subheader("workout计时器")
st.sidebar.markdown("""    
     > 储备心率=最大心率-静息心率。`最大心率 = 220 - 年龄`，年龄越小最大心率越快；静息心率是指在静息、不活动的安静状态下，每分钟心跳的次数。
     
     小强度运动：（最大心率-静息心率）× 44% + 静息心率\n
     中强度运动：（最大心率-静息心率）× 75% + 静息心率\n
     大强度运动：（最大心率-静息心率）× 85% + 静息心率
    """)
# history()

if __name__== '__main__':

    if st.sidebar.button("最新数据"):
        history()
        

    choose = st.radio(
        "选择计时方式",
        ('倒计时', '直接计时'))

    if choose == '倒计时':
        # st.write('选择倒计时方式')
        # if st.sidebar.button("计时器"):
        st.markdown("""
        #### 定时器
        点击“开始”按钮开始计时
        """)
        
        time_plank = st.slider('定时器', 0, 10)
        st.write("plank定时：", time_plank, "分钟")

        global t
        t = time_plank * 60

        df = pd.DataFrame(pd.read_csv(r"数据.csv"))
        # st.dataframe(df)
        d = datetime.date.today()
        #设置date列为时间格式
        df['Date'] = pd.to_datetime(df.Date, format = '%Y-%m-%d')
        #将date列作为index
        df.index = df['Date']

        if st.button('开始'):
            # progress_f(t)
            df_show = pd.DataFrame({
                "first_row":[0]})
            # st.dataframe(df_show)
            chart_show = st.area_chart(df_show)
            with st.empty():
                for seconds in range(t):
                    st.write(f"⏳ 还剩 **{t - seconds -1}** 秒钟！")
                    chart_show.add_rows({
                        "last_row":[seconds]
                    })
                    time.sleep(1)

                d = datetime.date.today()
                for i in range(10):
                    if df.loc[str(d),'Time' + str(i+1)] == 0:
                        df.loc[str(d),'Time' + str(i+1)] = time_plank
                        # print('Time' + str(i+1))
                        # print(df)
                        df.to_csv(r"数据.csv")
                        break
                st.bar_chart(df[["Time6","Time5","Time4","Time3","Time2","Time1"]])

            st.success('计时结束')
            st.balloons()

    else:
        # st.write("选择直接计时方式")
        col1, col2 = st.columns(2)
        df = pd.DataFrame(pd.read_csv(r"数据.csv"))
        #设置date列为时间格式
        df['Date'] = pd.to_datetime(df.Date, format = '%Y-%m-%d')
        #将date列作为index
        df.index = df['Date']

        with col1:
            if st.button("开始计时"):
                df_show = pd.DataFrame({
                    "first_row":[0]})
                chart_show = st.area_chart(df_show)
                t0 = time.time()
                st.session_state['t0'] = t0
                with st.empty():
                    for sec in range(10000000000):
                        st.write(f"⏳ 已经坚持 **{sec}** 秒钟！")
                        chart_show.add_rows({
                            "last_row":[sec]
                        })
                        time.sleep(1)
                        t1 = time.time()
                        st.session_state['t1'] = t1

        with col2:
            if st.button("停止计时"):
                d = datetime.date.today()
                # st.write(st.session_state.key)
                t2 = st.session_state.t1 - st.session_state.t0
                for i in range(10):
                    if df.loc[str(d),'Time' + str(i+1)] == 0:
                        df.loc[str(d),'Time' + str(i+1)] = t2 / 60
                        # print('Time' + str(i+1))
                        # print(df)
                        df.to_csv(r"数据.csv")
                        break
                st.bar_chart(df[["Time6","Time5","Time4","Time3","Time2","Time1"]])
