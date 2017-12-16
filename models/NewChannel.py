from typing import Optional

from Tickable import Tickable
from models.ChannelTypes import ChannelTypes
from models.NewMessage import NewMessage


class NewChannel(Tickable):
    def __init__(
            self,
            rank: int,
            channel_type: ChannelTypes
    ) -> None:
        super().__init__()
        self._to_transmit = None
        self._transmitted = None
        self._rank = rank
        self._type = channel_type

    @property
    def type(self) -> ChannelTypes:
        return self._type

    @property
    def rank(self) -> int:
        return self._rank

    @property
    def transmitted(self) -> Optional[NewMessage]:
        return self._transmitted

    def accept_to_transmit(self, message: NewMessage):
        self._to_transmit = message

    def flush(self):
        self._transmitted = None

    def on_tick(self) -> None:
        self._transmit()

    def _transmit(self):
        self._transmitted = self._to_transmit
        self._to_transmit = None
