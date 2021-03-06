import datetime
from com.join.quant.juejin.process_xsz import xiaoshizhi
from gmsdk.api import StrategyBase
import numpy as np
import pandas as pd
from _operator import index
import logging as log

class Mystrategy(StrategyBase):
    global xiaoshizhi
    def __init__(self, *args, **kwargs):
        super(Mystrategy, self).__init__(*args, **kwargs)
        self.xiaoshizhi=xiaoshizhi(self)
        self.xiaoshizhi.initialize()
        #self.xiaoshizhi.before_trading_start();
    def on_login(self):
        print('登录')
        pass

    def on_error(self, code, msg):
        pass

    def on_tick(self, tick):
        print('on_tick')
    def on_bar(self, bar):
        strBarDate= datetime.datetime.fromtimestamp(bar.utc_time);
        startDate=strBarDate.strftime('%Y-%m-%d %H:%M:%S')
        self.xiaoshizhi.handle_data(bar,startDate)
    def on_execrpt(self, res):
        pass

    def on_order_status(self, order):
        pass

    def on_order_new(self, res):
        print('on_order_new')
        pass

    def on_order_filled(self, res):
        pass

    def on_order_partiall_filled(self, res):
        pass
    def on_order_stop_executed(self, res):
        pass

    def on_order_canceled(self, res):
        pass

    def on_order_cancel_rejected(self, res):
        pass

    def on_backtest_finish(self,indicator):
        print('on_backtest_finish')

if __name__ == '__main__':
    myStrategy = Mystrategy(config_file='xsz_backtest.ini', config_file_encoding='UTF-8')
    ret = myStrategy.run()
    print('exit code: ')