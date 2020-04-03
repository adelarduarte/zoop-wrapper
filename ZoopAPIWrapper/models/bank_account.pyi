from ZoopAPIWrapper.models.base import Address as Address, BusinessOrIndividualModel as BusinessOrIndividualModel, MarketPlaceModel as MarketPlaceModel, VerificationModel as VerificationModel
from typing import Any, Optional

class BankAccountVerificationModel(VerificationModel):
    @classmethod
    def get_required_fields(cls): ...

class BankAccount(BusinessOrIndividualModel):
    RESOURCE: str = ...
    account_number: str
    bank_code: str
    holder_name: str
    routing_number: str
    address: Address
    verification_checklist: BankAccountVerificationModel
    bank_name: Optional[str]
    country_code: Optional[str]
    customer: Optional[str]
    description: Optional[str]
    debitable:  Optional[str]
    fingerprint: Optional[str]
    is_active: Optional[bool]
    is_verified: Optional[bool]
    last4_digits: Optional[str]
    phone_number: Optional[str]
    type: Optional[str]
    def init_custom_fields(self, address: Optional[Any] = ..., verification_checklist: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @classmethod
    def get_required_fields(cls): ...
    @classmethod
    def get_non_required_fields(cls): ...
    @classmethod
    def from_dict_and_seller(cls, seller: Any, data: Any): ...