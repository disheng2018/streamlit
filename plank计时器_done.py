import streamlit as st
import pandas as pd
import numpy as np
import time, datetime

st.sidebar.subheader("workout计时器")
st.sidebar.markdown("""    
     > 储备心率=最大心率-静息心率。`最大心率 = 220 - 年龄`，年龄越小最大心率越快；静息心率是指在静息、不活动的安静状态下，每分钟心跳的次数。
     
     小强度运动：（最大心率-静息心率）× 44% + 静息心率\n
     中强度运动：（最大心率-静息心率）× 75% + 静息心率\n
     大强度运动：（最大心率-静息心率）× 85% + 静息心率
    """)
        
