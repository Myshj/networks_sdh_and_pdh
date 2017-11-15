from Channel import Channel
from data import stations

a_to_b = Channel(
    source=stations.a,
    destination=stations.b,
    rank=1
)

b_to_c = Channel(
    source=stations.b,
    destination=stations.c,
    rank=1
)

table = {
    a_to_b, b_to_c
}
