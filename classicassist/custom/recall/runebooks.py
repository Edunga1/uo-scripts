from ClassicAssist.Data.Macros.Commands.AliasCommands import SetAlias, GetAlias
from ClassicAssist.Data.Macros.Commands.EntityCommands import X, Y
from ClassicAssist.Data.Macros.Commands.GumpCommands import ReplyGump, WaitForGump
from ClassicAssist.Data.Macros.Commands.MainCommands import Pause
from ClassicAssist.Data.Macros.Commands.MsgCommands import HeadMsg
from ClassicAssist.Data.Macros.Commands.JournalCommands import InJournal
from ClassicAssist.Data.Macros.Commands.ObjectCommands import UseObject


def init_alias(alias_name, default_value=0):
    found = GetAlias(alias_name)
    if not found:
        SetAlias(alias_name, default_value)
        return default_value
    return found


class Runebooks:
    MAX_RUNES = 16
    RUNEBOOK_RECALL_GUMP_INDEX = 50

    def __init__(
        self,
        books,
        alias_recall_index='alias_recall_index',
        alias_runebook_index='alias_runebook_idx',
    ):
        self.books = books
        self.idx = 0
        self.book_idx = 0
        self.alias_recall_index = alias_recall_index
        self.alias_runebook_index = alias_runebook_index
        self._init_indexes()

    def _init_indexes(self):
        self.idx = init_alias(self.alias_recall_index)
        self.book_idx = init_alias(self.alias_runebook_index)

    def next(self):
        self.idx += 1

        if self.idx >= self.MAX_RUNES:
            self.idx = 0
            self.book_idx += 1

        if self.book_idx >= len(self.books):
            self.book_idx = 0

        SetAlias(self.alias_recall_index, self.idx)
        SetAlias(self.alias_runebook_index, self.book_idx)

    @property
    def book(self):
        return self.books[self.book_idx]

    def _recall(self):
        pre_x = X('self')
        pre_y = Y('self')

        while (
            (pre_x == X('self') and pre_y == Y('self'))
            and not InJournal('block')
        ):
            UseObject(self.book)
            WaitForGump(0x59, 5000)
            ReplyGump(0x59, self.RUNEBOOK_RECALL_GUMP_INDEX + self.idx)
            Pause(3000)

    def head_msg_current(self):
        HeadMsg('next: book-{} rune-{}'.format(self.book_idx + 1, self.idx + 1))

    def recall(self):
        self._recall()