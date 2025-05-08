from pysnmp.smi import builder, view

__version__ = "0.1.0a"




def instantiate_mibs():
    mib_builder = builder.MibBuilder()
    mib_builder.add_mib_sources(builder.DirMibSource("/home/lukas/lvs-dev/learning-jenkins/flask-dashboard/app/compiled_mibs"))
    mib_builder.load_module('FORTINET-CORE-MIB')
    mib_view_controller = view.MibViewController(mib_builder)
    return mib_view_controller
