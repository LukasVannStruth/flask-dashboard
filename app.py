from quart import Quart, render_template, url_for
import os
import asyncio

from .snmp.get_cmd import run_cmd

#app = Flask(__name__)

template_dir = os.path.join(os.getcwd(), 'templates')
index_file = os.path.join(template_dir, 'index.html')


envvars = {}
__version__ = "0.1.0a"

app = Quart(__name__)

@app.route("/")
async def render_index():
    # setup paths for files
    stylefile_path = url_for('static', filename='styles.css')

    # define envvars for the page
    envvars["stylesheet"] = stylefile_path 
    envvars["version"] = __version__

    oid = ".1.3.6.1.4.1.12356.100.1.1.1.0"

    loop = asyncio.get_event_loop()
    # run snmp query
#   fgt_sn = asyncio.ensure_future(run_cmd(".1.3.6.1.4.1.12356.100.1.1.1.0"))
#   result = loop.run_until_complete(run_cmd(".1.3.6.1.4.1.12356.100.1.1.1.0"))

    fgt_sn = await run_cmd(oid)
    print(fgt_sn)

    return await render_template('index.html', envvars=envvars, FGT_SN=fgt_sn)
    
app.run()