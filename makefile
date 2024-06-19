# サーバー起動
.PHONY: run
run:
	uvicorn src.main:app --reload

# テスト　&カバレッジ(XML)　VSCode上で可視化できる。
.PHONY: test
test:
	pytest tests -n auto --cov=./ --cov-config=.coveragerc --cov-report=term-missing --cov-report=xml

# コンテナの削除(ローカルでのみ)
.PHONY: down
down:
	docker-compose down --rmi all --volumes --remove-orphans

# 推奨拡張機能の一括インストール
.PHONY: ext
ext:
	./install_extentions.sh
