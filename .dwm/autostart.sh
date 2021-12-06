#!/bin/sh
export PATH=$PATH:~/Scripts

pkill sxhkd
pkill picom
pkill slstatus
pkill pnmixer
pkill nitrogen
pkill nm-applet
pkill xfce4-notifyd
nm-applet &
pgrep -x sxhkd > /dev/null || sxhkd -c ~/.config/sxhkd/sxhkdrcdwm &
light -I
nitrogen --restore &
picom &
slstatus &
pnmixer &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
