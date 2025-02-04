# what is this repository

[![CI](https://github.com/tomo1227/htmx_book_app/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/tomo1227/htmx_book_app/actions/workflows/ci.yml)

htmxの本で使用するSample Application

# Usage

## Setup

以下のどれかの環境で実行できます。

* Dev-Containerでコンテナを起動
* Docker Composeでコンテナを起動
* ローカルで実行 : Pythonの環境が必要です

## htmxのチュートリアル

htmxの本のチュートリアルです。

```sh
make run
```

Or

```sh
@uvicorn src.main:app --reload
```

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
