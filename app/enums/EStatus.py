from enum import Enum


class EStatus(Enum):
    CREATED = "created"
    EXPIRED = "payment time exceed"
    ANALYSIS = "analysing"
    COMPLETE = "completed"
    CARGEBACK = "chargeback"
    PAID = "paid"
    REFUNDED = "refunded"
    FAILED = "failed"