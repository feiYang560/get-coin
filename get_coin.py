from locale import *
import requests
from colorama import Fore, Back, Style # 一个python专门用来在控制台、命令行输出彩色文字的模块,Fore是针对字体颜色，Back是针对字体背景颜色，Style是针对字体格式
from bs4 import BeautifulSoup as bs
from prettytable import PrettyTable

setlocale(LC_NUMERIC, 'English_US')
def getCoin():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = 'https://cn.investing.com/crypto/currencies'
    web_data = requests.get(url, headers=header)
    soup = bs(web_data.text, 'lxml')   # #fullColumn > div:nth-child(15) > table > tbody
    sumdata = soup.select('#fullColumn > div > table > tbody')
    #sumdata = soup.select('#table > tbody')  # 得到列表
    #print(web_data.text)
    #print(sumdata)
    pt = PrettyTable()
    pt._set_field_names(('排名 名称 简称 价格(美元) 价格(人民币) 市值 24h成交量 交易份额 24小时涨跌 7日涨跌').split())
    for onedata in sumdata[0].find_all('tr'):
        data = onedata.find_all('td')
        #print(data)
        Rank = data[0].get_text()         # 排名
        Name = data[2].get_text()         # 名称
        Enname = data[3].get_text()       # 英文名
        PriceUSD = data[4].get_text()     # 价格(美元)
        #print(type(PriceUSD))
        PriceCNY = atof(PriceUSD) * 6.7   #价格(人民币) = 将千位分隔符的数字转化为常规数值 * 汇率（先设为6.7）
        #print(PriceCNY)
        MarketPrice = data[5].get_text()  # 市值
        Volumn24h = data[6].get_text()    # 24小时成交量
        TotalVol = data[7].get_text()     # 交易份额
        Change24h = data[8].get_text()    # 24小时涨跌额
        Change7d = data[9].get_text()     # 7日涨跌额
        Change24hColor = Fore.RED + Change24h + Fore.RESET if Change24h.find('-') == -1 else Fore.GREEN + Change24h + Fore.RESET  #设置颜色，跌绿色，涨红色
        Change7dColor = Fore.RED + Change7d + Fore.RESET if Change7d.find('-') == -1 else Fore.GREEN + Change7d + Fore.RESET
        #print(onedata)
        pt.add_row([Rank, Name, Enname, PriceUSD, PriceCNY, MarketPrice, Volumn24h, TotalVol, Change24hColor, Change7dColor])
    print('以下数据来自英为财情：(https://cn.investing.com/crypto/currencies)')
    print(pt)

if __name__ == '__main__':
    getCoin()