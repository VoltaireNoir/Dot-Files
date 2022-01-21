#!/bin/sh
export PATH=$PATH:~/Scripts

pkill sxhkd
pkill picom
pkill slstatus
#pkill nitrogen
#pkill nm-applet
pkill dunst
pkill polkit-gnome-au
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
pgrep -x sxhkd > /dev/null || sxhkd -c ~/.config/sxhkd/sxhkdrcdwm &
~/.fehbg &
picom &
slstatus &
dunst &
#nm-applet &
