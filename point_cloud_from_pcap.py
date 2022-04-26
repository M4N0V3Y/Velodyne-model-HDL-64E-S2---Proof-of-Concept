import msgpack
import sys
import dpkt
import json
import time
from tqdm import tqdm
import project_constants
from velodyne import StatusState, process_frame, calc_coords
#
def firing_data_callback(laser_idx, ROT_podition, dist, intensity):
  values = calibration_vals[laser_idx]
  coords = calc_coords(dist, ROT_podition, values)
  if coords != (0, 0, 0):
    output_points.append(coords)
#
in_pcap_file, out_point_cloud_file, cal_file = project_constants.get_sys_args(sys.argv,project_constants.POINT_CLOUD_FROM_PCAP_USAGE)
output_points = []
status = StatusState()

print(project_constants.MSG_USING_CALIBRATION_FILE+cal_file)
with open(cal_file, 'r') as f:
  calibration_vals = json.load(f)

print(project_constants.MSG_READING_PCKG_FROM+in_pcap_file)
with open(in_pcap_file, 'rb') as f:
  reader = dpkt.pcap.Reader(f)

  frame_index = 0
  last_t = time.time() 

  for ts, buf in tqdm(reader):
    eth = dpkt.ethernet.Ethernet(buf)
    data = eth.data.data.data
    each_frame_process(data, 0, status, firing_data_callback)

    frame_index += 1
    if frame_index % 1000 == 0:
      t = time.time()
      print(project_constants.MSG_PROSS_EACH_FRAME+ str(frame_index) + ' fps: '+str(int(1000/(t - last_t))))
      last_t = t


print(project_constants.MSG_WRITING_DATA_TO+out_point_cloud_file)

with open(out_point_cloud_file, 'wb') as f:
  msgpack.pack(output_points, f)

print('done')
