# Pythonの公式イメージをベースに使用
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# 必要なPythonパッケージをインストール
RUN pip install opencv-python-headless numpy
