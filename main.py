from models.ChannelTypes import ChannelTypes
from models.Generator import Generator
from models.Multiplexer import Multiplexer
from models.NewChannel import NewChannel

# c = Channel()
# printer = ChannelView(c)
#
# c.send_through(
#     Message(1000, 'd')
# )
#
# for i in range(0, 5400):
#     c.on_tick()


c_1_1 = NewChannel(1, ChannelTypes.STS)
c_1_2 = NewChannel(1, ChannelTypes.STS)

c_2_1 = NewChannel(2, ChannelTypes.STS)

channels = [c_1_1, c_1_2, c_2_1]

gen1 = Generator(
    header='h1',
    data=' ',
    out_channel=c_1_1
)
gen1.on_tick()

gen2 = Generator(
    header='h2',
    data=' ',
    out_channel=c_1_2
)
gen2.on_tick()

mult1 = Multiplexer(
    [c_1_1, c_1_2],
    c_2_1
)

stations = [gen1, gen2, mult1]

for i in range(0, 100):
    print('tick: {0}'.format(i))
    for c in channels:
        c.on_tick()

    for s in stations:
        s.on_tick()
