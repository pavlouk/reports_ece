"dein Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath+=/home/pavlos/.config/nvim/dein//repos/github.com/Shougo/dein.vim

" Required:   :call dein#update()
if dein#load_state('/home/pavlos/.config/nvim/dein/')
  call dein#begin('/home/pavlos/.config/nvim/dein/')

  " Let dein manage dein
  " Required:
  call dein#add('/home/pavlos/.config/nvim/dein//repos/github.com/Shougo/dein.vim')

  " Add or remove your plugins here:
  call dein#add('Shougo/neosnippet.vim')
  call dein#add('Shougo/neosnippet-snippets')

  " You can specify revision/branch/tag.
  "call dein#add('Shougo/vimshell', { 'rev': '3787e5' })
  "call dein#add('Shougo/deoplete.nvim')
  "call dein#add('Rip-Rip/clang_complete')
  "call dein#add('zchee/deoplete-clang')
  "call dein#add('google/vim-colorscheme-primary')
  "call dein#add('vim-latex/vim-latex')

  call dein#add('vim-airline/vim-airline')
  call dein#add('tpope/vim-fugitive')
  call dein#add('scrooloose/nerdtree')
  call dein#add('vim-syntastic/syntastic')
  call dein#add('jiangmiao/auto-pairs')
  call dein#add('Yggdroot/indentLine')
  call dein#add('Valloric/YouCompleteMe')
  call dein#add('altercation/vim-colors-solarized')    

  " Required:
  call dein#end()
  call dein#save_state()
endif

" Required:
filetype plugin indent on
syntax enable

" If you want to install not installed plugins on startup.
if dein#check_install()
  call dein#install()
endif

"End dein Scripts-------------------------

"let g:deoplete#sources#clang#libclang_path='/usr/lib/llvm-3.8/lib/libclang.so'
"let g:deoplete#sources#clang#clang_header='/usr/include/clang'
"let g:deoplete#enable_at_startup=1
"let g:clang_complete_library_path='/usr/lib/llvm-3.8/lib/libclang.so'
"let g:clang_complete_auto=1
"let g:clang_use_library=1
"=========================================

let g:ycm_global_ycm_extra_conf='~/.config/nvim/.ycm_extra_conf.py'
let g:ycm_confirm_extra_conf = 0
let g:ycm_python_binary_path ='/usr/lib/python3.5'

"==============airline options================
let g:airline_left_sep=''
let g:airline_right_sep=''
let g:airline_powerline_fonts = 1
let g:airline_skip_empty_sections = 1
"==========syntastic=================
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
"======================================

if has("autocmd")       " Jump to the last position after start up
  au BufReadPost *
   \ if line("'\"") > 1 && line("'\"") <= line("$") |
   \ exe "normal! g'\"" |
   \ endif
endif

highlight CursorLine term=reverse cterm=None ctermbg=242 guibg=Grey40
syntax on
let g:solarized_termcolors=256
set t_Co=256 
set background=dark
colorscheme solarized
set clipboard=unnamedplus "Pasting from systems clipboard
set completeopt-=preview   "for YCM
set shiftwidth=2
set softtabstop=2
set expandtab
set scrolloff=3
set sidescrolloff=7
set sidescroll=1
set incsearch        "Find the next match as we type the search
set hlsearch
set cc=80
set nobackup
set noswapfile
set wildmenu 
set wildmode=list:full
set wildignore=*.swp,*.bak,*.pyc,*.class,*.log,*.aux,*.pdf
set relativenumber      " Show relative to the cursor numbering
set cursorline          " Highlight cursor line
set relativenumber      " Show relative to the cursor numbering
"let g:deoplete#enable_at_startup = 1
set tw=80               "Text width
set fo+=t               "Format option for text
set fo -=l              "But not for lines
set autowrite           "Save before various commands e.g. :make
set noshowmode          "Don't show the mode(airline is handling it)
set conceallevel=0      "Show $$$$
nmap <f9> :make!<Enter>
nnoremap <Enter> :noh<Enter><Enter>


