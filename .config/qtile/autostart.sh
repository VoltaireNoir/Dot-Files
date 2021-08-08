#!/bin/sh
picom --experimental-backends --use-ewmh-active-win &
lxsession &
nitrogen --restore &
