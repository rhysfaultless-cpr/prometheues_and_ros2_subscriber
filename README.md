# prometheues_and_ros2_subscriber

## background

This package requires the [air_velocity_measurement_fs3000_1015](https://github.com/rhysfaultless-cpr/air_velocity_measurement_fs3000_1015) package, and related hardware.
Note that the ros 2 package contained in the *prometheus_and_ros2_subscriber* was quickly put together, so the dependencies and tests may not be corrct.
This was also developed for a simple concept, so this README should not be considered a complete How-To-Guide.

## purpose

1.  Subscribe to the ROS 2 topic: *air_velocity_measurement*.
2.  Push the *Int16* data from this topic to Prometheus using their *prometheus_client* library's tools on port 8001.

## configure and launch

1.  Configure and start the Prometheus server.
2.  Add this repository to ~/ros2_ws/src
3.  Build the workspace
4.  Source the workspace
5.  Launch the node with the command `ros2 launch subscribe_and_push subscribe_and_push_launch.py`
