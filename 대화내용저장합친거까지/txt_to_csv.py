#-*-coding:utf-8-*-
import re
import pandas as pd
import datetime as dt
import re_time
import os

data_in_path = os.path.dirname(os.path.realpath(__file__))  # 데이터 파일 주소

def read_kko_msg(filename):
    with open(filename, encoding = 'utf-8') as f:
        msg_list = f.readlines()
    return msg_list

def apply_kko_regex(msg_list):
    kko_pattern = re.compile("\[([\S\s]+)\] \[(오전|오후) ([0-9:\s]+)\] ([^\n]+)")
    kko_date_pattern = re.compile("--------------- ([0-9]+년 [0-9]+월 [0-9]+일) ")

    kko_parse_result = list()
    cur_date = ""

    for msg in msg_list:
        if len(kko_date_pattern.findall(msg)) > 0:
        # 패턴에 해당하는 것이 있을 경우, 아래의 코드를 실행한다.
            cur_date = dt.datetime.strptime(kko_date_pattern.findall(msg)[0], "%Y년 %m월 %d일")
            # finall() 정규식으로 찾으면, 결과 문자열의 리스트를 리턴
            cur_date = cur_date.strftime("%Y-%m-%d")
            # cur_date에 날짜를 넣는다.
        else:
            kko_pattern_result = kko_pattern.findall(msg)
            # kko_pattern_result에 findall()을 통해 정규식으로 문자열의 리스트를 리턴
            if len(kko_pattern_result) > 0:
            # 패턴에 해당하는 것이 있을 경우 아래의 코드를 실행한다.
                tokens = list(kko_pattern_result[0])
                # tokens에 패턴에 해당하는 것을 전부 저장한다.
                pattern = re.compile("[0-9]+")
                cur_hour = pattern.findall(tokens[2])[0]
                # 시간 반환
                cur_minute = pattern.findall(tokens[2])[1]
                # 분 반환
                if tokens[1] == '오전' and cur_hour == '12':
                    cur_hour = '0'
                    tokens[2] = ("%s:%s"%(cur_hour, cur_minute))
                    del tokens[1]
                elif tokens[1] == '오전':
                    del tokens[1]
                elif (tokens[1] == '오후' and cur_hour == '12'):
                    cur_hour = '12'
                    tokens[2] = ("%s:%s"%(cur_hour, cur_minute))
                    del tokens[1]
                elif tokens[1] == '오후':
                    tokens[2] =  ("%s:%s"%(str(int(cur_hour)+12), cur_minute))
                    del tokens[1]
                tokens.insert(1, cur_date)
                # cur_date를 인덱스 1에 저장
                tokens[1] = tokens[1] + " " + tokens[2]
                del tokens[2]
                kko_parse_result.append(tokens)

    kko_parse_result = pd.DataFrame(kko_parse_result, columns = ["User", "Date", "Message"])
    kko_parse_result.to_csv(data_in_path+'/arskatalkdata.csv', encoding='utf-8-sig', index = False)

    return kko_parse_result

if __name__ == '__main__':
    msg_list = read_kko_msg(data_in_path+'/arstext.txt')
    apply_kko_regex(msg_list)
    data = pd.read_csv(data_in_path+'/arskatalkdata.csv', encoding='utf-8') # csv 파일 읽기
    reply_time = re_time.reply_message_time(data)
    f = open(data_in_path+'/reply_time.txt', 'w')
    f.write(reply_time)
    f.close()



# print(read_kko_msg('C:/Users/user/desktop/KakaoTalk_20201113_1600_22_429_group.txt'))
# 위의 주석 : 파일 읽기
