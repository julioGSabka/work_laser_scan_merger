# work_laser_scan_merger

This package is a fork of the ros2_laser_scan_merger package, specifically adapted to meet the requirements of the Cavalo Vendado team's robot for the @Work competition.

It is a full C++ based ROS 2 package designed to merge several LaserScan topics into a new virtual LaserScan topic. Each source can be individually configured via parameters to determine its heading and relative position to the virtual laser scan frame.

## Usage

To run the merger with the Cavalo Vendado @Work configurations:

```bash
ros2 launch work_laser_scan_merger work_scans_merge.launch.py
```

## Available Parameters

All parameters are being set in the `work_params.yaml` file inside the `config` directory.

All parameters similar for the first and second lidar data. The `{x}` marks means the index pattern for the lidar data. Example: `show{x}` means `show1` and `show2` for 2 lidar configuration.

| Parameter Name | Default Value | Description |
|----------------|---------------|-------------|
| scanTopic{x} | /lidar_1/scan <br/> /lidar_2/scan |  laser scan or lidar topic |
| show{x} | true | set as `true` to include the first lidar data or `false` to hide the specific lidar data |
| flip{x} | false | set as `true` for upside down lidar installation |
| laser{x}AngleMax | 180 | maximum angle in degree of the lidar data that are being used for the final merged result, usefull to hide some part of the lidars data. will highly depends on each lidar specification |
| laser{x}AngleMin | -180 | minimum angle in degree of the lidar data that are being used for the final merged result, usefull to hide some part of the lidars data. will highly depends on each lidar specification |
| inverse{x} | false | set as `true` to inverse the hidden lidar data based on the `laser{x}AngleMax` and `laser{x}AngleMin` value |
| laser{x}Alpha | 0 | angular offset of the lidar data |
| laser{x}XOff | -0.3 | linar offset of the lidar data in x axis |
| laser{x}YOff | -0.475 | linar offset of the lidar data in y axis |
| laser{x}ZOff | 0.176 | linar offset of the lidar data in z axis |
| laser{x}B | 0 | set color to the resulted pointclound2 data (0-255) |
| laser{x}G | 0 | set color to the resulted pointclound2 data (0-255) |
| laser{x}R | 255 | set color to the resulted pointclound2 data (0-255) |
| pointCloudTopic | cloud_in | pointcloud2 published topic (adjusted to `pointcloud_to_laserscan` package) |
| pointCloutFrameId | laser | frame id of the pointcloud2 published data |
