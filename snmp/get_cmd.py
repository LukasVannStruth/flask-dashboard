import asyncio
from pysnmp.hlapi.v3arch.asyncio import *
from pysnmp.smi import builder, view
from pysmi import debug
import os



# debug.set_logger(debug.Debug('searcher', 'reader', 'compiler', 'parser'))


'''
ifInOctets = ObjectType(ObjectIdentity(
    'FORTINET-CORE', 'ifInOctets', 1
    ).add_asn1_mib_source(
        'file://'
    )
)
'''

mib_builder = builder.MibBuilder()
mib_builder.add_mib_sources(builder.DirMibSource("/home/lukas/lvs-dev/learning-jenkins/flask-dashboard/compiled_mibs"))
mib_builder.load_module('FORTINET-CORE-MIB')
mib_view_controller = view.MibViewController(mib_builder)

async def run_cmd(mib_oid):
    snmpEngine = SnmpEngine()
#   object =  ObjectIdentity(mib, oid).add_asn1_mib_source("file:///home/lukas/lvs-dev/learning-jenkins/flask-dashboard/mibs", "http://mibs.snmplabs.com/asn1/@mib@")
#   object =  ObjectIdentity(mib, oid).add_mib_source("file:///home/lukas/lvs-dev/learning-jenkins/flask-dashboard/mibs", "http://mibs.snmplabs.com/asn1/@mib@")

    snmpEngine.cache["mibViewController"] = mib_view_controller
    object =  ObjectIdentity(mib_oid)

#   object.add_asn1_mib_source("file:///home/lukas/lvs-dev/learning-jenkins/flask-dashboard/mibs", "http://mibs.snmplabs.com/asn1/@mib@")

    errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
        snmpEngine,
        CommunityData("lukas"),
        await UdpTransportTarget.create(("10.0.0.1", 161)),
        ContextData(),
        ObjectType(object),
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

        for item in varBinds:
            x = 0
            for y in item: 
                print(f'value at index {x} is {y}') 
                x = x + 1 

        print(f'Retrieved value for OID {varBinds[0][0].prettyPrint()} is: {varBinds[0][1]}')
#       print(varBinds[0].prettyPrint())
        return varBinds[0][1]

#       return varBinds.prettyPrint()
#       for varBind in varBinds:

#           return varbind
#           print(" = ".join([x.prettyPrint() for x in varBind]))

# asyncio.run(run_cmd(oid))