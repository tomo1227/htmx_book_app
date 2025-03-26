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
