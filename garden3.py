from time import sleep
from math import isnan
import time
import sys
import datetime
import subprocess
import sys
import os
import datetime
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import psutil
import base64
import uuid
import socket 
from sgp30 import SGP30
import pulsar
from pulsar.schema import *

### Schema Object
# https://pulsar.apache.org/docs/en/client-libraries-python/
# https://pulsar.apache.org/api/python/

class Garden(Record):
    cpu = Float()
    diskusage = String()
    endtime = String()
    equivalentco2ppm = String()
    host = String()
    hostname = String()
    ipaddress = String()
    macaddress = String()
    memory = Float()
    rowid = String()
    runtime = Integer()
    starttime = String()
    systemtime = String()
    totalvocppb = String()
    ts = Integer()
    uuid = String()

sgp30 = SGP30()
sgp30.start_measurement()

external_IP_and_port = ('198.41.0.4', 53)  # a.root-servers.net
socket_family = socket.AF_INET

def IP_address():
        try:
            s = socket.socket(socket_family, socket.SOCK_DGRAM)
            s.connect(external_IP_and_port)
            answer = s.getsockname()
            s.close()
            return answer[0] if answer else None
        except socket.error:
            return None

# Get MAC address of a local interfaces
def psutil_iface(iface):
    # type: (str) -> Optional[str]
    import psutil
    nics = psutil.net_if_addrs()
    if iface in nics:
        nic = nics[iface]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address
# Random Word
def randomword(length):
 return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()) for i in range(length))

# Fixed
packet_size=3000
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ipaddress = IP_address()

# pulsar
client = pulsar.Client('pulsar://pulsar1:6650')
producer = client.create_producer(topic='persistent://public/default/garden3' ,schema=JsonSchema(Garden),properties={"producer-name": "garden3-py-sensor","producer-id": "garden3-sensor" })

try:
    while True:
        currenttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        starttime = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        start = time.time()
        uniqueid = 'garden3_uuid_{0}_{1}'.format(randomword(3),strftime("%Y%m%d%H%M%S",gmtime()))
        uuid2 = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
        result = sgp30.get_air_quality()
        usage = psutil.disk_usage("/")
        end = time.time()

        gardenRec = Garden()
        gardenRec.cpu = psutil.cpu_percent(interval=1)
        gardenRec.diskusage = "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
        gardenRec.endtime  = '{0}'.format(str(end))
        gardenRec.equivalentco2ppm = '{:5d}'.format( (result.equivalent_co2))
        gardenRec.host  = os.uname()[1]
        gardenRec.hostname  = host_name
        gardenRec.ipaddress = ipaddress
        gardenRec.macaddress  = psutil_iface('wlan0')
        gardenRec.memory = psutil.virtual_memory().percent
        gardenRec.rowid =  str(uuid2)
        gardenRec.runtime  = int(round(end - start)) 
        gardenRec.systemtime = str(datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S'))
        gardenRec.totalvocppb = '{0:3d}'.format(result.total_voc)
        gardenRec.ts =  int(time.time())
        gardenRec.uuid = str(uniqueid)
        gardenRec.runtime =  int(round(end - start)) 
        gardenRec.starttime = str(starttime)

        fa=open("/opt/demo/logs/gardenrec.log", "a+")
        fa.write(str(gardenRec) + "\n")
        fa.close()

        print(gardenRec)

        producer.send(gardenRec,partition_key=str(uniqueid))
except KeyboardInterrupt:
    pass

client.close()