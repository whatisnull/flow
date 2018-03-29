# flow
version == 1.0
灰度发布、小流量、AB TEST、流量分发等控制。

主要依赖 tornado/redis/sqlite

主要实现看逻辑。

部署方式如下：
      1.  git clone .....
      2.  cd ... 
      3.  export PYTHONPATH=`pwd`
      4.  supervisord -c bin/xxx.conf (注意，配置文件的部署路径与其他配置参数)
      5.  curl http:xxx:xxx/init?status=yes 初始化数据库，主要采用sqlite
      6.  curl http:xxx:xxx/admin 进行管理
      7.  多起几个tornado实例（端口不同，路径不同）进行测试
      8.  根据自己的需要改吧。
      9.   有什么不明白的，留言或者发邮件 458219939@qq.com
      
      
后续。。。。。。
