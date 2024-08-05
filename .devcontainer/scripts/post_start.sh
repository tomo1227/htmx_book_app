#!/usr/bin/bash

if [ -z "$1" ]; then
  echo "Error: No directory provided."
  exit 1
fi

#  ~/.gitconfigをローカルからコピーする
echo "start to copy local ~/.gitconfig"
git config --global --add safe.directory $1

# ~/.gitconfigの設定追加
git config pull.rebase false
git config --global commit.template .commit_template
echo "Success git config."

echo "Install pip & poetry"
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir poetry

poetry config virtualenvs.create false

echo "Install package"
poetry install

. ~/.bashrc
