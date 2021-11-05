from attr import s
from typing import Optional
from jstruct import JStruct


@s(auto_attribs=True)
class PickupAddress:
    name: Optional[str] = None
    companyName: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    address3: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[int] = None
    country: Optional[str] = None
    phone: Optional[int] = None
    email: Optional[str] = None


@s(auto_attribs=True)
class CreatePickupResponse:
    shipmentIdentifier: Optional[str] = None
    pickupAccount: Optional[int] = None
    pickupTimeBegin: Optional[str] = None
    pickupTimeEnd: Optional[str] = None
    readyBy: Optional[str] = None
    merchantId: Optional[str] = None
    packagingType: Optional[str] = None
    containerCount: Optional[int] = None
    shipmentCount: Optional[int] = None
    packageCount: Optional[int] = None
    value: Optional[int] = None
    currency: Optional[str] = None
    shipmentWeight: Optional[int] = None
    weightUom: Optional[str] = None
    specialInstructions: Optional[str] = None
    pickupAddress: Optional[PickupAddress] = JStruct[PickupAddress]