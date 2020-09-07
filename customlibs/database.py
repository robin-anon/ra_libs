import datetime as dt
import pickle
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import yfinance as yf


def dt_obj_to_string(dt_obj):
    year, month, day = dt_obj.year, dt_obj.month, dt_obj.day
    year, month, day = str(year), str(month), str(day)
    if int(day) < 10:
        day = "0" + day
    if int(month) < 10:
        month = "0" + month
    return "-".join((year, month, day))


def dt_string_to_obj(dt_string):
    dt_string = dt_string[:10]
    year, month, day = dt_string.split("-")
    year, month, day = int(year), int(month), int(day)
    return dt.datetime(year, month, day)


def dt_string_to_obj_23_59_59(dt_string):
    dt_string = dt_string[:10]
    year, month, day = dt_string.split("-")
    year, month, day = int(year), int(month), int(day)
    return dt.datetime(year, month, day, hour=23, minute=59, second=59)


def dt_obj_to_string_list(dt_obj_list):
    dt_string_list = []
    for dt_obj in dt_obj_list:
        dt_string_list.append(dt_obj_to_string(dt_obj))
    return dt_string_list


class Database:
    def __init__(self):
        self.start_date_obj = dt.datetime(2000, 1, 1, hour=23, minute=59, second=59)
        self.end_date_obj = dt.datetime(2000, 1, 1, hour=23, minute=59, second=59)
        self.start_date_string = dt_obj_to_string(self.start_date_obj)
        self.end_date_string = dt_obj_to_string(self.end_date_obj)
        self.date_before_obj = self.start_date_obj - dt.timedelta(days=1)
        self.date_after_obj = self.end_date_obj + dt.timedelta(days=1)
        self.date_before_string = dt_obj_to_string(self.date_before_obj)
        self.date_after_string = dt_obj_to_string(self.date_after_obj)
        self.ticker_list = []
        self.data = pd.DataFrame()

    def add_tickers(self, ticker_list):
        new_tickers = [
            ticker for ticker in ticker_list if ticker not in self.ticker_list
        ]
        new_data = []
        for ticker in new_tickers:
            try:
                series = yf.Ticker(ticker).history(
                    start=self.start_date_obj, end=self.end_date_obj, interval="1d"
                )["Close"]
            except:
                series = pd.Series(
                    data=np.nan, index=[self.start_date_obj, self.end_date_obj]
                )
            series.name = ticker
            new_data.append(series)
        for series in new_data:
            self.data[series.name] = series
        self.data = self.data.sort_index(axis=1)
        self.ticker_list += new_tickers
        return

    def add_date(self, dt_string):
        dt_obj = dt_string_to_obj_23_59_59(dt_string)
        new_data = []
        if dt_obj > self.end_date_obj:
            for ticker in self.ticker_list:
                try:
                    series = yf.Ticker(ticker).history(
                        start=self.date_after_obj, end=dt_obj, interval="1d"
                    )["Close"]
                except:
                    series = pd.Series(data=np.nan, index=[self.date_after_obj, dt_obj])
                series.name = ticker
                new_data.append(series)
            new_data = pd.concat(new_data, axis=1, sort=True)
            self.data = pd.concat([self.data, new_data], axis=0, sort=True)
            self.end_date_obj = dt_obj
            self.end_date_string = dt_string
            self.date_after_obj = dt_obj + dt.timedelta(days=1)
            self.date_after_string = dt_obj_to_string(self.date_after_obj)
        elif dt_obj < self.start_date_obj:
            for ticker in self.ticker_list:
                try:
                    series = yf.Ticker(ticker).history(
                        start=dt_obj, end=self.date_before_obj, interval="1d"
                    )["Close"]
                except:
                    series = pd.Series(
                        data=np.nan, index=[dt_obj, self.date_before_obj]
                    )
                series.name = ticker
                new_data.append(series)
            new_data = pd.concat(new_data, axis=1, sort=True)
            self.data = pd.concat([self.data, new_data], axis=0, sort=True)
            self.start_date_obj = dt_obj
            self.start_date_string = dt_obj_to_string(dt_obj)
            self.date_before_obj = dt_obj - dt.timedelta(days=1)
            self.date_before_string = dt_obj_to_string(self.date_before_obj)
        return self.data

    def save_to_csv(self, filename):
        self.data.to_csv(filename, sep="\t")

    def save_to_pickle(self, filename):
        file = open(filename, "wb")
        pickle.dump(self, file)
        file.close()


def read_from_pickle(filename):
    file = open(filename, "rb")
    db = pickle.load(file)
    file.close()
    return db


def read_from_csv(filename):
    db = Database()
    db.data = pd.read_csv(filename, sep="\t", index_col=0)
    db.start_date_string = db.data.index[0]
    db.start_date_obj = dt_string_to_obj_23_59_59(db.start_date_string)
    db.end_date_string = db.data.index[-1]
    db.end_date_obj = dt_string_to_obj_23_59_59(db.end_date_string)
    db.date_before_obj = db.start_date_obj - dt.timedelta(days=1)
    db.date_after_obj = db.end_date_obj + dt.timedelta(days=1)
    db.date_before_string = dt_obj_to_string(db.date_before_obj)
    db.date_after_string = dt_obj_to_string(db.date_after_obj)
    db.ticker_list = list(db.data.columns)
    return db


america_etfs = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
japan_etfs = "https://en.wikipedia.org/wiki/List_of_Japanese_exchange-traded_funds"
hongkong_etfs = "https://en.wikipedia.org/wiki/List_of_Hong_Kong_exchange-traded_funds"
europe_etfs = "https://en.wikipedia.org/wiki/List_of_European_exchange-traded_funds"


def get_etf_list(url):
    page = requests.get(url).content
    soup = BeautifulSoup(page, features="html.parser")
    li_list = []
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li"):
            li_list.append(li.text)
    li_list = [
        li.split("|")[1].split(")")[0] for li in li_list if "|" in li and ")" in li
    ]
    return li_list
