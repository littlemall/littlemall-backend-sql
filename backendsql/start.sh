#!/bin/bash

ps -aux | grep python|xargs kill -9

nohup python manage.py runserver 0:7106 & -> manage.log