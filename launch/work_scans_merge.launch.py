from launch import LaunchDescription
import launch_ros.actions
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition

from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    use_rviz = LaunchConfiguration('use_rviz')
    use_sim_time = LaunchConfiguration('use_sim_time')

    declare_use_rviz = DeclareLaunchArgument(
        'use_rviz',
        default_value='true',
        description='Decide se o RViz será lançado'
    )
    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Usar /clock (sim time)'
    )

    rviz_config_dir = os.path.join(
        get_package_share_directory('work_laser_scan_merger'),
        'rviz',
        'ros2_laser_scan_merge.rviz'
    )

    config = os.path.join(
        get_package_share_directory('work_laser_scan_merger'),
        'config',
        'work_params.yaml'
    )

    work_scans_merger = launch_ros.actions.Node(
            package='work_laser_scan_merger',
            executable='work_laser_scan_merger',
            parameters=[
                config,
                {'use_sim_time': use_sim_time}
            ],
            output='screen',
            respawn=True,
            respawn_delay=2,
    )

    work_pcl_to_scan = launch_ros.actions.Node(
            name='pointcloud_to_laserscan',
            package='pointcloud_to_laserscan',
            executable='pointcloud_to_laserscan_node',
            parameters=[
                config,
                {'use_sim_time': use_sim_time}
            ],
    )

    rviz_node = launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            output='screen',
            condition=IfCondition(use_rviz)
        )


    return LaunchDescription([   

        declare_use_rviz,
        declare_use_sim_time,
        work_scans_merger,
        work_pcl_to_scan,
        rviz_node
    ])

