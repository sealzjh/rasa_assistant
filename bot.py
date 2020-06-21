# -*- coding: utf-8 -*-
import time

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionReportWeather(Action):
    def name(self):
        return "action_report"

    def run(self, dispatcher, tracker, domain):
        # 可以做一些事情
        message = "自定义内容"

        return [SlotSet('matches', message)]


class ActionBusTime(Action):
    def name(self):
        return "action_bus_time"

    def run(self, dispatcher, tracker, domain):
        bus_times = ['8:10', '8:20', '8:30', '8:35', '8:40', '8:45',
                    '8:47', '8:50', '8:55', '9:00', '9:05', '9:10',
                    '9:15', '9:20', '9:25', '9:30', '9:35', '9:40',
                    '9:45','9:50','9:55',
                    '17:15', '17:30', '17:45', '17:50', '17:55',
                    '18:10', '18:20', '18:45', '18:55', '19:00',
                    '19:05', '19:10', '19:15', '19:30', '19:45',
                    '19:55', '20:10', '20:45', '21:15']

        now_h = int(time.strftime("%H"))
        now_m = int(time.strftime("%M"))
        message = "现在时间是%s:%s, " % (now_h, now_m)
        if now_h == 9 and now_m > 55 and now_h <= 12:
            message += '早上已经没有班车了.'
            return [SlotSet('bus_time_text', message)]
        if now_h >= 10 and now_h <= 12:
            message += '早上已经没有班车了'
            return [SlotSet('bus_time_text', message)]
        if now_h == 21 and now_m > 15:
            message += '晚上已经没有班车了, 21点之后下班企业微信里面可以打车哦'
            return [SlotSet('bus_time_text', message)]
        if now_h > 21:
            message += '晚上已经没有班车了, 21点之后下班企业微信里面可以打车哦'
            return [SlotSet('bus_time_text', message)]
        for item in bus_times:
            h, m = item.split(':')
            if int(h) == now_h and int(m) >= now_m:
                message += '下一班车将在%s:%s出发' % (h, m)
                return [SlotSet('bus_time_text', message)]
            if int(h) > now_h:
                message += '下一班车将在%s:%s出发' % (h, m)
                return [SlotSet('bus_time_text', message)]
