>>> from ansicolor import colorize
>>> colorize('ayy', 'bold', 'underline', fg='red')
'\x1b[0;31;1;4mayy\x1b[0m'
>>> print(colorize('ayy', 'bold', 'underline', fg='red', esc='\e'))
\e[0;31;1;4mayy\e[0m
