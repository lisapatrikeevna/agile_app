from enum import Enum


class Statuses(Enum):
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    PENDING = 'pending'
    BLOCKED = 'blocked'
    TESTING = 'testing'
    CLOSED = 'closed'

    @classmethod
    def choices(cls):
        return ([i.name, i.value] for i in cls)











