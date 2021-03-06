from zoop_wrapper.models.base import (
    PaymentMethod as PaymentMethod,
    ZoopObject as ZoopObject,
)
from typing import Any, Optional, List

class BillingConfiguration(ZoopObject):
    PERCENTAGE_MODE: str = ...
    DAILY_PERCENTAGE_MODE: str = ...
    MONTHLY_PERCENTAGE_MODE: str = ...
    FIXED_MODE: str = ...
    PERCENT_MODES: Any = ...
    MODES: Any = ...

    is_discount: Optional[bool]
    mode: Optional[str]
    start_date: Optional[str]
    limit_date: Optional[str]
    amount: Optional[str]
    percentage: Optional[str]
    def init_custom_fields(
        self, mode: Optional[str] = ..., is_discount: bool = ..., **kwarg: Any
    ) -> None: ...
    def validate_mode(self, mode: str): ...
    def set_type(self, mode: str, is_discount: bool) -> None: ...
    def get_validation_fields(self) -> set: ...
    def get_all_fields(self) -> set: ...
    @classmethod
    def get_required_fields(cls) -> set: ...
    @classmethod
    def get_fee_required_fields(cls) -> set: ...
    @classmethod
    def get_discount_required_fields(cls) -> set: ...
    @classmethod
    def get_fixed_required_fields(cls) -> set: ...
    @classmethod
    def get_percent_required_fields(cls) -> set: ...

class BillingInstructions(ZoopObject):
    late_fee: BillingConfiguration
    interest: BillingConfiguration
    discount: List[BillingConfiguration]
    def init_custom_fields(
        self,
        late_fee: Optional[Any] = ...,
        interest: Optional[Any] = ...,
        discount: Optional[Any] = ...,
        **kwargs: Any,
    ) -> None: ...
    @classmethod
    def get_required_fields(cls) -> set: ...

class Invoice(PaymentMethod):
    RESOURCE: str = ...

    expiration_date: str

    zoop_boleto_id: Optional[str]
    status: Optional[str]
    reference_number: Optional[str]
    document_number: Optional[str]
    recipient: Optional[str]
    bank_code: Optional[str]
    sequence: Optional[str]
    url: Optional[str]
    accepted: Optional[bool]
    printed: Optional[bool]
    downloaded: Optional[bool]
    fingerprint: Optional[str]
    paid_at: Optional[str]
    barcode: Optional[str]
    payment_limit_date: Optional[str]
    body_instructions: Optional[List[str]]
    billing_instructions: Optional[BillingInstructions]
    def init_custom_fields(self, billing_instructions: Optional[Any] = ..., **kwargs: Any) -> None: ...  # type: ignore
    @classmethod
    def get_required_fields(cls) -> set: ...
    @classmethod
    def get_non_required_fields(cls) -> set: ...
