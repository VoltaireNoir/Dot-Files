#!/bin/sh

xrandr --dpi 120
lxsession &
light -I
nitrogen --restore &
picom &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
sleep 0.1
polybar mainbarqt -r & disown
