# srcNotice
平时微信公众号太多消息，难免会错过一些src活动的推送，这个工具通过爬虫的方式监控60家企业微信公告的更新，并推送至企业微信统一观看，因为teamssix师傅说不想维护了，我觉得有用处故在此更新维护脚本

# 介绍
✔ 对2022年发布的活动通知进行红色高亮显示

✔ 填写Server酱key后可运行结果可推送至企业微信统一管理

✔ 支持的SRC平台【当前共计60家】,较之前多更了33家SRC，修了一些bug，优化了一下脚本

# 安装与使用
git clone https://github.com/0dinary/srcNotice.git

cd srcNotice

pip3 install -r requirements.txt

python3 srcNotice.py 运行脚本根据提示走

# 推送至企业微信
https://sct.ftqq.com/log server酱根据喜好填好通道配置，点击发送测试，手机微信有消息就算成功了

# 有云服务器的可通过计划任务定期执行脚本实现监控
在云服务器上安装好脚本和环境，参考上边安装与使用

1、输入crontab -e

2、输入数字选择喜欢的编辑器，没有就不用管

3、输入python3 脚本路径 即可

