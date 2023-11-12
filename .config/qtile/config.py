# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os, subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Match, Screen, Key, EzKey, KeyChord
from libqtile.lazy import lazy
from omnilayout import OmniLayout

@lazy.function
def float_to_front(qtile) -> None:
    """Bring all floating windows of the group to front"""
    for window in qtile.current_group.windows:
        if window.floating:
            window.cmd_bring_to_front()

mod = "mod4"
terminal = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.next().when(layout = "Omni"), lazy.layout.down().when(layout = "Monad"), desc="Move focus down"),
    Key([mod], "k", lazy.layout.previous().when(layout = "Omni"),  lazy.layout.up().when(layout = "Monad"),desc="Move focus up"),
    Key([mod], "space", lazy.next_layout(), desc="Move window focus to other window"),
    Key([mod, "shift"], "space", lazy.layout.flip(), desc="Move window focus to other window"),

    Key([mod], "bracketright", lazy.screen.next_group(skip_empty=True), desc="Go to the next group"),
    Key([mod], "bracketleft", lazy.screen.prev_group(skip_empty=True), desc="Go to the prev group"),
    Key([mod,"shift"], "bracketright", lazy.screen.next_group(), desc="Go to the next group"),
    Key([mod,"shift"], "bracketleft", lazy.screen.prev_group(), desc="Go to the prev group"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down().when(layout = "Omni"), lazy.layout.shrink().when(layout = "Monad"), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up().when(layout = "Omni"), lazy.layout.grow().when(layout = "Monad"), desc="Grow window up"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "s",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    EzKey("M-b", lazy.hide_show_bar(),desc="Toggle bar"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.layout.down(), desc="Move to the next window"),
    Key([mod,"shift"], "Tab", lazy.screen.next_group(skip_empty=True), desc="Toggle between groups"),
    EzKey("M-C-<Tab>", lazy.screen.toggle_group(), desc = "Toggle groups"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod,"shift"], "w", lazy.spawn("forcekill"), desc="force Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    Key([mod,"shift"], "f", float_to_front, desc="float to front"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Spawn a command using a prompt widget"),
    # Custom
    EzKey("M-s", lazy.window.toggle_floating()),
    EzKey("M-p", lazy.spawn("rofi -show drun")),
    EzKey("M-q", lazy.spawn("powermenu")),
    EzKey("M-S-e", lazy.spawn("kitty --class Neovim nvim")),
    EzKey("M-e", lazy.spawn("kitty --class Helix helix")),
    EzKey("M-a", lazy.spawn("kitty --class Mixer pulsemixer")),
    EzKey("M-C-n", lazy.spawn("kitty --class Network nmtui")),
    # Utilities
    Key([],"XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume +2")),
    Key([],"XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -2")),
    Key([],"XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),
    EzKey("M-S-<equal>", lazy.spawn("pulsemixer --change-volume +2")),
    EzKey("M-S-<minus>", lazy.spawn("pulsemixer --change-volume -2")),
    Key([mod, "control"],"m", lazy.spawn("pulsemixer --toggle-mute")),
    Key([],"XF86MonBrightnessUp", lazy.spawn("blight inc 5 -s")),
    Key([],"XF86MonBrightnessDown", lazy.spawn("blight dec 5 -s")),
    EzKey("M-C-<equal>", lazy.spawn("blight inc 5 -s")),
    EzKey("M-C-<minus>", lazy.spawn("blight dec 5 -s")),
    Key(["control"],"XF86MonBrightnessUp", lazy.spawn("blight inc 100 -s")),
    Key(["control"],"XF86MonBrightnessDown", lazy.spawn("blight dec 100 -s")),
    Key(["shift"],"XF86MonBrightnessUp", lazy.spawn("blight inc")),
    Key(["shift"],"XF86MonBrightnessDown", lazy.spawn("blight dec")),
    # Screenshots
    Key([],"Print", lazy.spawn("screenshot")),
    Key(["mod1"],"Print", lazy.spawn("screenshot copy")),
    Key(["control"],"Print", lazy.spawn("screenshot window")),
    Key(["control","mod1"],"Print", lazy.spawn("screenshot window-copy")),
    Key(["shift"],"Print", lazy.spawn("screenshot select")),
    Key(["shift","mod1"],"Print", lazy.spawn("screenshot select-copy")),
    #Notifications
    EzKey("M-z", lazy.spawn("dunstctl set-paused toggle")),
    EzKey("M-S-z", lazy.spawn("dunstctl history-pop")),
    #Process managers
    EzKey("M-x", lazy.spawn("kitty btm")),
    EzKey("M-S-x", lazy.spawn("kitty bpytop")),
    #Screen lock
    EzKey("M-<Delete>", lazy.spawn("slock")),

    # Key Chords
    KeyChord([mod],"o", [
        EzKey("b",lazy.spawn("firefox")),
        EzKey("m",lazy.spawn("spotify")),
        EzKey("S-m",lazy.spawn("kitty --class Music ncmpcpp")),
        EzKey("f",lazy.spawn("kitty ranger")),
        EzKey("S-f",lazy.spawn("nautilus")),
        EzKey("t", lazy.spawn("telegram-desktop")),
        EzKey("d", lazy.spawn("discord")),
        EzKey("l", lazy.spawn("logseq")),
        EzKey("q", lazy.spawn("qbittorrent")),
        EzKey("w", lazy.spawn("firefoxpwa site launch 01FQTTGK6682KTTBGBV7PD2TX8")),
        EzKey("n", lazy.spawn("standard-notes")),
        EzKey("o", lazy.spawn("obs")),
        EzKey("p", lazy.spawn("fish -c playvideo")),
        EzKey("S-o", lazy.spawn("obsidian")),
    ]),

    #switch to custom groups
    KeyChord([mod], "g", [
        EzKey("s", lazy.screen.toggle_group(group_name="6"), desc="Go to socials group"),
        EzKey("m", lazy.screen.toggle_group(group_name="7"), desc="Go to music group"),
        EzKey("v", lazy.screen.toggle_group(group_name="8"), desc="Go to video group"),
        EzKey("o", lazy.screen.toggle_group(group_name="9"), desc="Go to obs group"),
        EzKey("c", lazy.screen.toggle_group(group_name="10"), desc="Go to code group"),
    ]),

    #normalize
    KeyChord([mod], "n", [
        EzKey("n", lazy.layout.normalize(), desc="Full normalization"),
        EzKey("h", lazy.layout.normalize_height(), desc="Current Column Height normalization"),
        EzKey("w", lazy.layout.normalize_width(), desc="All width normalization"),
    ]),

    #OmniLayout Shortcuts
    EzKey("M-m",lazy.layout.toggle_autotile().when(layout = "Omni"), lazy.layout.maximize().when(layout = "Monad")),
    EzKey("M-S-m",lazy.layout.toggle_automove()),
    EzKey("M-S-a",lazy.layout.reset()),
    EzKey("M-A-j",lazy.layout.swap_down()),
    EzKey("M-A-k",lazy.layout.swap_up()),
    EzKey("M-A-l",lazy.layout.swap_right()),
    EzKey("M-A-h",lazy.layout.swap_left()),
    EzKey("M-S-<Return>",lazy.layout.swap_to_largest().when(layout = "Omni"), lazy.layout.swap_main().when(layout = "Monad")),
    EzKey("M-<minus>",lazy.layout.dec_maxstack()),
    EzKey("M-<equal>",lazy.layout.inc_maxstack()),
]

