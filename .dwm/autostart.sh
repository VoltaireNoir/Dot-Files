#!/bin/sh
export PATH=$PATH:~/Scripts

pkill sxhkd
pkill picom
pkill slstatus
pkill pnmixer
pkill nitrogen
pkill nm-applet
# pkill lxqt-policykit-agent
pkill dunst
pkill polkit-gnome-au
# lxqt-policykit-agent &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
nm-applet &
pgrep -x sxhkd > /dev/null || sxhkd -c ~/.config/sxhkd/sxhkdrcdwm &
light -I
nitrogen --restore &
picom &
slstatus &
pnmixer &
dunst &
