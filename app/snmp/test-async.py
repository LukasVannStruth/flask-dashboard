from get_cmd import run_cmd
from __init__ import fcore_mib, fgt_mib
import asyncio

oid = ".1.3.6.1.4.1.12356.100.1.1.1.0"

async def main():
    result = await run_cmd(oid)
    print(result)


asyncio.run(main())
