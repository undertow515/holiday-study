import os
import sys
from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus, unquote
import requests
import json
import pandas as pd

class Wamis(object):
    # url: http://www.wamis.go.kr:8080/wamis/openapi/wkw/flw_dubobsif
    
    def __init__(self, key=None, urlcat=None):
        """
        :param key: First, you have to get the api key for the right purposes
        :param url: also you have to set the url link below
        """
        url_dict = {
                    "일기상자료":"http://www.wamis.go.kr:8080/wamis/openapi/wkw/we_dtdata",
                    "일강수량자료":"http://www.wamis.go.kr:8080/wamis/openapi/wkw/rf_dtdata",
                    "일수위자료":"http://www.wamis.go.kr:8080/wamis/openapi/wkw/wl_dtdata",
                    "일유량자료":"http://www.wamis.go.kr:8080/wamis/openapi/wkw/flw_dtdata",
                    "일댐수문정보":"http://www.wamis.go.kr:8080/wamis/openapi/wkd/mn_dtdata"
                    }
        self.key = key
        self.url = url_dict[urlcat]
        self.params = None
        self.df : pd.DataFrame = None

    def set_daily_we(self, startdt,enddt, ids = 1001620):
        """
        obscd	문자	(필수) 관측소코드	
        startdt	문자	관측기간-시작일	YYYYMMDD
        enddt	문자	관측기간-종료일	YYYYMMDD
        output	문자	출력 포멧	- 사용자 선택
        xml, json
        - 기본값
        json
        """
        self.params = "?" + urlencode({quote_plus("obscd"): ids,
                                       quote_plus("startdt"): startdt,
                                       quote_plus("key"): self.key,
                                       quote_plus("output"): "json",
                                       quote_plus("enddt"): enddt,})
        return self.params
    
    def set_daily_rf(self, startdt,enddt, ids = 1001620):
        self.params = "?" + urlencode({quote_plus("obscd"): ids,
                                       quote_plus("startdt"): startdt,
                                       quote_plus("key"): self.key,
                                       quote_plus("output"): "json",
                                       quote_plus("enddt"): enddt,})
        return self.params
    
    def set_daily_wl(self, startdt,enddt, ids = 1001620):
        self.params = "?" + urlencode({quote_plus("obscd"): ids,
                                       quote_plus("startdt"): startdt,
                                       quote_plus("key"): self.key,
                                       quote_plus("output"): "json",
                                       quote_plus("enddt"): enddt,})
        return self.params

    def set_daily_flw(self, year, ids = 1001620):
        self.params = "?" + urlencode({quote_plus("obscd"): ids,
                                       quote_plus("year"): year,
                                       quote_plus("key"): self.key,})
        return self.params

    def set_daily_dam(self, startdt, enddt, ids = 1003110):
        self.params = "?" + urlencode({quote_plus("damcd"): ids,
                                        quote_plus("startdt"): startdt,
                                        quote_plus("enddt"): enddt,
                                        quote_plus("key"): self.key,})
        return self.params
    
    def get_df(self):
        req = requests.get(self.url + unquote(self.params))
        result_data = req.json()
        return result_data

