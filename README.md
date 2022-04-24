# nonebot-plugin-readme
一个nonebot2的readme插件  
暂未完成  
推荐搭配manager插件  
使用 readme [插件名称] 的方式阅读文档  
~~其实我不想上传因为写得太烂了（我是菜逼😭）  
上传上来其实是想等大佬看到代码大手一挥重写~~  

# 关于
### 初始化（任选方法）
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
#### bot管理员
@机器人 readme update	——更新plugin.json  
@机器人 readme upgrade	——更新readme文档  
#### 高级
##### 自定义机器人文档
在readme文件夹中添加文件  
nonebot_plugin_readme  
└── readme  
修改readme，则指令`@机器人readme`将指向此readme，可自定义机器人文档  
##### 自定义下载文档
*建议禁用readme update*  
修改plugin.json与rule.json,配置插件  
```
"module_name": "plugin_name"
"homepage": "https://github.com/name/plugin_name"
```

并确保下载url指向正确的https://cdn.jsdelivr.net/gh/name/plugin_name/README.md  
可以下载github上的非商店插件文档  
rules.json用于配置github->cdn.jsdelivr.net规则，删除README.md，  
将插件名字写入rules.json中列表的最后一个，可以禁用插件文档更新  
（"nonebot_plugin_strman"为没有插件文档的插件，因此会返回空url）  
详阅源码  
#### 用户
`@机器人readme [插件名称]`

### 有什么用
~~方便像我这种插件喜加一爱好者浏览插件README（老百嫖怪了）~~  
方便在目前插件帮助功能不完善时用户查看功能  
~~其实就是没有什么卵用~~  

### 代办
长信息限制  （无法发送较长的文档）
根据用户配置的readme_path,下载插件到机器人data文件夹  
使用其他参数查看plugin.json附带的插件信息  
### bug反馈
~~（似乎有时@机器人 不灵，等会再试就好了）~~
提交issue
