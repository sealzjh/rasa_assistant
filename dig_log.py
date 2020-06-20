# -*- coding: utf-8 -*-
import json
import re
import time


class DigLog(object):

    def load_data(self, file, num=0):
        texts = list()
        with open(file, "r") as f:
            lines = f.readlines()
            for no, line in enumerate(lines, 1):

                line = re.compile(r'\n').sub("", line)
                texts.append(line)

                if num > 0 and no >= num:
                    break

        return texts

    def analyse_log(self, logs):
        rs = list()
        for log in logs:
            log_dict = json.loads(log)
            rs.append({'input_word': log_dict['user_input']['text'],
                       'intent_confidence': log_dict['user_input']['intent']['confidence'],
                       'intent_name': log_dict['user_input']['intent']['name'],
                       'log_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(log_dict['log_time'])))
                       })

        return rs

    def print_log(self, logs):
        for item in logs:
            print item['log_time'], item['input_word'], item['intent_name'], item['intent_confidence']

    def group_log(self, logs):
        groups = dict()
        for item in logs:
            if item['input_word'] not in groups:
                groups[item['input_word']] = {
                    'input_word': item['input_word'],
                    'count': 0,
                    'intent_name': item['intent_name'],
                    'intent_confidence': item['intent_confidence']
                }

            groups[item['input_word']]['count'] += 1

        for key in groups:
            item = groups[key]
            print item['input_word'], item['count'], item['intent_name'], item['intent_confidence']

    def run(self, log_file):
        logs = self.load_data(log_file)
        analyse_logs = self.analyse_log(logs)
        self.print_log(analyse_logs)


if __name__ == "__main__":
    log_file = "logs/rasa_nlu_log-20190211-174836-87666.log"
    DigLog().run(log_file)
