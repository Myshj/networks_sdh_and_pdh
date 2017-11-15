from typing import Iterable

from Message import Message
from Tickable import Tickable
from data import stations, channels


def tick(tickable: Tickable):
    tickable.on_tick()


def tick_table(table: Iterable[Tickable]):
    for t in table:
        tick(t)


if __name__ == '__main__':
    channels.a_to_b._put(Message(
        destination=stations.c,
        rank=1
    ))

    for i in range(0, 10):
        print('tick {0}'.format(i))
        tick_table(channels.table)
        tick_table(stations.table)
