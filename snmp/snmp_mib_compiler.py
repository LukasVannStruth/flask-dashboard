from pysmi.reader import FileReader
from pysmi.searcher import PyFileSearcher, PyPackageSearcher, StubSearcher
from pysmi.writer import PyFileWriter
from pysmi.parser import SmiStarParser
from pysmi.codegen import PySnmpCodeGen
from pysmi.compiler import MibCompiler

inputMibs = ["FORTINET-CORE-MIB.mib","FORTINET-FORTIGATE-MIB.mib",  "IF-MIB", "IP-MIB"]
srcDirectories = ["/home/lukas/lvs-dev/learning-jenkins/flask-dashboard/mibs"]
dstDirectory = ".pysnmp-mibs"

# https://docs.lextudio.com/pysmi/examples/compile-smistar-mibs-into-pysnmp-files-if-needed

# Initialize compiler infrastructure

mibCompiler = MibCompiler(SmiStarParser(), PySnmpCodeGen(), PyFileWriter(dstDirectory))

# search for source MIBs here
mibCompiler.add_sources(*[FileReader(x) for x in srcDirectories])

# check compiled MIBs in our own productions
mibCompiler.add_searchers(PyFileSearcher(dstDirectory))
# ...and at default PySNMP MIBs packages
mibCompiler.add_searchers(
    *[PyPackageSearcher(x) for x in PySnmpCodeGen.defaultMibPackages]
)

# never recompile MIBs with MACROs
mibCompiler.add_searchers(StubSearcher(*PySnmpCodeGen.baseMibs))

# run [possibly recursive] MIB compilation
results = mibCompiler.compile(*inputMibs)  # , rebuild=True, genTexts=True)

print(f"Results: {', '.join(f'{x}:{results[x]}' for x in results)}")