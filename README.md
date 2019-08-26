# **hsup_sserpxe**

hsup_sserpxe 。送推行进改更，态状递快控监

## 1 使用方法

### 1.1 需要python3 与 PHP 环境

### 1.2 clone 到本地

``` url
git clone https://github.com/1dooooo/hsup_sserpxe.git
```

### 1.3 注册申请push key，并绑定微信

详细步骤1.3 注册申请push key，并绑定微信参见  [https://sc.ftqq.com](https://sc.ftqq.com) 进行操作

### 1.4 添加定时任务

``` shell
crontab -e
```

在首行添加

``` 
(*/30 * * * * python3 [yourrootpath]/main.py >> [yourrootpath]/out.log 2>&1)
```



### 1.5 进入add/adduser.html 添加用户信息

### 1.6 进入add/additem.html 添加快递信息



## 2 后期计划

### 2.1 增加错误处理，曾强程序鲁棒性。

### 2.2 封装快递接口，建立代理池进行代理访问，防止接口被封失效。
### 2.3 缩短访问间隔（目前为30分钟）