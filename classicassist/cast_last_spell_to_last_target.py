from ClassicAssist.Data.Hotkeys import Commands

while True:
    Commands.CastLastSpell().Execute()
    WaitForTarget(5000)
    Target('last', False, True)
