set nocompatible
set nocindent
set cul                                                             " highlight current line
hi CursorLine term=none cterm=none ctermbg=3                        " adjust color
set nu                                                              " Line numbers on
set nowrap                                                          " wrap long lines
set autoindent                                                      " indent at the same level of the previous line
set shiftwidth=4 ts=4 et                                            " use indents of 4 spaces plus an indentation every four columns
set incsearch hlsearch                                              " highlight search terms
set smartindent
set virtualedit=onemore                                             " allow for cursor beyond last character
set history=1000                                                    " Store a ton of history (default is 20)
set showmatch                                                       " show matching brackets/parenthesis
set incsearch                                                       " find as you type search
set wildmenu                                                        " show list instead of just completing


colorscheme ron                                                     " Preffered colorscheme
filetype plugin indent on                                           " Automatically detect file types.
set mouse=a                                                         " Automatically enable mouse usage
syntax on                                                           " syntax highlighting
scriptencoding utf-8

highlight link RedundantSpaces Error				                " Highlight trailing whitespace and tabs
au BufEnter,BufRead * match RedundantSpaces "\t"
au BufEnter,BufRead * match RedundantSpaces "[[:space:]]\+$"

let g:is_sh = 1							                            "Set default sh to bash

function! s:DiffWithSaved()
    let filetype=&ft
    diffthis
    vnew | r # | normal! 1Gdd
    diffthis
    exe "setlocal bt=nofile bh=wipe nobl noswf ro ft=" . filetype
endfunction
com! DiffSaved call s:DiffWithSaved()

cmap w!! %!sudo tee > /dev/null %		                            " Will allow you to use :w!! to write to a file using sudo
autocmd BufEnter * execute "chdir ".escape(expand("%:p:h"), ' ')
