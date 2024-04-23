#!/bin/bash

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
~/.fehbg &
picom --config ~/.config/picom/spectr.conf &
dunst &
sxhkd -c ~/.config/sxhkd/sxhkdrcspectr &
