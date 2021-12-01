#!/usr/bin/bash
export PATH=$PATH:~/Scripts

xrandr --dpi 120
pkill sxhkd
pgrep -x sxhkd > /dev/null || sxhkd -c ~/.config/sxhkd/sxhkdrcdwm &
light -I
pkill lxsession
lxsession &
nitrogen --restore &
picom &
pkill slstatus
slstatus &
pkill xfce4-notifyd
/usr/lib/xfce4/notifyd/xfce4-notifyd &
