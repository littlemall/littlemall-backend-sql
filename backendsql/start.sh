#!/bin/bash

ps -aux | grep python|xargs kill -9

nohup python3.7 manage.py runserver 0:7106