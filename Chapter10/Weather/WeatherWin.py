#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Time : 2019-3-16 13:18
# @Author : leoyo
# @Email : #
# @File : WeatherWin.py
# @Project : PYQT5_UI
# @IDE : PyCharm

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QThread,pyqtSignal
from Chapter10.Weather.Weather_UI import Ui_Form
import sys,PyQt5.sip,requests,logging,json
from Chapter10.Weather.cityCode import CITYCODE

logging.basicConfig(level=logging.DEBUG,datefmt="%a,%d %b %Y %H:%M:%S",format='%(asctime)s %(levelname)s %(message)s' )
class WeatherWin(QWidget,Ui_Form):
    def __init__(self,parent = None):
        super(WeatherWin,self).__init__(parent)
        self.setupUi(self)
        self.weatherComboBox.addItems( i for i in CITYCODE.keys() )
        logging.debug("初始化成功")

    def queryWeather(self):
        logging.debug("Qthread启动")
        self.weatherThread = weatherThread(city=self.weatherComboBox.currentText())
        self.weatherThread.weather_emit.connect(self.addweather)
        self.weatherThread.start()

    def addweather(self,msg):
        self.resultText.setText(msg)


    def clearWeather(self):
        logging.debug("* ClearResult")
        self.resultText.clear()

class weatherThread(QThread):
    weather_emit = pyqtSignal(str)
    def __init__(self,parent =None,city =None):
        super(weatherThread,self).__init__(parent)
        self.city = city

    def run(self,city=None):
        logging.debug("获取当前城市:%s"%self.city)
        if self.city !='请选择':
            try:
                citycode = CITYCODE[self.city]
                rep = requests.get('http://www.weather.com.cn/data/sk/' + citycode + '.html')
                data = json.loads(rep.content)
                msg1 = '城市：%s'%data['weatherinfo']['city']+'\n'
                msg2 = '温度：%s'%data['weatherinfo']['temp']+'\n'
                msg3 = '风向：%s'%data['weatherinfo']['WD']+'\n'
                msg4 = '风力：%s'%data['weatherinfo']['WS']+'\n'
                msg5 = '湿度：%s'%data['weatherinfo']['SD']+'\n'
                result = msg1+msg2+msg3+msg4+msg5
                logging.debug("Get Weather Result!")
                self.weather_emit.emit(result)
            except Exception as e:
                logging.error(e)
                self.weather_emit.emit( e )
        else:
            self.weather_emit.emit( "请选择城市后进行查询！" )

if __name__ == '__main__':
    app =QApplication(sys.argv)
    weatherwin = WeatherWin()
    weatherwin.show()
    sys.exit(app.exec_())




