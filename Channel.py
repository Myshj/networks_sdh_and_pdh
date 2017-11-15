from Message import Message
from Station import Station
from Tickable import Tickable


class Channel(Tickable):
    def __init__(
            self,
            source: Station,
            destination: Station,
            rank: int
    ) -> None:
        super().__init__()
        self.source = source
        source.want_to_transmit_broadcaster.register(self._put)
        self.destination = destination
        self.rank = rank
        self.free_space = rank
        self.messages_to_transmit = set()

    def _put(self, message: Message):
        if message.rank > self.free_space:
            raise ValueError('Message too large.')
        self.messages_to_transmit.add(message)
        self.free_space -= message.rank

    def on_tick(self) -> None:
        super().on_tick()
        self._transmit_all()

    def _transmit_all(self):
        for message in self.messages_to_transmit:
            self.destination.receive(message)
            print(
                '{0} delivered to {1}'.format(str(message), str(self.destination))
            )
        self.messages_to_transmit.clear()
        self.free_space = self.rank
