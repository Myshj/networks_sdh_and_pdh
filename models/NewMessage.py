from typing import List


class NewMessage:
    def __init__(
            self,
            data: List[str]
    ) -> None:
        super().__init__()
        self._data = data
        self._size = len(data)

    @property
    def data(self) -> List[str]:
        return self._data

    @property
    def size(self) -> int:
        return self._size
