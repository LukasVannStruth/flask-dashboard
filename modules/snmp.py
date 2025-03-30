import asyncio
from pysnmp.hlapi.v3arch.asyncio import *
from pysnmp.smi import builder
import os


# Grab the Fortinet MIBs


'''
ifInOctets = ObjectType(ObjectIdentity(
    'FORTINET-CORE', 'ifInOctets', 1
    ).add_asn1_mib_source(
        'file://'
    )
)
'''

async def run():
    snmpEngine = SnmpEngine()
    errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
        snmpEngine,
        CommunityData("lukas"),
        await UdpTransportTarget.create(("10.0.0.1", 161)),
        ContextData(),
        ObjectType(
            ObjectIdentity("IF-MIB", "ifInOctets", 1).add_asn1_mib_source(
                "/home/lukas/lvs-dev/learning-jenkins/flask-dashboard/mibs"
            )
        ),
    )



    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(
            "{} at {}".format(
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
            )
        )
    else:
        for varBind in varBinds:
            print(" = ".join([x.prettyPrint() for x in varBind]))


asyncio.run(run())