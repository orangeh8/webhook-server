# 使用官方 Python 3.9 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制代码到容器
COPY app.py .

# 安装 Flask
RUN pip install flask

# 暴露端口
EXPOSE 5000

# 运行应用
CMD ["python", "app.py"]