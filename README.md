# 浙江师范大学战疫通每日打卡脚本

## 使用方法
<br> 打开战役通网站，进行登录等操作

<br>战役通网站url：http://zyt.zjnu.edu.cn/Login/EIPV4/login.aspx

<br>登录完成后，进入打卡url：http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx

<br>按需选择打卡的选项

<br>完成后，点击上报并使用BurpSuite进行抓包

<br>![Bp](/1.png)

<br>将你的cookie和post内容放到脚本的对应位置

<br>上传脚本python文件到/root路径下并在vps上并设定定时任务

<br>crontab -e
```
20 0 * * * python /root/autosubmit.py >> /root/autosubmit.py.log 2>&1
```

<br>每日打卡完成后，可以查看/root/autosubmit.py.log文件观察日志