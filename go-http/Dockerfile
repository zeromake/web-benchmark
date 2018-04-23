FROM alpine:3.7

# 更换到阿里云
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

# 设置时区语言
ENV TZ Asia/Shanghai

RUN mkdir /data/
WORKDIR /data/

RUN apk add --no-cache gcc g++ make go

COPY main.go /data/

RUN go build main.go

CMD ["./main"]
