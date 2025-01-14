SCHEMAS=./schemas
LIB_MODULES=./canadapost_lib
find "${LIB_MODULES}" -name "*.py" -exec rm -r {} \;
touch "${LIB_MODULES}/__init__.py"


generateDS --no-namespace-defs -o "${LIB_MODULES}/authreturn.py" $SCHEMAS/authreturn.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/common.py" $SCHEMAS/common.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/customerinfo.py" $SCHEMAS/customerinfo.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/discovery.py" $SCHEMAS/discovery.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/manifest.py" $SCHEMAS/manifest.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/merchantregistration.py" $SCHEMAS/merchantregistration.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/messages.py" $SCHEMAS/messages.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/ncshipment.py" $SCHEMAS/ncshipment.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/openreturn.py" $SCHEMAS/openreturn.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/pickup.py" $SCHEMAS/pickup.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/pickuprequest.py" $SCHEMAS/pickuprequest.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/postoffice.py" $SCHEMAS/postoffice.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/rating.py" $SCHEMAS/rating.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/serviceinfo.py" $SCHEMAS/serviceinfo.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/shipment.py" $SCHEMAS/shipment.xsd
generateDS --no-namespace-defs -o "${LIB_MODULES}/track.py" $SCHEMAS/track.xsd
