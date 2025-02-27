# 使用官方 Python 3.9 基础镜像
FROM python:3.11-ubi9

# 设置工作目录
WORKDIR /app

# 复制代码到容器
COPY app.py .

# 安装 Flask
RUN pip install flask

USER root

RUN chgrp -R 0 /app && \
	chmod -R g=u /app

USER 10001

# 暴露端口
EXPOSE 8080

# 运行应用
CMD ["python", "app.py"]