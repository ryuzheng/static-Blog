# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "https://zhengzexin.com/"
source_dir = "../src/"
build_dir = "../dist/"
template = "Galileo"
index_page_size = 10
archives_page_size = 20
fetch_remote_imgs = False
category_by_folder = True
enable_jsdelivr = {"enabled": True, "repo": "ryuzheng/static-Blog@gh-pages"}
valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "ValcujOd8RqQw9PnuSaVkWey-gzGzoHsz",
    "appKey": "xHr7ovH5p80YCEyIi5QMAB9F",
    "visitor": True,
    "recordIP": True,
    "placeholder": "欢迎留言"
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
external_links = [{"name": "< &frasl; > with ❤️", "url": "https://codewith.love", "brief": "Ryu的主页。"}]
nav = [{
    "name": "首页",
    "url": "${site_prefix}",
    "target": "_self"
}, {
    "name": "归档",
    "url": "${site_prefix}archives/",
    "target": "_self"
}, {
    "name": "关于",
    "url": "${site_prefix}About/",
    "target": "_self"
}, {
    "name": "友链",
    "url": "${site_prefix}Friends/",
    "target": "_self"
}]

social_links = [{"name": "GitHub", "url": "https://github.com/ryuzheng", "icon": "gi gi-github"}]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = r'''
<a no-style href="http://www.beian.miit.gov.cn" target="_blank">粤 ICP 备 18056573 号</a>
'''

body_addon = r'''
<script>
    if(window.location.hash){
        var checkExist = setInterval(function() {
           if ($(window.location.hash).length) {
              $('html, body').animate({scrollTop: $(window.location.hash).offset().top-90}, 1000);
              clearInterval(checkExist);
           }
        }, 100);
    }
</script>
<script type="text/javascript">
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-89607299-1" type="text/javascript"></script>
<script type="text/javascript">
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-89607299-1');
</script>
'''
