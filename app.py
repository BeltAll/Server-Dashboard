import os
from socket import gethostbyname, gethostname

import psutil as pu
from flask import Flask, render_template

app=Flask(__name__)


# flask
@app.route("/")
def home():
	if getStats() == True:
		return render_template(
		"index.html",
		server1_cpu_usage=server1_cpu_usage,
		server1_cpu_temp=server1_cpu_temp,
		server1_ram_usage=server1_ram_usage,
		server1_disk_usage=server1_disk_usage,
		server1_download_speed=server1_download_speed,
		server1_upload_speed=server1_upload_speed,
		server1_local_ip=server1_local_ip,
		server1_storage1_avail=server1_storage1_avail,
		server1_storage1_total=server1_storage1_total,
		server1_storage1_percent=server1_storage1_percent,
		server1_storage2_avail=server1_storage2_avail,
		server1_storage2_total=server1_storage2_total,
		server1_storage2_percent=server1_storage2_percent,
		server1_ssh_status=server1_ssh_status,
		server1_nginx_status=server1_nginx_status,
		server2_wireguard_status=server2_wireguard_status,
		dashboard_status=dashboard_status,
		subnetcalc_status=subnetcalc_status,
		shortcut_status=shortcut_status
		)

# helper functions

# main functions
def getInternalStats():
	global server1_cpu_usage, server1_cpu_temp, server1_ram_usage, server1_disk_usage, server1_download_speed, server1_upload_speed, server1_local_ip, server1_storage1_avail, server1_storage1_total, server1_storage1_percent, server1_storage2_avail, server1_storage2_total, server1_storage2_percent, server1_ssh_status, server1_nginx_status, dashboard_status, subnetcalc_status, shortcut_status
	server1_cpu_usage=pu.cpu_percent(interval=1)
	if os.name=="nt":
		server1_cpu_temp="uwu windows"
	else:
		temps=pu.sensors_temperatures(False)
		server1_cpu_temp=temps["k10temp"] # [shwtemp(label='Tctl', current=37.75, high=None, critical=None)]
	ram_stats=pu.virtual_memory()
	server1_ram_usage=ram_stats.percent
	server1_disk_usage=0
	server1_download_speed=0
	server1_upload_speed=0
	server1_local_ip=gethostbyname(gethostname())
	server1_storage1_avail=0
	server1_storage1_total=0
	server1_storage1_percent=0
	server1_storage2_avail=0
	server1_storage2_total=0
	server1_storage2_percent=0
	server1_ssh_status=0
	server1_nginx_status=0
	dashboard_status=0
	subnetcalc_status=0
	shortcut_status=0


def getExternalStats():
	global server2_wireguard_status
	server2_wireguard_status=0


def getStats():
	getInternalStats()
	getExternalStats()
	return True

if __name__ == "__main__":
   app.run(debug=False)