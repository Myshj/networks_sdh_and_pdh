class Message:
    def __init__(
            self,
            destination: 'Station',
            rank: int
    ) -> None:
        super().__init__()
        self.destination = destination
        self.rank = rank

    def __str__(self):
        return 'Message with {0} rank'.format(self.rank)
