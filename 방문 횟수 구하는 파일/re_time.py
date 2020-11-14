import pandas as pd
import re
from datetime import datetime, timedelta
import datetime
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# data_in_path = 'C:/Users/user/Desktop/'  # 데이터 파일 주소

# data = pd.read_csv(data_in_path+'okadata.csv', encoding='utf-8') # csv 파일 읽기

def reply_message_time(data):
    time_data =list(data['Date'])

    re_time_data = []
    for i in time_data:
        a = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S')
        re_time_data.append(a)

    time_gap =[]
    for i in range(0, len(re_time_data)-1):
        delta = re_time_data[i+1] - re_time_data[i]
        gap = delta.seconds
        if gap > 60 and gap <= 1200:
            time_gap.append(gap)

    sum = 0
    for i in time_gap:
        sum += i
    aver = sum/len(time_gap)

    return aver

    # print("평균 답장 시간(초):", aver) # 출력
