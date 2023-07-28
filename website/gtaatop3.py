from requests_html import HTMLSession

class ETF:
    def __init__(self, name, url, img_url, query, average, one, three, six, twelf):
        self.name = name
        self.url = url
        self.img_url = img_url
        self.query = query
        self.average = average
        self.one = one
        self.three = three
        self.six = six
        self.twelf = twelf

VALUES = [
    ETF('Xetra Gold', 
        'https://www.justetf.com/de/etf-profile.html?isin=DE000A0S9GB0&from=search#chart', 
        'https://charts.comdirect.de/charts/rebrush/design_big.chart?AVG1=200&AVGTYPE=simple&AXIS_SCALE=lin&DATA_SCALE=abs&HEIGHT=655&IND0=VOLUME&LCOLORS=5F696E&LNOTATIONS=46672186&SHOWHL=1&TIME_SPAN=1Y&TO=1690551585&TYPE=MOUNTAIN&WIDTH=645&WITH_EARNINGS=1',
        '/html/body/div[1]/div[3]/div[3]/div[17]/div[4]/div[1]/div/div/table/tbody', 
        'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Amundi Global Prime', 
        'https://www.justetf.com/de/etf-profile.html?query=S%26P++500&isin=LU2089238203&from=search#rendite', 
        'https://charts.comdirect.de/charts/rebrush/design_big.chart?AVG1=200&AVGTYPE=simple&AXIS_SCALE=lin&DATA_SCALE=abs&HCMASK=3&HEIGHT=655&IND0=VOLUME&LCOLORS=5F696E&LNOTATIONS=284305027&SHOWHL=1&TIME_SPAN=1Y&TO=1689883326&TYPE=MOUNTAIN&WIDTH=645&WITH_EARNINGS=0',
        '/html/body/div[1]/div[3]/div[3]/div[18]/div[4]/div[1]/div/div/table/tbody', 
        'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Amundi Prime Emerging Markets', 
        'https://www.justetf.com/de/etf-profile.html?query=Lyxor++Core++US&groupField=index&from=search&isin=LU2300295123#rendite',
        'https://charts.comdirect.de/charts/rebrush/design_big.chart?AVG1=200&AVGTYPE=simple&AXIS_SCALE=lin&DATA_SCALE=abs&HCMASK=3&HEIGHT=655&IND0=VOLUME&LCOLORS=5F696E&LNOTATIONS=356145503&SHOWHL=1&TIME_SPAN=1Y&TO=1690488128&TYPE=MOUNTAIN&WIDTH=645&WITH_EARNINGS=0',
        '/html/body/div[1]/div[3]/div[3]/div[18]/div[4]/div[1]/div/div/table/tbody', 
        'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Lyxor Core STOXX Europe 600', 
        'https://www.justetf.com/de/etf-profile.html?query=Lyxor++Core++US&groupField=index&from=search&isin=LU0908500753#rendite',
        'https://charts.comdirect.de/charts/rebrush/design_big.chart?AVG1=200&AVGTYPE=simple&AXIS_SCALE=lin&DATA_SCALE=abs&HCMASK=3&HEIGHT=655&IND0=VOLUME&LCOLORS=5F696E&LNOTATIONS=208341222&SHOWHL=1&TIME_SPAN=1Y&TO=1690560898&TYPE=MOUNTAIN&WIDTH=645&WITH_EARNINGS=0',
        '/html/body/div[1]/div[3]/div[3]/div[18]/div[4]/div[1]/div/div/table/tbody', 
        'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Xtrackers Bloomberg Commodity Swap', 
        'https://www.justetf.com/de/etf-profile.html?query=Lyxor++Core++US&groupField=index&from=search&isin=LU2278080713#rendite',
        'https://cdn.pixabay.com/photo/2017/02/12/21/29/false-2061131_1280.png',
        '/html/body/div[1]/div[3]/div[3]/div[17]/div[4]/div[1]/div/div/table/tbody', 
        'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('VanEck Bitcoin', 
        'https://www.justetf.com/de/etf-profile.html?isin=DE000A28M8D0&from=search',
        'https://charts.comdirect.de/charts/rebrush/design_big.chart?AVG1=200&AVGTYPE=simple&AXIS_SCALE=lin&DATA_SCALE=abs&HEIGHT=655&IND0=VOLUME&LCOLORS=5F696E&LNOTATIONS=315175933&SHOWHL=1&TIME_SPAN=1Y&TO=1690565152&TYPE=MOUNTAIN&WIDTH=645&WITH_EARNINGS=1',
        '/html/body/div[1]/div[3]/div[3]/div[17]/div[4]/div[1]/div/div/table/tbody', 
        'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('Lyxor Core US Equity', 
        'https://www.justetf.com/de/etf-profile.html?isin=LU1781540957&from=search#uebersicht',
        'https://charts.comdirect.de/charts/rebrush/design_big.chart?AVG1=200&AVGTYPE=simple&AXIS_SCALE=lin&DATA_SCALE=abs&HCMASK=3&HEIGHT=655&IND0=VOLUME&LCOLORS=5F696E&LNOTATIONS=306088959&SHOWHL=1&TIME_SPAN=1Y&TO=1690488128&TYPE=MOUNTAIN&WIDTH=645&WITH_EARNINGS=0',
        '/html/body/div[1]/div[3]/div[3]/div[18]/div[5]/div[1]/div/div/table/tbody', 
        'Errro', 'Errro', 'Errro', 'Errro', 'Errro'),
    ETF('XTrackers S&P 500 2x', 
        'https://www.justetf.com/de/etf-profile.html?isin=LU0411078552&from=search',
        'https://charts.comdirect.de/charts/rebrush/design_big.chart?AVG1=200&AVGTYPE=simple&AXIS_SCALE=lin&DATA_SCALE=abs&HCMASK=3&HEIGHT=655&IND0=VOLUME&LCOLORS=5F696E&LNOTATIONS=35603972&SHOWHL=1&TIME_SPAN=1Y&TO=1690558203&TYPE=MOUNTAIN&WIDTH=645&WITH_EARNINGS=0',
        '/html/body/div[1]/div[3]/div[3]/div[17]/div[4]/div[1]/div/div/table/tbody', 
        'Errro', 'Errro', 'Errro', 'Errro', 'Errro')
]

s = HTMLSession()

def getDataAndPrintOut(data):
    _r = s.get(data.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})
    _r2 = s.get(data.img_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})

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