#!/usr/bin/env python3
# Software License Agreement (BSD)
#
# @author    Rhys Faultless <rfaultless@clearpathrobotics.com>
# @copyright (c) 2024, Clearpath Robotics, Inc., All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Clearpath Robotics nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

from prometheus_client import start_http_server, Summary, Gauge
prometheus_gauge = Gauge('air_speed_in_cm_per_second', 'Value of air speed in cm/s')
prometheus_gauge.set(0)   # Set to a given value


class SubscribeAndPush(Node):
    def __init__(self):
        super().__init__('subscribe_and_push')
        self.subscription = self.create_subscription(
            Int16,
            'air_velocity_measurement',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Subscribed to data from Air Velocity publisher "%s"' % str(msg.data))
        prometheus_gauge.set(msg.data)


def main():
    start_http_server(8001)

    # rclpy.init(args=args)
    rclpy.init()
    subscribe_and_push = SubscribeAndPush()
    rclpy.spin(subscribe_and_push)
    subscribe_and_push.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
