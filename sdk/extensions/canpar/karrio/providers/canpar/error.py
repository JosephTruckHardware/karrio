from typing import List
from karrio.core.models import Message
from karrio.core.utils import Element, extract_fault
from karrio.providers.canpar.utils import Settings


def parse_error_response(response: Element, settings: Settings) -> List[Message]:
    errors: List[Element] = response.xpath(".//*[local-name() = $name]", name="error")
    return (
        extract_fault(response, settings) +
        [
            Message(
                carrier_id=settings.carrier_id,
                carrier_name=settings.carrier_name,
                message=error.text,
            )
            for error in errors
            if error.text is not None
        ]
    )
