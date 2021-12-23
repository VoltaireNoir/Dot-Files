# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi
export PATH=$PATH:~/Scripts

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt autocd extendedglob nomatch
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
#zstyle : ":completion:*" menu select
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

autoload -Uz compinit
compinit

# Enable Vim mode
#bindkey -v

# End of lines added by compinstall
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh


# Aliases

alias s="pacman -Ss"
alias as="paru"
alias i="sudo pacman -S"
alias ai="paru -S"
alias r="sudo pacman -Rcs"
alias checkupdates="checkupdates ; echo "---" ; paru -Qua"
alias update="sudo pacman -Syu"
alias updatemirrors="sudo pacman -Syyu"
alias au="paru -Syu"
alias clean="sudo pacman -Sc"
alias aclean="paru -Sc"
alias cls="clear"
alias mixer="pulsemixer"
alias ls="exa --icons"
alias lss="exa -a --icons"
alias lsp="exa -l --icons"
alias lssp="exa -la --icons"
alias matrix="cmatrix -s -C blue" 
alias incognito="sudo incognito"
alias data="cd /mnt/data"
alias vpnc="protonvpn-cli c"
alias vpnd="protonvpn-cli d"
alias bsp="startx ~/.xinitrc bspwm"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
