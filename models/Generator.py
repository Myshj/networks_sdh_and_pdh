import constants
from Tickable import Tickable
from models.NewChannel import NewChannel
from models.NewMessage import NewMessage


class Generator(Tickable):
    def __init__(
            self,
            header: str,
            data: str,
            out_channel: NewChannel
    ) -> None:
        super().__init__()
        self._header = header
        self._data = data
        self._out_channel = out_channel

    def on_tick(self) -> None:
        super().on_tick()
        r = self._out_channel.rank
        data = []
        t = self._out_channel.type
        for i in range(0, 9):
            for j in range(0, constants.header_columns[t] * r):
                data.append(self._header)
            for j in range(0, constants.data_columns[t] * r):
                data.append(self._data)
        self._out_channel.accept_to_transmit(NewMessage(data))
