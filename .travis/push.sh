#!/bin/sh

setup_git() {
  git config --global user.name "MarkWh1te"
  git config --global user.email "iamwh1temark@outlook.com"
}

commit_website_files() {
  git add . 
  git status
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER update README.md"
}

upload_files() {
  git remote add origin https://$GH_TOKEN@github.com/MarkWh1te/leetcode.git
  git push -f origin master 
}

setup_git
commit_website_files
upload_files