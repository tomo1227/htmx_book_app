# what is this repository

[![CI](https://github.com/tomo1227/htmx_book_app/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/tomo1227/htmx_book_app/actions/workflows/ci.yml)

htmxの本で使用するSample Application

# Usage

## Download

## Setup

以下コマンドでcloneしてください。

```sh
git clone https://github.com/tomo1227/htmx_book_app.git
```

起動は以下3つの方法で実行できます。

1. Dev-Containerでコンテナを起動
2. Docker Composeでコンテナを起動
3. ローカルで実行 (Python 3.13.2、uvのインストールが事前に必要)

### Dev-Container

Dev-Containerで先ほどcloneした`htmx_book_app`を開くと起動されます。

### Docker Compose

以下コマンドをローカルで叩くと起動できます。

```sh
docker compose up -d
```

## htmxのチュートリアル

htmxの本のチュートリアルです。

```sh
make run
```

Or

```sh
uvicorn src.main:app --reload
```

Dev-Container : ローカル環境で http://127.0.0.1:8000/ にアクセスしてください。
Docker Compose : ローカル環境で http://0.0.0.0:8000/ にアクセスしてください。

## ToDo App

シンプルなToDoアプリケーションです。

```sh
make todo
```

Or

```sh
@uvicorn src.todo:app --reload
```

## Chat App

WebSocketを用いたチャットアプリケーションです。

```sh
make chat
```

Or

```sh
@uvicorn src.chat:app --reload
```
