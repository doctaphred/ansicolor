"""
http://misc.flogisoft.com/bash/tip_colors_and_formatting
"""


colors = {
    'default': '9',
    'black': '0',
    'red': '1',
    'green': '2',
    'yellow': '3',
    'blue': '4',
    'magenta': '5',
    'cyan': '6',
    'gray': '7',
}

effects = {
    'bold': '1',
    'faint': '2',
    'italic': '3',
    'underline': '4',
    'blink': '5',
    'negative': '7',
    'hidden': '8',
    'strikethrough': '9',
}

FG_PREFIX = '3'
BG_PREFIX = '4'
BRIGHT_FG_PREFIX = '9'
BRIGHT_BG_PREFIX = '10'
RESET_EFFECT_PREFIX = '2'
RESET_EVERYTHING = '0'
ESCAPE = '\x1b'
RESET = '\x1b[0m'


color_info = {}
for name, code in colors.items():
    color_info[name] = (name, False)
for name, code in colors.items():
    color_info['bright_' + name] = (name, True)
    color_info['bright ' + name] = (name, True)
color_info['dark_gray'] = ('black', True)
color_info['dark gray'] = ('black', True)
color_info['white'] = ('gray', True)


def color_code(color_name, fg=True):
    color, bright = color_info[color_name]
    if fg:
        if bright:
            return BRIGHT_FG_PREFIX + colors[color]
        else:
            return FG_PREFIX + colors[color]
    else:
        if bright:
            return BRIGHT_BG_PREFIX + colors[color]
        else:
            return BG_PREFIX + colors[color]


def encode(name, value):
    if name == 'fg':
        return color_code(value, fg=True)
    elif name == 'bg':
        return color_code(value, fg=False)
    elif value:
        return effects[name]
    else:
        return RESET_EFFECT_PREFIX + effects[name]


class AnsiFormat:

    attrs = (
        ('fg', None),
        ('bg', None),
        ('bold', None),
        ('faint', None),
        ('underline', None),
        ('blink', None),
        ('negative', None),
    )

    def __init__(self, **attrs):
        for name, default in self.attrs:
            setattr(self, name, attrs.get(name, default))

    def _codes(self):
        yield RESET_EVERYTHING
        for name, _ in self.attrs:
            value = getattr(self, name)
            if value is not None:
                yield encode(name, value)

    def codes(self):
        return ';'.join(self._codes())

    def seq(self, esc=ESCAPE):
        return '{}[{}m'.format(esc, self.codes())

    def __str__(self):
        return self.seq()

    def __repr__(self):
        attrs = ', '.join(
            '{}={}'.format(name, getattr(self, name))
            for name, _ in self.attrs
        )
        return '{}({})'.format(self.__class__.__name__, attrs)


reset = AnsiFormat()


def colorize(obj, *, esc=ESCAPE, end=reset, **attrs):
    return '{}{}{}'.format(AnsiFormat(**attrs).seq(esc), obj, end.seq(esc))
