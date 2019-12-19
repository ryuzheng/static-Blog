# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/static-Blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
fetch_remote_imgs = True
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "郑泽鑫的博客"
site_logo = "${static_prefix}logo.png"
site_build_date = "2013-07-31T13:07+08:00"
author = "ryuzheng"
email = "ryu@zhengzexin.com"
author_homepage = "https://zhengzexin.com"
description = "一个生信工作者的独立博客"
key_words = ['生物信息学', 'Geek', 'Python', '独立博客']
language = 'zh-CN'
external_links = [
    {
        "name": "\<\/\> with ❤️",
        "url": "https://codewith.love",
        "brief": "Ryu的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/ryuzheng",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
