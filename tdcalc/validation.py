from logging import getLogger

from .types import PaidAtInterval

logger = getLogger(__name__)


def validate_inputs(term_months: int, paid_at: PaidAtInterval) -> None:
    if (term_months < 12 and paid_at == "annually") or (term_months < 4 and paid_at == "quarterly"):
        logger.error(f"Cannot calculate a term of {term_months} months for interval {paid_at}")
        exit(1)
