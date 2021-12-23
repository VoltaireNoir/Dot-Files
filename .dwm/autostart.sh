#!/bin/sh
export PATH=$PATH:~/Scripts

pkill sxhkd
pkill picom
pkill slstatus
pkill pnmixer
#pkill nitrogen
pkill nm-applet
pkill dunst
pkill polkit-gnome-au
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
nm-applet &
pgrep -x sxhkd > /dev/null || sxhkd -c ~/.config/sxhkd/sxhkdrcdwm &
light -I
~/.fehbg &
picom &
slstatus &
pnmixer &
dunst &
