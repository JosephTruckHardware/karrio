import unittest
from datetime import datetime
from unittest.mock import patch
from purplship.core.utils.helpers import to_dict
from purplship.core.models import RateRequest
from purplship.package import rating
from tests.purolator.package.fixture import gateway


class TestPurolatorQuote(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.RateRequest = RateRequest(**RATE_REQUEST_PAYLOAD)

    def test_create_shipment_request(self):
        request = gateway.mapper.create_rate_request(self.RateRequest)

        self.assertEqual(request.serialize(), RATE_REQUEST_XML)

    @patch("purplship.package.mappers.purolator.proxy.http", return_value="<a></a>")
    def test_create_shipment(self, http_mock):
        rating.fetch(self.RateRequest).from_(gateway)

        url = http_mock.call_args[1]["url"]
        self.assertEqual(
            url,
            f"{gateway.settings.server_url}/EWS/V2/Estimating/EstimatingService.asmx",
        )

    def test_parse_shipment_response(self):
        with patch("purplship.package.mappers.purolator.proxy.http") as mock:
            mock.return_value = RATE_RESPONSE_XML
            parsed_response = rating.fetch(self.RateRequest).from_(gateway).parse()

            self.assertEqual(to_dict(parsed_response), to_dict(PARSED_RATE_RESPONSE))


if __name__ == "__main__":
    unittest.main()


RATE_REQUEST_PAYLOAD = {
    "shipper": {
        "person_name": "Aaron Summer",
        "state_code": "ON",
        "city": "Mississauga",
        "country_code": "CA",
        "postal_code": "L4W5M8",
        "address_line_1": "Main Street",
        "phone_number": "5555555",
    },
    "recipient": {
        "person_name": "Aaron Summer",
        "state_code": "BC",
        "city": "Burnaby",
        "country_code": "CA",
        "postal_code": "V5C5A9",
        "address_line_1": "Douglas Road",
        "phone_number": "2982181",
    },
    "parcel": {
        "reference": "Reference For Shipment",
        "weight": 10,
        "weight_unit": "LB",
        "services": ["purolator_express"],
    },
}

RATE_REQUEST_WITH_PRESET_PAYLOAD = {
    "shipper": {
        "person_name": "Aaron Summer",
        "state_code": "ON",
        "city": "Mississauga",
        "country_code": "CA",
        "postal_code": "L4W5M8",
        "address_line_1": "Main Street",
        "phone_number": "5555555",
    },
    "recipient": {
        "person_name": "Aaron Summer",
        "state_code": "BC",
        "city": "Burnaby",
        "country_code": "CA",
        "postal_code": "V5C5A9",
        "address_line_1": "Douglas Road",
        "phone_number": "2982181",
    },
    "parcel": {
        "reference": "Reference For Shipment",
        "package_preset": "purolator_express_box",
        "services": ["purolator_express"],
    },
}

PARSED_RATE_RESPONSE = [[{'base_charge': 62.35, 'carrier': 'purolator', 'currency': 'CAD', 'delivery_date': '2009-04-17', 'discount': 0.0, 'duties_and_taxes': 5.15, 'extra_charges': [{'amount': 0.0, 'currency': 'CAD', 'name': 'PST/QST'}, {'amount': 0.0, 'currency': 'CAD', 'name': 'HST'}, {'amount': 5.15, 'currency': 'CAD', 'name': 'GST'}, {'amount': 1.85, 'currency': 'CAD', 'name': 'Residential Delivery'}, {'amount': 2.81, 'currency': 'CAD', 'name': 'Fuel'}, {'amount': 36.0, 'currency': 'CAD', 'name': 'Dangerous Goods Classification'}], 'service_name': 'purolator_express_9_am', 'total_charge': 108.16}, {'base_charge': 55.0, 'carrier': 'purolator', 'currency': 'CAD', 'delivery_date': '2009-04-17', 'discount': 0.0, 'duties_and_taxes': 4.77, 'extra_charges': [{'amount': 0.0, 'currency': 'CAD', 'name': 'PST/QST'}, {'amount': 0.0, 'currency': 'CAD', 'name': 'HST'}, {'amount': 4.77, 'currency': 'CAD', 'name': 'GST'}, {'amount': 1.85, 'currency': 'CAD', 'name': 'Residential Delivery'}, {'amount': 2.48, 'currency': 'CAD', 'name': 'Fuel'}, {'amount': 36.0, 'currency': 'CAD', 'name': 'Dangerous Goods Classification'}], 'service_name': 'purolator_express_10_30_am', 'total_charge': 100.1}, {'base_charge': 46.15, 'carrier': 'purolator', 'currency': 'CAD', 'delivery_date': '2009-04-17', 'discount': 0.0, 'duties_and_taxes': 4.3, 'extra_charges': [{'amount': 0.0, 'currency': 'CAD', 'name': 'PST/QST'}, {'amount': 0.0, 'currency': 'CAD', 'name': 'HST'}, {'amount': 4.3, 'currency': 'CAD', 'name': 'GST'}, {'amount': 1.85, 'currency': 'CAD', 'name': 'Residential Delivery'}, {'amount': 2.08, 'currency': 'CAD', 'name': 'Fuel'}, {'amount': 36.0, 'currency': 'CAD', 'name': 'Dangerous Goods Classification'}], 'service_name': 'purolator_express', 'total_charge': 90.38}, {'base_charge': 29.6, 'carrier': 'purolator', 'currency': 'CAD', 'delivery_date': '2009-04-22', 'discount': 0.0, 'duties_and_taxes': 3.44, 'extra_charges': [{'amount': 0.0, 'currency': 'CAD', 'name': 'PST/QST'}, {'amount': 0.0, 'currency': 'CAD', 'name': 'HST'}, {'amount': 3.44, 'currency': 'CAD', 'name': 'GST'}, {'amount': 1.85, 'currency': 'CAD', 'name': 'Residential Delivery'}, {'amount': 1.33, 'currency': 'CAD', 'name': 'Fuel'}, {'amount': 36.0, 'currency': 'CAD', 'name': 'Dangerous Goods Classification'}], 'service_name': 'purolator_ground', 'total_charge': 72.22}, {'base_charge': 87.69, 'carrier': 'purolator', 'currency': 'CAD', 'delivery_date': '2009-04-22', 'discount': 0.0, 'duties_and_taxes': 6.47, 'extra_charges': [{'amount': 0.0, 'currency': 'CAD', 'name': 'PST/QST'}, {'amount': 0.0, 'currency': 'CAD', 'name': 'HST'}, {'amount': 6.47, 'currency': 'CAD', 'name': 'GST'}, {'amount': 1.85, 'currency': 'CAD', 'name': 'Residential Delivery'}, {'amount': 3.95, 'currency': 'CAD', 'name': 'Fuel'}, {'amount': 36.0, 'currency': 'CAD', 'name': 'Dangerous Goods Classification'}], 'service_name': 'purolator_ground', 'total_charge': 135.96}], []]

RATE_REQUEST_XML = f"""<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://purolator.com/pws/datatypes/v1">
    <SOAP-ENV:Header>
        <ns1:RequestContext>
            <Version>2.1</Version>
            <Language>en</Language>
            <UserToken>token</UserToken>
        </ns1:RequestContext>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <ns1:GetFullEstimateRequest>
            <Shipment>
                <SenderInformation>
                    <Address>
                        <Name>Aaron Summer</Name>
                        <StreetName>Main Street</StreetName>
                        <City>Mississauga</City>
                        <Province>ON</Province>
                        <Country>CA</Country>
                        <PostalCode>L4W5M8</PostalCode>
                        <PhoneNumber>
                            <Phone>5555555</Phone>
                        </PhoneNumber>
                    </Address>
                </SenderInformation>
                <ReceiverInformation>
                    <Address>
                        <Name>Aaron Summer</Name>
                        <StreetName>Douglas Road</StreetName>
                        <City>Burnaby</City>
                        <Province>BC</Province>
                        <Country>CA</Country>
                        <PostalCode>V5C5A9</PostalCode>
                        <PhoneNumber>
                            <Phone>2982181</Phone>
                        </PhoneNumber>
                    </Address>
                </ReceiverInformation>
                <ShipmentDate>{str(datetime.now().strftime("%Y-%m-%d"))}</ShipmentDate>
                <PackageInformation>
                    <ServiceID>PurolatorExpress</ServiceID>
                    <TotalWeight>
                        <Value>10</Value>
                        <WeightUnit>lb</WeightUnit>
                    </TotalWeight>
                    <TotalPieces>1</TotalPieces>
                    <PiecesInformation>
                        <Piece>
                            <Weight>
                                <Value>10.</Value>
                                <WeightUnit>lb</WeightUnit>
                            </Weight>
                        </Piece>
                    </PiecesInformation>
                </PackageInformation>
                <PickupInformation>
                    <PickupType>DropOff</PickupType>
                </PickupInformation>
                <TrackingReferenceInformation>
                    <Reference1>Reference For Shipment</Reference1>
                </TrackingReferenceInformation>
            </Shipment>
            <ShowAlternativeServicesIndicator>true</ShowAlternativeServicesIndicator>
        </ns1:GetFullEstimateRequest>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""

RATE_REQUEST_WITH_PRESET_XML = f"""<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://purolator.com/pws/datatypes/v1">
    <SOAP-ENV:Header>
        <ns1:RequestContext>
            <Version>2.1</Version>
            <Language>en</Language>
            <UserToken>token</UserToken>
        </ns1:RequestContext>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <ns1:GetFullEstimateRequest>
            <Shipment>
                <SenderInformation>
                    <Address>
                        <Name>Aaron Summer</Name>
                        <StreetName>Main Street</StreetName>
                        <City>Mississauga</City>
                        <Province>ON</Province>
                        <Country>CA</Country>
                        <PostalCode>L4W5M8</PostalCode>
                        <PhoneNumber>
                            <Phone>5555555</Phone>
                        </PhoneNumber>
                    </Address>
                </SenderInformation>
                <ReceiverInformation>
                    <Address>
                        <Name>Aaron Summer</Name>
                        <StreetName>Douglas Road</StreetName>
                        <City>Burnaby</City>
                        <Province>BC</Province>
                        <Country>CA</Country>
                        <PostalCode>V5C5A9</PostalCode>
                        <PhoneNumber>
                            <Phone>2982181</Phone>
                        </PhoneNumber>
                    </Address>
                </ReceiverInformation>
                <ShipmentDate>{str(datetime.now().strftime("%Y-%m-%d"))}</ShipmentDate>
                <PackageInformation>
                    <ServiceID>PurolatorExpress</ServiceID>
                    <TotalWeight>
                        <Value>10</Value>
                        <WeightUnit>lb</WeightUnit>
                    </TotalWeight>
                    <TotalPieces>1</TotalPieces>
                    <PiecesInformation>
                        <Piece>
                            <Weight>
                                <Value>7.</Value>
                                <WeightUnit>lb</WeightUnit>
                            </Weight>
                        </Piece>
                    </PiecesInformation>
                </PackageInformation>
                <PickupInformation>
                    <PickupType>DropOff</PickupType>
                </PickupInformation>
                <TrackingReferenceInformation>
                    <Reference1>Reference For Shipment</Reference1>
                </TrackingReferenceInformation>
            </Shipment>
            <ShowAlternativeServicesIndicator>true</ShowAlternativeServicesIndicator>
        </ns1:GetFullEstimateRequest>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""

RATE_RESPONSE_XML = """<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
    <s:Header>
        <h:ResponseContext xmlns:h="http://purolator.com/pws/datatypes/v1" 
            xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
            <h:ResponseReference>Rating Example</h:ResponseReference>
        </h:ResponseContext>
    </s:Header>
    <s:Body>
        <GetFullEstimateResponse xmlns="http://purolator.com/pws/datatypes/v1" 
            xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
            <ResponseInformation>
                <Errors/>
                <InformationalMessages i:nil="true"/>
            </ResponseInformation>
            <ShipmentEstimates>
                <ShipmentEstimate>
                    <ServiceID>PurolatorExpress9AM</ServiceID>
                    <ShipmentDate>2009-04-16</ShipmentDate>
                    <ExpectedDeliveryDate>2009-04-17</ExpectedDeliveryDate>
                    <EstimatedTransitDays>1</EstimatedTransitDays>
                    <BasePrice>62.35</BasePrice>
                    <Surcharges>
                        <Surcharge>
                            <Amount>1.85</Amount>
                            <Type>ResidentialDelivery</Type>
                            <Description>Residential Delivery</Description>
                        </Surcharge>
                        <Surcharge>
                            <Amount>2.81</Amount>
                            <Type>Fuel</Type>
                            <Description>Fuel</Description>
                        </Surcharge>
                    </Surcharges>
                    <Taxes>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>PSTQST</Type>
                            <Description>PST/QST</Description>
                        </Tax>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>HST</Type>
                            <Description>HST</Description>
                        </Tax>
                        <Tax>
                            <Amount>5.15</Amount>
                            <Type>GST</Type>
                            <Description>GST</Description>
                        </Tax>
                    </Taxes>
                    <OptionPrices>
                        <OptionPrice>
                            <Amount>36</Amount>
                            <ID>DangerousGoodsClass</ID>
                            <Description>Dangerous Goods Classification</Description>
                        </OptionPrice>
                    </OptionPrices>
                    <TotalPrice>108.16</TotalPrice>
                </ShipmentEstimate>
                <ShipmentEstimate>
                    <ServiceID>PurolatorExpress10:30AM</ServiceID>
                    <ShipmentDate>2009-04-16</ShipmentDate>
                    <ExpectedDeliveryDate>2009-04-17</ExpectedDeliveryDate>
                    <EstimatedTransitDays>1</EstimatedTransitDays>
                    <BasePrice>55</BasePrice>
                    <Surcharges>
                        <Surcharge>
                            <Amount>1.85</Amount>
                            <Type>ResidentialDelivery</Type>
                            <Description>Residential Delivery</Description>
                        </Surcharge>
                        <Surcharge>
                            <Amount>2.48</Amount>
                            <Type>Fuel</Type>
                            <Description>Fuel</Description>
                        </Surcharge>
                    </Surcharges>
                    <Taxes>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>PSTQST</Type>
                            <Description>PST/QST</Description>
                        </Tax>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>HST</Type>
                            <Description>HST</Description>
                        </Tax>
                        <Tax>
                            <Amount>4.77</Amount>
                            <Type>GST</Type>
                            <Description>GST</Description>
                        </Tax>
                    </Taxes>
                    <OptionPrices>
                        <OptionPrice>
                            <Amount>36</Amount>
                            <ID>DangerousGoodsClass</ID>
                            <Description>Dangerous Goods Classification</Description>
                        </OptionPrice>
                    </OptionPrices>
                    <TotalPrice>100.1</TotalPrice>
                </ShipmentEstimate>
                <ShipmentEstimate>
                    <ServiceID>PurolatorExpress</ServiceID>
                    <ShipmentDate>2009-04-16</ShipmentDate>
                    <ExpectedDeliveryDate>2009-04-17</ExpectedDeliveryDate>
                    <EstimatedTransitDays>1</EstimatedTransitDays>
                    <BasePrice>46.15</BasePrice>
                    <Surcharges>
                        <Surcharge>
                            <Amount>1.85</Amount>
                            <Type>ResidentialDelivery</Type>
                            <Description>Residential Delivery</Description>
                        </Surcharge>
                        <Surcharge>
                            <Amount>2.08</Amount>
                            <Type>Fuel</Type>
                            <Description>Fuel</Description>
                        </Surcharge>
                    </Surcharges>
                    <Taxes>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>PSTQST</Type>
                            <Description>PST/QST</Description>
                        </Tax>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>HST</Type>
                            <Description>HST</Description>
                        </Tax>
                        <Tax>
                            <Amount>4.3</Amount>
                            <Type>GST</Type>
                            <Description>GST</Description>
                        </Tax>
                    </Taxes>
                    <OptionPrices>
                        <OptionPrice>
                            <Amount>36</Amount>
                            <ID>DangerousGoodsClass</ID>
                            <Description>Dangerous Goods Classification</Description>
                        </OptionPrice>
                    </OptionPrices>
                    <TotalPrice>90.38</TotalPrice>
                </ShipmentEstimate>
                <ShipmentEstimate>
                    <ServiceID>PurolatorGround</ServiceID>
                    <ShipmentDate>2009-04-16</ShipmentDate>
                    <ExpectedDeliveryDate>2009-04-22</ExpectedDeliveryDate>
                    <EstimatedTransitDays>4</EstimatedTransitDays>
                    <BasePrice>29.6</BasePrice>
                    <Surcharges>
                        <Surcharge>
                            <Amount>1.85</Amount>
                            <Type>ResidentialDelivery</Type>
                            <Description>Residential Delivery</Description>
                        </Surcharge>
                        <Surcharge>
                            <Amount>1.33</Amount>
                            <Type>Fuel</Type>
                            <Description>Fuel</Description>
                        </Surcharge>
                    </Surcharges>
                    <Taxes>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>PSTQST</Type>
                            <Description>PST/QST</Description>
                        </Tax>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>HST</Type>
                            <Description>HST</Description>
                        </Tax>
                        <Tax>
                            <Amount>3.44</Amount>
                            <Type>GST</Type>
                            <Description>GST</Description>
                        </Tax>
                    </Taxes>
                    <OptionPrices>
                        <OptionPrice>
                            <Amount>36</Amount>
                            <ID>DangerousGoodsClass</ID>
                            <Description>Dangerous Goods Classification</Description>
                        </OptionPrice>
                    </OptionPrices>
                    <TotalPrice>72.22</TotalPrice>
                </ShipmentEstimate>
                <ShipmentEstimate>
                    <ServiceID>PurolatorGround</ServiceID>
                    <ShipmentDate>2009-04-16</ShipmentDate>
                    <ExpectedDeliveryDate>2009-04-22</ExpectedDeliveryDate>
                    <EstimatedTransitDays>4</EstimatedTransitDays>
                    <BasePrice>87.69</BasePrice>
                    <Surcharges>
                        <Surcharge>
                            <Amount>1.85</Amount>
                            <Type>ResidentialDelivery</Type>
                            <Description>Residential Delivery</Description>
                        </Surcharge>
                        <Surcharge>
                            <Amount>3.95</Amount>
                            <Type>Fuel</Type>
                            <Description>Fuel</Description>
                        </Surcharge>
                    </Surcharges>
                    <Taxes>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>PSTQST</Type>
                            <Description>PST/QST</Description>
                        </Tax>
                        <Tax>
                            <Amount>0</Amount>
                            <Type>HST</Type>
                            <Description>HST</Description>
                        </Tax>
                        <Tax>
                            <Amount>6.47</Amount>
                            <Type>GST</Type>
                            <Description>GST</Description>
                        </Tax>
                    </Taxes>
                    <OptionPrices>
                        <OptionPrice>
                            <Amount>36</Amount>
                            <ID>DangerousGoodsClass</ID>
                            <Description>Dangerous Goods Classification</Description>
                        </OptionPrice>
                    </OptionPrices>
                    <TotalPrice>135.96</TotalPrice>
                </ShipmentEstimate>
            </ShipmentEstimates>
            <ReturnShipmentEstimates i:nil="true"/>
        </GetFullEstimateResponse>
    </s:Body>
</s:Envelope>
"""
