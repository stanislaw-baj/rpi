#!/bin/bash

ssh pi@192.168.0.101 'cd ~/rpi && kill $(ps aux | grep \'python read_test.py\' | awk \'{print $2}\'); git pull; && nohup python read_test.py > read_log.log &' &

