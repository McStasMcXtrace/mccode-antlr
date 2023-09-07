from textwrap import TextWrapper as PyTextWrapper


def pre_mid_post(string, open_token, close_token):
    io = string.find(open_token)
    ic = string.rfind(close_token)
    if 0 < io < ic:
        return string[:io], string[io+1:ic], string[ic+1:]
    return None, string, None


class TextWrapper(PyTextWrapper):

    def wrap(self, text: str, pad: str = None) -> list[str]:
        if pad is None:
            pad = ''
        return [self._wrap_line(line, self.width, pad) for line in text.splitlines(True)]

    def _wrap_line(self, line, width, pad) -> str:
        # This is not good enough. TODO Use a combined McCode _and_ C parser to identify reasonable line break points
        return line

        # from math import ceil
        # if len(line) <= width:
        #     return line
        #
        # if not any(',' == x for x in line):
        #     for o, c in (('{', '}'), ('(', ')'), ('[', ']')):
        #         pre, line, post = pre_mid_post(line, o, c)
        #         if pre:
        #             return (pad + self._wrap_line(pre, width, pad) + f'{o}\n'
        #                     + self._wrap_line(line, width, pad + '  ')
        #                     + f'\n{pad}{c}' + self._wrap_line(post, width, pad))
        #
        # if width == self.width:
        #     width = min(width, int(len(line) / ceil(len(line) / width)))
        # elif len(line) <= self.width:
        #     return pad + line
        #
        # first = line[:width]
        # for d in (',', ' ', '\t'):
        #     x = first.rfind(d)
        #     if x > 0:
        #         return pad + line[:x+1] + f'\n' + self._wrap_line(line[x+1:], width, pad)
        # for d in ('-', '+', '*', '/'):
        #     x = first.rfind(d)
        #     if x > 0:
        #         return pad + line[:x] + f'\n' + self._wrap_line(line[x:], width, pad)
        # return pad + line
