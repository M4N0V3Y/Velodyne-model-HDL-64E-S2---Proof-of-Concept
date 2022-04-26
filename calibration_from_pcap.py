import json
import pprint
import sys
import dpkt
import project_constants
import time
from tqdm import tqdm
from velodyne import StatusState, process_frame, calc_coords
#
def fdata_callback(laser_idx, rot_pos, dist, intensity):
  pass
#
def generate_output_json(status,out_file):
    output_calibration = [status.lasers[l].values for l in range(64)]
    print(project_constants.MESSAGE_SAVE_CALIBRATION+out_file)
    with open(out_file, 'w') as f:
      json.dump(output_calibration, f, sort_keys=True, indent=4)
#      
in_file, out_file = project_constants.get_sys_args(sys.argv, project_constants.CALIBRATION_FROM_PCAP_USAGE)
#
status = StatusState()
print(project_constants.MSG_READING_CALIBRATION+in_file)
#
with open(in_file, 'rb') as f:
  reader = dpkt.pcap.Reader(f)  
  for ts, buf in tqdm(reader):
    eth = dpkt.ethernet.Ethernet(buf)
    data = eth.data.data.data
    process_frame(data, 0, status, fdata_callback)
    if len(status.lasers[63].values) > 0:
      break
#
generate_output_json(status,out_file)

