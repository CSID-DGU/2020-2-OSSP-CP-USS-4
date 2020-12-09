from flask import Flask
import pandas
import time
import re
import pandas as pd
import datetime as dt

app = Flask(__name__)

@app.route('/')
def index():
    f = open("새파일.txt", 'w')
    f.close()
    return 'txt 파일 생성'

if __name__ == '__main__':
    app.run(debug=True)
