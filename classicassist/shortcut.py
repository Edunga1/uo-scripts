alias = 'shortcutf2'
if not FindAlias(alias) or not FindObject(alias, -1, 'backpack'):
    PromptAlias(alias)
UseObject(GetAlias(alias))
