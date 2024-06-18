# テスト　&カバレッジ(XML)　VSCode上で可視化できる。
.PHONY: test
cov:
	pytest src -n auto --cov=./ --cov-config=.coveragerc --cov-report=term-missing --cov-report=xml

# コンテナの削除(ローカルでのみ)
.PHONY: delete
delete:
	docker-compose down --rmi all --volumes --remove-orphans

# 推奨拡張機能の一括インストール
.PHONY: ext
ext:
	./install_extentions.sh
