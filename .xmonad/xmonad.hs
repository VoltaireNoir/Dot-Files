import XMonad
import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.DynamicLog
import XMonad.Config.Desktop

import XMonad.Util.EZConfig
import XMonad.Util.Ungrab
import XMonad.Util.SpawnOnce

import XMonad.Layout.ThreeColumns
import XMonad.Layout.NoBorders

main :: IO ()
main = xmonad . ewmh =<< xmobar myConfig

myLayout = tiled ||| Mirror tiled ||| threeCol ||| Full
  where
    threeCol = ThreeCol nmaster delta ratio
    tiled   =  Tall nmaster delta ratio
    nmaster = 1      -- Default number of windows in the master pane
    ratio   = 1/2    -- Default proportion of screen occupied by master pane
    delta   = 3/100  -- Percent of screen to increment by when resizing panes


myConfig = def -- Main Config 
    { handleEventHook = fullscreenEventHook
    , modMask = mod4Mask  -- Rebind Mod to the Super key
    , terminal = "kitty"
    , layoutHook = smartBorders $ myLayout
    , startupHook = startup
    , borderWidth = 1
    }
  `additionalKeysP` -- Key bindings
    [ ("M-<Delete>", spawn "slock")
    , ("M-]"  , spawn "firefox")
    , ("M-p", spawn "rofi -show drun")
    , ("M-<F5>", spawn "brightnessctl s 5%-")
    , ("M-<F6>", spawn "brightnessctl s +5%")
    , ("M-<F1>", spawn "pulseaudio-ctl mute")
    , ("M-<F2>", spawn "pulseaudio-ctl down")
    , ("M-<F3>", spawn "pulseaudio-ctl up")
    ]

-- Auto Start Applications
startup :: X ()
startup = do
    spawnOnce "picom"
    spawnOnce "lxsession"
    spawnOnce "nitrogen --restore"
