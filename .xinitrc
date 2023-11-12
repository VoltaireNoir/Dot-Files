#!/bin/sh

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# Default wm
session=${1:-qtile}

case $session in
    dwm		) 	xrandr --dpi 120
              export CHROME_EXECUTABLE=/usr/bin/google-chrome-stable
	    		    exec dwm;;
    bspwm       )	exec bspwm;;
    qtile       )   xrandr --dpi 120
                    exec qtile start;;
    leftwm      )   exec dbus-launch leftwm;;
    xmonad      )   exec xmonad;;
    # No known session, try to run it as command
    *                 ) exec $1;;
esac

