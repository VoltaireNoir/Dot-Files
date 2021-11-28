#!/bin/sh
lxsession &
nitrogen --restore &
picom &
sleep 0.1
polybar mainbarqt -r & disown
