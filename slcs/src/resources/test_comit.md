#### Docker部署容器与主机时间不一致问题
- 使用docker容器部署的应用，会出现时间与主机不一致的情况。
- 有两种情况：
  - 一是容器内时间与主机时间不一致，
  - 二是容器与主机时间不一致，差距为8小时；

简单解决问题方案：
#### 容器时间与主机差8个小时:主机的与容器的/etc/localtime不-致。
- 解决方法：创建容器的时候指定启动参数，自动挂载localtime文件到容器内；
```
docker run --name api-groups -v /etc/localtime:/etc/localtime:ro -v /usr/local/docker/unnet-log/api-log/:/unnet-log/oneclick/ -d -p 9080:9080 api-groups:1.0
```

#### 如果容器里面运行的是Java程序，Java代码获取的时间还是会有8个小时的差别，主要原因是Java获取时间是从/etc/timezone里获取时区的。
- 解决方法:挂载主机的/etc/timezone到容器,如果没有则新建echo "Asia/shanghai" > /etc/timezone或者是通过Jvm参数-Duser.timezone=GMT+08将时区信息传进Jvm里，Docker运行容器时添加启动参数：`-e JAVA_OPTS='-Duser.timezone=GMT+08'`，完整命令可以参考：

```
docker run --name mgmt  \
 -e JAVA_OPTS='-Duser.timezone=GMT+08' \
 -v /etc/localtime:/etc/localtime:ro \
 -v /usr/local/docker/unnet-log/:/usr/local/tomcat/logs \
 -d -p 8090:8080 images-name
```
