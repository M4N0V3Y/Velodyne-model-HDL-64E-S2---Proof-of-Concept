# Usage of Velodyne Lidar with  Python

This code currently supports model HDL 64E S2 only.

*** You can download 'maccdc2012_00011.pcap' from [maccdc2012_00011.pcap](https://download.netresec.com/pcap/maccdc-2012/)
## Table of Contents
1. [Prerequisites](#Prerequisites)
2. [Calibration Data generation](#calibration_from_pcap)
3. [Point Cloud generation](#point_cloud_from_pcap.py)
4. [Visualization](#velodyne_view)
5. [Intructions for vizualization](#intructions-for-vizualization)

## Prerequisites

Python, tested with Python 3.5

```bash 
$ pip install dpkt
$ pip install json
$ pip install msgpack
$ pip install pyglet
$ pip3 install -U tqdm
```

## Calibration Data generation

Calibration data is generated from PCAP file and stored in a JSON file for all further usage.
Point Cloud data is readed from PCAP using calibration JSON file as reference and written in .LAZ file.

To read from the PCAP use:
The `calibration_from_pcap.py` generates a JSON calibration file from provided PCAP file.

```bash 
$ python calibration_from_pcap.py <FILE.PCAP> <CALIBRATION.JSON>
```

## Point Cloud generation
The `point_cloud_from_pcap.py` converts a pcap trace into a msgpack file holding the measurement points
using a message pack data file as an array of 3-tupels (x,y,z).
To extract point cloud use:

```bash
$ python point_cloud_from_pcap.py <FILE.PCAP> <POINT_CLOUD.LAZ> <CALIBRATION.JSON>
```

## Visualization

The `velodyne_view.py` program visualizes the message pack points file:

```bash
$ python visualize.py msgpack <POINT_CLOUD.LAZ> <start_point_index> <end_point_index>
```

Is possible to narrow down the number of plotted points by using <start_point_index> and <end_point_index> to about one revolution of the lidar.

### Intructions for vizualization:
```
$ Use <cursor keys> to rotate the view, 
$ <shift> + cursor keys to pan, 
$ <ctrl> +<up> and <ctrl>+<down> to zoom
$ Click on a point to mark it and output it's 3d coordiantes.
$ Click on a second point to output the distance from the first point.

```
### The MIT License (MIT)

Copyright (c) 2017 E.S.R. Labs AG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
