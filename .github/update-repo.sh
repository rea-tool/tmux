#!/bin/bash
status_log=$(git status -sb)
# 这里使用的是 main 分支，根据需求自行修改
if [ "$status_log" == "## main...origin/main" ];then
  echo -e "\033[42;30m nothing to commit, working tree clean \033[0m"
else
  git status -s && git pull origin main && git add -A && git commit -m "update" && git push origin main
fi