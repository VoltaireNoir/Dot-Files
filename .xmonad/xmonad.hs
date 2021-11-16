import XMonad

import XMonad.Util.EZConfig
import XMonad.Util.Ungrab
import XMonad.Hooks.InsertPosition
import XMonad.Actions.DwmPromote
import XMonad.Hooks.EwmhDesktops
import XMonad.Layout.NoBorders


main :: IO ()
main = xmonad $ ewmhFullscreen $ ewmh $ myConfig

myConfig = def
	{ modMask = mod4Mask
	, terminal = "kitty"
	, manageHook = insertPosition Below Newer
        , layoutHook = myLayout
	}
  `additionalKeysP`
    [ ("M-S-z", spawn "slock")
    , ("M-]"  , spawn "firefox")
    , ("M-w" , kill)
    , ("M-<Return>" , spawn "kitty")
    , ("M-S-<Return>" , dwmpromote)
    ]
   `removeKeysP` 
    [ ("M-S-c")
    ]

myLayout = smartBorders tiled ||| smartBorders mtiled ||| smartBorders Full
  where
    tiled   = Tall nmaster delta ratio
    nmaster = 1      -- Default number of windows in the master pane
    ratio   = 1/2    -- Default proportion of screen occupied by master pane
    delta   = 3/100  -- Percent of screen to increment by when resizing panes
    mtiled  = Mirror tiled
 
