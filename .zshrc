if [[ ! -d ~/.zgen ]];then
    git clone --recursive https://github.com/rslindee/zgen.git ~/.zgen
fi

ZGEN_RESET_ON_CHANGE=(~/.zshrc)

source ~/.zgen/zgen.zsh

if ! zgen saved; then
	### PREZTO CONFIGS ###
    zgen prezto "*" color 'yes'

    zgen prezto terminal auto-title 'yes'
    zgen prezto terminal:window-title format '%n@%m: %s'
    zgen prezto terminal:tab-title format '%m: %s'

    zgen prezto prompt theme 'agnoster'
	
    ### PREZTO PLUGINS ###
    ZGEN_PREZTO_LOAD_DEFAULT=0

    # The order matters
    zgen prezto
    zgen prezto terminal
    zgen prezto command-not-found
    zgen prezto history
    zgen prezto utility
    zgen prezto completion
    zgen prezto syntax-highlighting
    zgen prezto history-substring-search
    zgen prezto prompt

    ### THIRD-PARTY PLUGINS ###
    zgen load jmatsuzawa/zsh-comp-gsettings

    zgen save
fi

### CONFIGS ###
zstyle ':completion:*:processes-names' command 'NOCOLORS=1 ps xho command|sed "s/://g"'

unsetopt correct # Disable commands autocorrection

DEFAULT_USER=`whoami`
SELECTED_EDITOR="/bin/nano"

export PATH="/home/djaler/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

bindkey '^H' backward-kill-word

### ALIASES ###
alias please='sudo $(fc -ln -1)'

alias root='sudo -s'
