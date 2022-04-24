# nonebot-plugin-readme
一个nonebot2的readme插件  
暂未完成  
推荐搭配manager插件  
使用 readme [插件名称] 的方式阅读文档  
~~其实我不想上传因为写得太烂了（我是菜逼😭）  
上传上来其实是想等大佬看到代码大手一挥重写~~  

# 关于
### 初始化
1. 插件放入 src 文件夹，加载后
```
readme upgrade
```

2. 插件目录下
```
python3 download.py 
python3 readme.py
```
3.下载并解压 data 到插件目录
### 插件目录应当为
.  
├── __init__.py		     —— 机器人插件  
├── data		            —— 数据存储（readme upgrade得到）  
│   └── readme  
│       ├── ELF_RSS2  
│       │   ├── README.md- 原文档  
│       │   └── readme	—— 插件将读取的数据  
│       ├── OlivOS  
|	……  
├── download.py		      —— 爬虫  
├── plugins.json	      —— 商店插件信息（readme update得到）  
├── readme.py		        —— 将markdown转换为文本文档（readme）  
└── rules.json		       —— 将插件github网址转换为下载README使用的规则（详阅download.py） 
### 使用
`readme [插件名称]`

### 有什么用
~~方便像我这种插件喜加一爱好者浏览插件README（老百嫖怪了）~~  
方便在目前插件帮助功能不完善时用户查看功能  
~~其实就是没有什么卵用~~  

### 代办
长信息限制  （无法发送较长的文档）
使用其他参数查看plugin.json附带的插件信息  
### 反馈
提交issue