group_names = {
    "1":"I",
    "2":"II",
    "3":"III",
    "4":"IV",
    "5":"V",
    "6":"",
    "7":"",
    "8":"󰿎 ",
    "9":"",
    "10":"󰌢 ",
}

groups = [Group(n, label=l) for n,l in group_names.items()]
group_keys = [i for i in "1234567890"]

for i, k in zip(groups,group_keys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

defaults = dict(
    border_focus = "#eceff4",
    border_normal="#2e3440",
    border_width=2 ,
    margin=6
)

omni = OmniLayout(
        max_stack=3,
        border_focus_stack="#88c0d0",
        grow_amount=10,
        insert_position=1,
        **defaults        
    )

maxi = layout.Max(margin=6, name = "Max")
monad = layout.MonadTall(
    align = layout.MonadTall._left,
     ratio = 0.6,
     name = "Monad",
    single_border_width = 0,
    new_client_position = 'bottom',
    **defaults
)

monad_t = layout.MonadThreeCol(
    ratio = 0.6,
    name = "Monad",
    single_border_width = 0,
    new_client_position = 'bottom',
    **defaults
)

layouts = [
    # omni,
    monad,
    # monad_t,
    maxi,
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    #font="sans",
    font="NotoSansMono Nerd Font",
    fontsize=14,
    padding=3,
    foreground="#d8dee9",
    background="#2e3440",
)


def get_brightness():
    return subprocess.getoutput("getbrightness").strip()

extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(fmt=' {} '),
                widget.GroupBox(
                    inactive="#e5e9f0",
                    highlight_method='line',
                    active="#88c0d0",
                    highlight_color="#4c566a",
                    disable_drag=True,
                    hide_unused=True,
                    spacing=4),
                widget.WindowName(background="#d8dee9",foreground="#2e3440",fmt="  {}",padding=5),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Wlan(fmt='  {}',format='{essid} [{quality}/70]',mouse_callbacks={"Button1":lazy.spawn("kitty nmtui")}),
                widget.CPU(fmt='  {}',format='{load_percent}%'),
                widget.Memory(fmt='  {}',format='{MemUsed:.2f}{mm} / {MemTotal:.2f}{mm}',measure_mem='G'),
                widget.Volume(fmt='  {}'),
                widget.GenPollText(fmt="  {}%",
                                   func=get_brightness,
                                   update_interval=0.5,
                                   mouse_callbacks={
                                       "Button1":lazy.spawn("blight inc"),
                                       "Button3":lazy.spawn("blight dec"),
                                   }),
                widget.Battery(format='  {percent:2.0%}{char} ({hour:d}:{min:02d})'),
                widget.Clock(format="%d %b %Y %a %H:%M",fmt="  {} "),
                widget.Systray(),
            ],
            28,
            background = "#d8dee9"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=2,
    border_normal="#2e3440",
    border_focus="#eceff4"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Startup
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

@hook.subscribe.client_new
def new_client(c):
    # Use xdotool selectwindow getwindowclassname to find class name
    grp = ''
    match c.get_wm_class()[1]:
        #Chat
        case 'TelegramDesktop' | 'discord':
            grp = '6'
        #Music
        case "Spotify" | "Music":
            grp = '7'
        #Video
        case "mpv":
            c.cmd_toggle_floating()
            grp = '8'
        #Recording
        case "obs":
            grp = '9'
        #Coding
        case "Neovim" | "Code" | "Helix":
            grp = '10'
    if grp:
        c.togroup(grp, switch_group=True)

@hook.subscribe.client_focus
def update_label(c):
    g = c.group
    if g is not None and g.name in ["1","2","3","4","5"]:
        wname = c.get_wm_class()[1].capitalize()
        g.label = f"{group_names[g.name]} [{wname}]"

@hook.subscribe.client_killed
def reset_label(c):
    g = c.group
    if g is not None and g.name in ["1","2","3","4","5"]:
        if len(g.windows) == 1:
            g.label = group_names[g.name]
#
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
