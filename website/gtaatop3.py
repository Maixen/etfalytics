from requests_html import HTMLSession

class ETF:
    def __init__(self, name, url, query, average, one, three, six, twelf):
        self.name = name
        self.url = url
        self.query = query
        self.average = average
        self.one = one
        self.three = three
        self.six = six
        self.twelf = twelf

VALUES = [
    ETF('Xetra Gold', 'https://www.justetf.com/de/etf-profile.html?isin=DE000A0S9GB0&from=search#chart', '/html/body/div[1]/div[3]/div[3]/div[17]/div[4]/div[1]/div/div/table/tbody', 'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Amundi Global Prime', 'https://www.justetf.com/de/etf-profile.html?query=S%26P++500&isin=LU2089238203&from=search#rendite', '/html/body/div[1]/div[3]/div[3]/div[18]/div[4]/div[1]/div/div/table/tbody', 'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Amundi Prime Emerging Markets', 'https://www.justetf.com/de/etf-profile.html?query=Lyxor++Core++US&groupField=index&from=search&isin=LU2300295123#rendite', '/html/body/div[1]/div[3]/div[3]/div[18]/div[4]/div[1]/div/div/table/tbody', 'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Lyxor Core STOXX Europe 600', 'https://www.justetf.com/de/etf-profile.html?query=Lyxor++Core++US&groupField=index&from=search&isin=LU0908500753#rendite', '/html/body/div[1]/div[3]/div[3]/div[18]/div[4]/div[1]/div/div/table/tbody', 'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Xtrackers Bloomberg Commodity Swap', 'https://www.justetf.com/de/etf-profile.html?query=Lyxor++Core++US&groupField=index&from=search&isin=LU2278080713#rendite', '/html/body/div[1]/div[3]/div[3]/div[17]/div[4]/div[1]/div/div/table/tbody', 'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('VanEck Bitcoin', 'https://www.justetf.com/de/etf-profile.html?isin=DE000A28M8D0&from=search', '/html/body/div[1]/div[3]/div[3]/div[17]/div[4]/div[1]/div/div/table/tbody', 'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Lyxor Core US Equity', 'https://www.justetf.com/de/etf-profile.html?isin=LU1781540957&from=search#uebersicht', '/html/body/div[1]/div[3]/div[3]/div[18]/div[5]/div[1]/div/div/table/tbody', 'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('XTrackers S&P 500 2x', 'https://www.justetf.com/de/etf-profile.html?isin=LU0411078552&from=search', '/html/body/div[1]/div[3]/div[3]/div[17]/div[4]/div[1]/div/div/table/tbody', 'Errro', 'Errro', 'Errro', 'Errro', 'Errro')
]

s = HTMLSession()

def getDataAndPrintOut(data):
    _r = s.get(data.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})

    try:
        _1month = float((_r.html.xpath(f'{data.query}/tr[2]/td[2]', first=True).text)[:-1].replace(',', '.'))
        _3months = float((_r.html.xpath(f'{data.query}/tr[3]/td[2]', first=True).text)[:-1].replace(',', '.'))
        _6months = float((_r.html.xpath(f'{data.query}/tr[4]/td[2]', first=True).text)[:-1].replace(',', '.'))
        _12months = float((_r.html.xpath(f'{data.query}/tr[5]/td[2]', first=True).text)[:-1].replace(',', '.'))

        _average = (float(_1month) + float(_3months) + float(_6months) + float(_12months)) / 4

        data.average = _average
        data.one = _1month
        data.three = _3months
        data.six = _6months
        data.twelf = _12months

    except:

        data.name = 'ERROR: E404'

def getGtaatop3():
    for data in VALUES:
        getDataAndPrintOut(data)

    VALUES.sort(key=lambda x: x.average, reverse=True)

    return VALUES