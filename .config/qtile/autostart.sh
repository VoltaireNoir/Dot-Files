#!/usr/bin/sh
export PATH=$PATH:~/Scripts

~/.fehbg &
picom &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &
