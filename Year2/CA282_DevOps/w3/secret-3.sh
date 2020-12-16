#!/bin/sh
#da39a3ee5e6b4b0d3255bfef95601890afd80709  -

git init
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
mkdir files
mv runner.zsh files
git add .
git commit -m "added runners"

