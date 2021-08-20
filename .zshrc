# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Use powerline
USE_POWERLINE="true"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi
# Use manjaro zsh prompt
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
  source /usr/share/zsh/manjaro-zsh-prompt
fi


# Custom aliases
alias ls="exa --icons"
alias lss="exa -a --icons"
alias lsp="exa -l --icons"
alias lssp="exa -la --icons"
alias data="cd /mnt/80486C04486BF6F6"
alias mv="mv -i"
alias cls="clear"
alias remove="pamac remove -o"
alias install="pamac install"
alias search="pamac search"
alias update="pamac update"
alias checkupdates="pamac checkupdates"
alias pacman="sudo pacman"
alias matrix="cmatrix -C blue"
alias mixer="pulsemixer"
alias vpn="protonvpn-cli c"
alias vpnd="protonvpn-cli d"

# Print out Animals and Sayings
#fortune -s | cowthink -f $(ls /usr/share/cows/*.cow|shuf -n 1) | lolcat
#Print animals and sayings along wiht neofetch
#neofetch --ascii "$(fortune -n 80 -s | cowsay -W 30 -f $(cat /usr/share/cows/neolist|shuf -n 1))" | lolcat

# Spaceship
#autoload -U promptinit; promptinit
#prompt spaceship

#SPACESHIP_PROMPT_SEPARATE_LINE=false
#SPACESHIP_CHAR_SYMBOL=">"

# Starship prompt
#eval "$(starship init zsh)"

# Paths
 export PATH=$PATH:~/Scripts:~/.emacs.d/bin

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
