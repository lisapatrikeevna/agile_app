from enum import Enum


class Priority(Enum):
    LOW = (1, 'low')
    MEDIUM = (2, 'medium')
    HIGH = (3, 'high')
    CRITICAL = (4, 'critical')

    @classmethod
    def choices(cls):
        return [(pr.value[0], pr.value[1]) for pr in cls]

    def __getitem__(self, item):
        return self.value[item]
