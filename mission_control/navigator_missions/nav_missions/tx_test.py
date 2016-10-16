#!/usr/bin/env python
import txros
from geometry_msgs.msg import PoseStamped


@txros.util.cancellableInlineCallbacks
def main(navigator):
    ps = PoseStamped()
    ps.header.frame_id = "enu"
    pub = navigator.latching_publisher('/test', PoseStamped, ps)

    yield navigator.nh.sleep(5)

    # This seems to throw an error after the mission execution.
    # Everything still works without it.
    #pub.cancel()

    print "Done!"