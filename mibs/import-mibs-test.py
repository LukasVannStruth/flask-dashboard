from pysnmp.hlapi import SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, getCmd

iterator = getCmd(
    SnmpEngine(),
    CommunityData('rostring', mpModel=1),
    UdpTransportTarget(('192.168.11.201', 161)),
    ContextData(),
    ObjectType(ObjectIdentity(
        'IF-MIB', 'ifInOctets', 1
        ).addAsn1MibSource(
            'file://.'
        )
    )
)

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
