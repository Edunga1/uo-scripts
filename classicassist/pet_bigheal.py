def adjust_alias(alias, msg='', color=60):
    while not FindAlias(alias) or not FindObject(alias):
        HeadMsg(msg, 'self', color)
        PromptAlias(alias)

def adjust_pet():
    adjust_alias('pet', 'TARGET A PET', 60)

def bigheal(obj):
    if Poisoned(obj):
        Cast('Arch Cure', obj)
    else:
        Cast('Greater Heal', obj)

def main():
    while True:
        if DiffHitsPercent('pet') > 30 and Mana('self') > 30:
            bigheal('pet')

main()
