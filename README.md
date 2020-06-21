# install
* mkvirtualenv rasa
* pip install -r requirements_mitie.txt

# 训练: 意图+对话模式
* sh bin/train.sh

# 启动core
* sh bin/run_core.sh

# 提交自定义Action
* sh bin/bot.sh

# 启动nlu
* sh bin/run_nlu.sh

## 启动界面webchat
* cd webchat
* python -m SimpleHTTPServer

## 访问
* http://localhost:8000
