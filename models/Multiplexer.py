import random
from typing import List

import constants
from Tickable import Tickable
from models.NewChannel import NewChannel
from models.NewMessage import NewMessage


class Multiplexer(Tickable):
    chance_of_new_message = 0.5
    min_message_size = 1.1
    max_message_size = 1.5
    message_symbol = 'd'

    def __init__(
            self,
            in_channels: List[NewChannel],
            out_channel: NewChannel
    ) -> None:
        super().__init__()
        if sum((ch.rank for ch in in_channels)) != out_channel.rank:
            raise ValueError('Сумма рангов входящих каналов должна быть равна рангу исходящего.')
        if any((ch.rank != in_channels[0].rank) for ch in in_channels):
            raise ValueError('Все входные каналы должны быть одинаковыми.')
        if any((ch.type != out_channel.type for ch in in_channels)):
            raise ValueError('Можно мультиплексировать только каналы одного типа (STS или STM)')
        self._in_channels = in_channels

        self._out_channel = out_channel
        self._data = []

        self._new_message_symbols_remaining = 0
        self._new_message_size = 0

    def _make_data(self) -> List[str]:
        data = []
        index_in_small_message = -1
        for i in range(0, self._out_channel.rank * constants.overall_sizes[self._out_channel.type]):
            if i % len(self._in_channels) == 0:
                index_in_small_message += 1
            data.append(self._in_channels[i % len(self._in_channels)].transmitted.data[index_in_small_message])
        return data

    def on_tick(self) -> None:
        super().on_tick()

        m = NewMessage(
            data=self._make_data()
        )
        if self._new_message_symbols_remaining == 0:
            r = random.random()
            if r > Multiplexer.chance_of_new_message:
                print('new message generated')
                self._generate_and_transmit_new_message(m)

        else:
            self._continue_generated_message_transmission(m)

        self._out_channel.accept_to_transmit(m)
        print('Message: ', end='')
        for i in range(0, len(m.data)):
            print(m.data[i], end='')

        print('end of message')

    def _generate_and_transmit_new_message(self, m):
        self._new_message_size = int(
            random.uniform(
                Multiplexer.min_message_size,
                Multiplexer.max_message_size
            ) * constants.overall_sizes[self._out_channel.type]
        )
        self._new_message_symbols_remaining = self._new_message_size
        print('size: ' + str(self._new_message_size))
        new_message_generation_time = random.randrange(constants.overall_sizes[self._out_channel.type])
        print('time: ' + str(new_message_generation_time))
        for i, symbol in enumerate(m.data):
            if i >= new_message_generation_time and symbol.isspace():
                m.data[i] = Multiplexer.message_symbol
                self._new_message_symbols_remaining -= 1
                if self._new_message_symbols_remaining == 0:
                    break

    def _continue_generated_message_transmission(self, carrier_message):
        for i, symbol in enumerate(carrier_message.data):
            if symbol.isspace():
                carrier_message.data[i] = Multiplexer.message_symbol
                self._new_message_symbols_remaining -= 1
                if self._new_message_symbols_remaining == 0:
                    break
