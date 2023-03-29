#! /bin/bash
pip4 install -r requirements.txt
python3.7 run.py
git add .
git commit -m "执行一次"
git push origin master
