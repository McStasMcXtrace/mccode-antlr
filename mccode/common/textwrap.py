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

    def comment(self, name: str, content: str) -> str:
        pad = ' '*(len(name) + 1)
        lines = self.wrap(content, pad=pad)
        lines[0] = f'{name} {lines[0].strip()}'
        return '/*' + '\n* '.join(lines) + '\n*/'

    @staticmethod
    def start_block_comment(name: str) -> str:
        return f'/* {name}'

    @staticmethod
    def end_block_comment() -> str:
        return '*/'

    def block(self, name: str, content: str) -> str:
        return '\n'.join([name + '%{', *self.wrap(content), '}%'])

    def line(self, name: str, items: list[str], sep: str = ' ') -> str:
        return '\n'.join(self.wrap(f'{name} {sep.join(items)}'))

    @staticmethod
    def metadata_group(name: str, mimetype: str, item: str, value: str) -> str:
        return f'{name} "{mimetype}" {item} %{{{value}%}}'

    @staticmethod
    def datatype(data_type: str) -> str:
        return data_type

    @staticmethod
    def parameter(parameter: str) -> str:
        return f'{parameter}'

    @staticmethod
    def unit(unit: str) -> str:
        return f'/{unit}'

    @staticmethod
    def value(value: str) -> str:
        return f'{value}'

    @staticmethod
    def start_list(name: str) -> str:
        return name

    @staticmethod
    def end_list(name: str) -> str:
        return name

    @staticmethod
    def start_list_item() -> str:
        return ''

    @staticmethod
    def end_list_item() -> str:
        return ''

    @staticmethod
    def list_item(content: str) -> str:
        return content

    @staticmethod
    def escape(content: str) -> str:
        return content

    @staticmethod
    def url(content: str) -> str:
        return content


    @staticmethod
    def _wrap_line(line, width, pad) -> str:
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


class HTMLWrapper:

    @staticmethod
    def wrap(text: str, pad: str = None) -> list[str]:
        return [text]

    @staticmethod
    def comment(name: str, content: str) -> str:
        return f"<details><summary>{name}</summary>{content}</details>"

    @staticmethod
    def start_block_comment(name: str) -> str:
        return f'<details><summary>{name}</summary>'

    @staticmethod
    def end_block_comment() -> str:
        return '</details>'

    def block(self, name: str, content: str) -> str:
        return '<br>'.join([f"<b>{name}</b>" + '%{', *self.wrap(content), '}%'])

    def line(self, name: str, items: list[str], sep: str = ' ') -> str:
        return ''.join(self.wrap(f'<b>{name}</b> {sep.join(items)}'))

    @staticmethod
    def metadata_group(name: str, mimetype: str, item: str, value: str) -> str:
        return f'<b>{name}</b> <code>"{mimetype}"</code>" <var>{item}</var> %{{<pre>{value}</pre>%}}'

    @staticmethod
    def datatype(data_type: str) -> str:
        return f'<code>{data_type}</code>'

    @staticmethod
    def parameter(parameter: str) -> str:
        return f'<var>{parameter}</var>'

    @staticmethod
    def unit(unit: str) -> str:
        return f'/{unit}'

    @staticmethod
    def value(value: str) -> str:
        return f'<code>{value}</code>'

    @staticmethod
    def start_list(name: str) -> str:
        return f'<ul> {name}'

    @staticmethod
    def end_list(name: str) -> str:
        return f'</ul> {name}'

    @staticmethod
    def start_list_item() -> str:
        return '<li>'

    @staticmethod
    def end_list_item() -> str:
        return '</li>'
    @staticmethod
    def list_item(content: str) -> str:
        return f'<li>{content}</li>'

    @staticmethod
    def escape(content: str) -> str:
        from html import escape
        return escape(content)

    @staticmethod
    def url(content: str) -> str:
        return f'<a href="{content}">{content}</a>'
