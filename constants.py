from models.ChannelTypes import ChannelTypes

rows = 9

header_columns = {
    ChannelTypes.STS: 3,
    ChannelTypes.STM: 9
}

data_columns = {
    ChannelTypes.STS: 10,
    ChannelTypes.STM: 10
}

columns = {
    ChannelTypes.STS: header_columns[ChannelTypes.STS] + data_columns[ChannelTypes.STS],
    ChannelTypes.STM: header_columns[ChannelTypes.STM] + data_columns[ChannelTypes.STM]
}

overall_sizes = {
    ChannelTypes.STS: columns[ChannelTypes.STS] * rows,
    ChannelTypes.STM: columns[ChannelTypes.STM] * rows
}
