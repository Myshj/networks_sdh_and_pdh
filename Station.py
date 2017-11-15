from Message import Message
from MulticastDelegate import MulticastDelegate
from Tickable import Tickable


class Station(Tickable):
    def __init__(
            self,
            name: str
    ) -> None:
        super().__init__()
        self.name = name
        self.want_to_transmit_broadcaster = MulticastDelegate()
        self.received_messages = set()

    def receive(self, message: Message):
        self.received_messages.add(message)

    def on_tick(self) -> None:
        super().on_tick()
        self._receive_all()
        self._forward_all()

    def _receive_all(self):
        for message in self.received_messages.copy():
            if self._is_for_me(message):
                self._report_about_received(message)
                self._forget_about(message)

    def _forward_all(self):
        for message in self.received_messages:
            self._forward(message)
        self._forget_about_all_messages()

    def _forward(self, message: Message):
        self.want_to_transmit_broadcaster.broadcast(message)
        print('{0} forwarded by {1}'.format(str(message), str(self)))

    def _is_for_me(self, message: Message):
        return message.destination is self

    def _report_about_received(self, message: Message):
        print('{0} received {1}'.format(str(self), str(message)))

    def _forget_about(self, message: Message):
        self.received_messages.remove(message)

    def _forget_about_all_messages(self):
        self.received_messages.clear()

    def __str__(self):
        return 'Station {0}'.format(self.name)
