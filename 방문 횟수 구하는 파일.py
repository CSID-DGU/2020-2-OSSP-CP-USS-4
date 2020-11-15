import pandas as pd
import re
from datetime import datetime, timedelta
import datetime

data_in_path = 'C:/Users/user/Desktop/'
data = pd.read_csv(data_in_path + 'KakaoTalk.csv', encoding = 'utf-8', header = 0)

Date, User = list(data['Date']), list(data['User'])
count = 0

for i in User:
    if i == '16엄순호':
        count += 1

print(count)

re_time_data = []
for i in Date:
    a = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S')
    re_time_data.append(a)

delta = re_time_data[len(re_time_data)-1] - re_time_data[0]

print(delta)
print(delta.days * 24 * 60 / count)
