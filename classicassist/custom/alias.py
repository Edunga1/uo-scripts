from ClassicAssist.Data.Macros.Commands.AliasCommands import GetAlias, PromptAlias
from ClassicAssist.Data.Macros.Commands.ObjectCommands import FindObject
from ClassicAssist.Data.Macros.Commands.MsgCommands import HeadMsg


def adjust_alias(alias, msg='', color=60, check_object=True):
    while not GetAlias(alias) or (check_object and not FindObject(alias)):
        msg = msg if msg else 'set alias: {}'.format(alias)
        HeadMsg(msg, 'self', color)
        PromptAlias(alias)
    return GetAlias(alias)