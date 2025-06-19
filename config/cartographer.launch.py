from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_dir = get_package_share_directory('MATRO_NB')
    config_dir = os.path.join(pkg_dir, 'config')
    rviz_config_file = os.path.join(pkg_dir, 'rviz', 'cartographer_slam.rviz')  # ✅ RViz 설정파일 경로

    return LaunchDescription([
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[{
                'use_sim_time': False,
            }],
            arguments=[
                '-configuration_directory', config_dir,
                '-configuration_basename', 'cartographer.lua'
            ],
            remappings=[
                ('/scan', '/scan'),
                ('/odom', '/odom'),
            ]
        ),
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            name='occupancy_grid_node',
            output='screen',
            parameters=[{'use_sim_time': False}]
        ),
        Node(  # ✅ RViz 실행 노드
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_file]
        )
    ])
