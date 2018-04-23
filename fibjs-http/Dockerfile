FROM centos:7

# 设置时区语言
ENV TZ Asia/Shanghai

RUN yum install curl sudo -y && curl -s http://fibjs.org/download/installer.sh|sh

RUN mkdir /data/
WORKDIR /data/

COPY main.js /data/

CMD ["fibjs", "./main.js"]
