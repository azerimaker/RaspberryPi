import os
import glob
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import datetime 
import time

# Plotly api key and token
username = 'your_username'
api_key = 'your_api_key'
stream_token = 'your_stream_token'

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=3000
   )
)

layout = Layout(
    title = 'Raspberry Pi Streaming Temperature Sensor Data'
)

fig = Figure(data=[trace1], layout=layout)
print py.plot(fig, filename='Raspberry Pi Streaming Example values')

stream = py.Stream(stream_token)
stream.open()

# sensor related 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

#try:
i = 0

while True:
    now = datetime.datetime.now()
    deg_c, deg_f = read_temp()
    stream.write({'x':now,'y':deg_c})
    i += 1
    #print str(now)
    #print "C:  %s, F: %s" %(deg_c, deg_f)
    time.sleep(60)

#except:
#    print "unknown error"
#    exit(-1)
