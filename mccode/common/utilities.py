def escape_str_for_c(s: str):
    return s.encode('unicode-escape').decode('utf-8').replace('"', r'\"')
