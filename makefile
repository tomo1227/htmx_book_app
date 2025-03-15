# サーバー起動
.PHONY: run
run:
	@uvicorn src.main:app --reload --host 0.0.0.0 --port 80

# テスト　&カバレッジ(XML)　VSCode上で可視化できる。
.PHONY: test
test:
	pytest tests -n auto --cov=./ --cov-config=.coveragerc --cov-report=term-missing --cov-report=xml

# コンテナの起動(ローカルでのみ)
.PHONY: up
up:
	docker compose up -d

# コンテナの削除(ローカルでのみ)
.PHONY: down
down:
	docker compose down --rmi all --volumes --remove-orphans

.PHONY: prune
prune:
	docker system prune -a

# 推奨拡張機能の一括インストール
.PHONY: ext
ext:
	./install_extentions.sh

.PHONY: lint
lint:
	ruff check

.PHONY: fix
fix:
	ruff check --fix

.PHONY: format
format:
	ruff format

.PHONY: todo
todo:
	@uvicorn src.todo:app --reload --host 0.0.0.0 --port 80

.PHONY: chat
chat:
	@uvicorn src.chat:app --reload --host 0.0.0.0 --port 80
