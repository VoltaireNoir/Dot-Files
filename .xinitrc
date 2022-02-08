#!/bin/sh

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# Here Xfce is kept as default
session=${1:-dwm}

case $session in
    dwm		) 	xrandr --dpi 120
	    		exec dwm;;
    bspwm       )	exec bspwm;;
    xmonad      )	exec xmonad;;
    # No known session, try to run it as command
    *                 ) exec $1;;
esac

