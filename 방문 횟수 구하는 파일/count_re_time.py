import pandas as pd
import re
from datetime import datetime, timedelta
import datetime

# data_in_path = 'C:/Users/user/Desktop/' # 데이터 파일 경로
# data = pd.read_csv(data_in_path + 'KakaoTalk.csv', encoding = 'utf-8', header = 0) # csv 파일 읽기

def reply_message_time(data, user_name):
    Date, User = list(data['Date']), list(data['User'])
    count = 0

    for i in User:
        if i == user_name:
            count += 1



    re_time_data = []
    for i in Date:
        a = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S')
        re_time_data.append(a)

    delta = re_time_data[len(re_time_data)-1] - re_time_data[0]

    delta = delta.days * 24 * 60 / count

    return delta
