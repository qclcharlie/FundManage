odelist = ophq.getcodelist()
for item in odelist:
    # if item['ExchangeID'] in ['SHFE', 'DCE', 'CZCE', 'INE', 'CFFEX']:
    if item['ExchangeID'] in ['CFFEX']:
        if len(item['CodeAlias']) >4 and len(item['CodeAlias']) < 8:

            desktop_path = "C:\\test\\"
            full_path = desktop_path + str(item['CodeID'])  # 也可以创建一个.doc的word文档

            respone = requests.get(
                # "http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=" + item['CodeAlias'])
                "http://stock2.finance.sina.com.cn/futures/api/json.php/CffexFuturesService.getCffexFuturesDailyKLine?symbol="+ item['CodeAlias'])
            dt = json.loads(respone.text)
            if dt == None:
                continue
            print(item['CodeAlias'], item['CodeID'])
            file = open(full_path, 'w')
            for item in dt:
                date = item[0]
                open1 = item[1]
                high = item[2]
                low = item[3]
                close = item[4]
                volume = item[5]
                if(open1 == '0.000' or high == '0.000' or low =='0.000' or close =='0.000' or volume == '0'): continue
                if(date == '2020-03-25'): continue
                if(date == '2020-03-24'): continue
                # print(open1)
                timestamp = date_to_timestamp(date, format_string="%Y-%m-%d")
                timestamp = timestamp * 1000
                msg = '{"Time": ' + str(timestamp) + ',"TimeZone": -11, "OpenPrice":' + str(
                    open1) + ',"HighPrice":' + str(high) + ',"LowPrice":' + str(low) + ',"ClosePrice":' + str(
                    close) + ',"AcceptVol":' + str(volume) + '}' + '\n'
                # msg = '{"Timge": 1516461213,"TimeZone":-11}'+'\n'

                file.write(msg)
            file.close()
