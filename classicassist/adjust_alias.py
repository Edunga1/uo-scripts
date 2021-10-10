def adjust_alias(alias, msg='', color=60, check_object=True):
    value = GetAlias(alias)
    while not value or (check_object and not FindObject(alias)):
        msg = msg if msg else 'set alias: {}'.format(alias)
        HeadMsg(msg, 'self', color)
        PromptAlias(alias)
    return value
