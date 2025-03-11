SHELL=/bin/bash
.SHELLFLAGS := -eu -o pipefail -c

# サーバー起動
.PHONY: run
run:
	@uvicorn src.main:app --reload

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
	$(call run_command, ruff check)

.PHONY: fix
fix:
	$(call run_command, ruff check --fix)

.PHONY: format
format:
	$(call run_command, ruff format)

.PHONY: todo
todo:
	@uvicorn src.todo:app --reload

.PHONY: chat
chat:
	@uvicorn src.chat:app --reload

# 推奨拡張機能の一括インストール
.PHONY: ext
ext:
	./install_extentions.sh

.PHONY: log
log:
	docker compose logs -f

.PHONY: run_command
# 仮想環境を使用する場合と使用しない場合でPathを変更する
define run_command
if [ "${PIPENV_VENV_IN_PROJECT}" != "false" ] && [  "${PIPENV_ACTIVE}" != 1 ]; then \
    pipenv run $1 ; \
else \
    $1 ; \
fi
endef
