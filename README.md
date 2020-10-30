# zjnudk
浙江师范大学战疫通每日打卡脚本
<br>需要自行抓包，得到自己的cookie
<br>然后修改脚本，放到vps上设定定时任务
<br>crontab -e
```
20 0 * * * python /root/autosubmit.py >> /root/autosubmit.py.log 2>&1
```
<br>原始脚本 https://github.com/hwlanxiaojun/DailyHealth_autoCheck
