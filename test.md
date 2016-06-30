>>> from ansicolor import colorize
>>> colorize('ayy', fg='red', bold=True, underline=True)
'\x1b[0;31;1;4mayy\x1b[0m'
>>> print(colorize('ayy', fg='red', bold=True, underline=True, esc='\e'))
\e[0;31;1;4mayy\e[0m
