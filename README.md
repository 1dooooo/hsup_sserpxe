# **hsup_sserpxe**

hsup_sserpxe 。送推行进改更，态状递快控监

- 添加快递公司识别
- 添加交替查询接口
- 快递公司识别码写入config

## 1 使用方法

### 1.1 需要python3 与 PHP 环境

### 1.2 clone 到本地

``` url
git clone https://github.com/1dooooo/hsup_sserpxe.git
```

### 1.3 注册申请push key，并绑定微信

详细步骤1.3 注册申请push key，并绑定微信参见  [https://sc.ftqq.com](https://sc.ftqq.com) 进行操作

### 1.4 添加定时任务

使用定时任务命令 `crontab` 来进行定时任务的添加.
``` shell
crontab -e  
```

该命令会打开（或由用户选择）一个文本编辑器用于编辑定时任务，在首行添加
``` sh
*/30 * * * * python3 [YOURPATH]/main.py >> [YOURPATH]/out.log 2>&1
# 例如 : 
# */30 * * * * python3 /www/express/main.py >> /www/express/out.log 2>&1
```
其中`[YOURPATH]`替换为项目根目录，`*/30`指代每30分钟执行一次,即30分钟进行一次查询. 这个时间将直接影响推送的延时效性.

### 1.5 进入add/adduser.html 添加用户信息

### 1.6 进入add/additem.html 添加快递信息



## 2 后期计划

### 2.1 增加错误处理，增强程序鲁棒性。 √
### 2.2 封装快递接口，建立代理池进行代理访问，防止接口被封失效。 √
### 2.3 缩短访问间隔（目前为30分钟） 
### 2.4 面向对象
### 2.5 html使用ajax进行请求