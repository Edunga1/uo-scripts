HeadMsg('pet healing + firebaoll + WoD is running.')

def adjust_alias(alias, msg='', color=60):
    while not FindAlias(alias) or not FindObject(alias):
        HeadMsg(msg, 'self', color)
        PromptAlias(alias)

def adjust_pet():
    adjust_alias('pet', 'TARGET A PET', 60)

def adjust_enemy():
    adjust_alias('mob', 'TARGET A ENEMY', 25)

def bigheal(obj):
    if Poisoned(obj):
        Cast('Arch Cure', obj)
    else:
        Cast('Greater Heal', obj)

def loop():
    while FindObject('mob'):
        if DiffHitsPercent('pet') > 40:
            bigheal('pet')
        if not FindObject('mob'):
            continue
        if DiffHitsPercent('mob') < 75 and Mana('self') > 30:
            Cast('Fireball', 'mob')
        if DiffHitsPercent('mob') >= 75 and Mana('self') >= 60:
            Cast('Word of Death', 'mob')
            Pause(500)

def main():
    adjust_pet()
    adjust_enemy()
    loop()

main()
