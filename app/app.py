from quart import Quart, render_template, url_for, request, websocket
import os
import asyncio
import json

from .snmp import instantiate_mibs
from .snmp.get_cmd import run_cmd

#app = Flask(__name__)

template_dir = os.path.join(os.getcwd(), 'templates')
index_file = os.path.join(template_dir, 'index.html')


envvars = {}
__version__ = "0.1.0a"

app = Quart(__name__)

mib_view_ctrl = instantiate_mibs()



@app.route("/")
async def render_index():


    # setup paths for files
    stylefile_path = url_for('static', filename='styles.css')
    ws_url = url_for('ws')
    # define envvars for the page
    envvars["stylesheet"] = stylefile_path 
    envvars["version"] = __version__
    envvars["ws_url"] = ws_url


    return await render_template('index.html', envvars=envvars, FGT_SN=None)

async def ws_tx():
    while True:
        await websocket.send('test')


async def ws_rx():
    while True:
        data = await websocket.receive()
        print(data)

@app.websocket('/ws')
async def ws():
    try:
        producer = asyncio.create_task(ws_tx())
        consumer = asyncio.create_task(ws_rx())
        print('ws triggered')
        await asyncio.gather(producer, consumer)
    except asyncio.CancelledError:
        raise asyncio.CancelledError
    
## todo add validation with quart-schema
@app.get("/snmp/fgt_sn")
async def retrieve_fgt_sn():
    oid = ".1.3.6.1.4.1.12356.100.1.1.1.0"
    fgt_sn = await run_cmd(oid, mib_view_ctrl)
    jsons = f'{{"fgt_sn": "{fgt_sn}"}}' 
    print(jsons)
    return json.loads(jsons)





app.run()