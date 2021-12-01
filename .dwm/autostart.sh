#!/usr/bin/bash
export PATH=$PATH:~/Scripts

xrandr --dpi 115
pgrep -x sxhkd > /dev/null || sxhkd &
light -I
pkill lxsession
lxsession &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
nitrogen --restore &
picom --config ~/.config/picom/picom.conf &
slstatus &
