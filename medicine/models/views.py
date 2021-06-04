#https://honeyteacs.tistory.com/6
import os
import pickle
import numpy as np
import pandas as pd
from django.shortcuts import render
from sklearn.neighbors import KNeighborsClassifier
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from keras.preprocessing import sequence
from keras.utils import np_utils
from tensorflow.keras.preprocessing.text import Tokenizer
from urllib.request import urlopen
import json
import pymysql
from django.db import connection
# Create your views here.

def knn_model(request):
    print(request.method == "POST")
    print(request["POST"])

    sample= ""
    # MySQL Connection 연결
    conn = pymysql.connect(host='localhost',
                           user='root', password='1234', db='mydb', charset='utf8')
    # Connection으로부터 Cursor 생성
    curs = conn.cursor()
    # SQL문 실행
    sql = 'select effective_ingredient from korean_data where Type = "{}";'.format('감기약')
    curs.execute(sql)
    # 데이터 Fetch
    korean_rows = curs.fetchall()
    sql = 'select effective_ingredient from foreign_data;'
    curs.execute(sql)
    # 데이터 Fetch
    foreign_rows = curs.fetchall()
    sql = 'name from foreign_data;'
    curs.execute(sql)
    # 데이터 Fetch
    foreign_names = curs.fetchall()
    conn.close()

    df = pd.read_excel('/content/gdrive/MyDrive/소프트웨어공학/result_fe8.xlsx', engine='openpyxl')
    # print(df['효능효과'],df['약 종류'])

    import nltk
    nltk.download('averaged_perceptron_tagger')
    # nltk.download('punkt')

    x_train = []
    x_test = []
    for i in korean_rows:
        if i != None:
            x_test.append(nltk.tokenize.word_tokenize(i))

    for _ in foreign_rows:
        x_train.append(nltk.tokenize.word_tokenize(_))
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(x_train + x_test)

    threshold = 3
    total_cnt = len(tokenizer.word_index)  # 단어의 수
    rare_cnt = 0  # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
    total_freq = 0  # 훈련 데이터의 전체 단어 빈도수 총 합
    rare_freq = 0  # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

    # 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
    for key, value in tokenizer.word_counts.items():
        total_freq = total_freq + value

        # 단어의 등장 빈도수가 threshold보다 작으면
        if (value < threshold):
            rare_cnt = rare_cnt + 1
            rare_freq = rare_freq + value

    def tokenize(samples):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(samples)
        return tokenizer

    r_src_tokenizer = tokenize(x_train + x_test)
    x_test = r_src_tokenizer.texts_to_sequences(x_test)
    x_train = r_src_tokenizer.texts_to_sequences(x_train)
    d = {}
    w = set(foreign_names)
    # print(w)
    # print(len(w))
    count = 0
    for _ in w:
        d[_] = count
        count += 1
    y_train = np.array([d[i] for i in foreign_names])
    x_train = sequence.pad_sequences(x_train, maxlen=50)
    y_train = np_utils.to_categorical(y_train)

    from sklearn.neighbors import KNeighborsClassifier

    ml = KNeighborsClassifier(n_neighbors=1, p=2, metric='minkowski')
    ml.fit(x_train, y_train)
    # x_test = sequence.pad_sequences(x_test, maxlen=50)
    # temp = list(ml.predict(sample)[0]).index(1)
    # print(list(w)[temp])

#정보 sql