FROM alpine:3.7

# 更换到阿里云
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

# 设置时区语言
ENV TZ Asia/Shanghai
ENV PYTHONIOENCODING utf8

COPY requirements.txt /tmp/requirements.txt

RUN apk add --no-cache gcc g++ make python3 py3-pip python3-dev

RUN mkdir -p ~/.pip && echo -e "[global]\ntimeout = 6000\nindex-url = https://pypi.doubanio.com/simple\n\n[install]\nuse-mirrors = true\nmirrors = https://pypi.doubanio.com/simple\ntrusted-host = pypi.doubanio.com" > ~/.pip/pip.conf

RUN mkdir /data/
WORKDIR /data/

COPY app.py /data/

RUN pip3 install -r /tmp/requirements.txt

CMD ["python3", "./app.py"]
