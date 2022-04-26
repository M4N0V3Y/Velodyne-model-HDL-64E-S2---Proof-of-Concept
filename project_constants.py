#!/usr/bin/env python
# encoding: utf-8
"""
Constants.py
"""

def get_sys_args(_argv,msg):
    if len(_argv)==3:
        return _argv[1], _argv[2], _argv[3]
    elif len(_argv)==2:
        return _argv[1], _argv[2]
    else:
        print(msg.format(sys.argv[0]))
        exit()

MY_CONSTANT_ONE = 50
MY_CONSTANT_TWO = 51

MESSAGE_SAVE_CALIBRATION='writing calibration to '
POINT_CLOUD_FROM_PCAP_USAGE='usage: python {} <pcap_file> <out_file> <cal_file>'
CALIBRATION_FROM_PCAP_USAGE='usage: python {} <pcap_file> <out_file>'
MSG_USING_CALIBRATION_FILE ='using calibration file '
MSG_READING_PCKG_FROM='reading packets from '
MSG_PROSS_EACH_FRAME ='processing each frame: ' 
MSG_WRITING_DATA_TO='writing data to '
MSG_READING_CALIBRATION = 'Reading calibration from PCAP file: '
VERT_CORRECTION                 ='vertical_correction'
ROTA_CORRECTION                 ='rotational_correction'
DIST_FAR_CORRECTION             ='distance_far_correction'
DIST_CORRECTION_X               ='distance_correction_x'
DIST_CORRECTION_Y               ='distance_correction_y'
VERT_OFFSET_CORRECTION          ='vertical_offset_correction'
HORI_OFFSET_CORRECTION          ='horizontal_offset_correction'
FOCAL_DISTANCE                  ='focal_distance'
FOCAL_SLOPE                     ='focal_slope'
MIN_INTENSITY                   ='min_intensity'
MAX_INTENSITY                   ='max_intensity'
#
COS_VERT_CORR      = '_cos_vert_corr'
SIN_VERT_CORR      = '_sin_vert_corr'
COS_ROT_CORR       = '_cos_rot_corr'
SIN_ROT_CORR       = '_sin_rot_corr'
HOR_OFF_CORR       = '_hor_off_corr'
VERT_OFF_CORR      = '_vert_off_corr'
DIST_CORR_X_FACT   = '_dist_corr_x_fact'
DIST_CORR_Y_FACT   = '_dist_corr_y_fact'