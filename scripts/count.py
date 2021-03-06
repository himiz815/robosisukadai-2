PDX-License-Identifier: GPL-3.0-only
'''
     Copyright (C) 2020  Haruki Shimotori and Ryuichi Ueda. All right reserved.
'''

import rospy
from std_msgs.msg import String

rospy.init_node('count') # ノード名「count」に設定
pub = rospy.Publisher('count_up', String, queue_size=1) # パブリッシャ「count_up」を作成
rate = rospy.Rate(10) # 10Hzで実行

while not rospy.is_shutdown():
    rospy.loginfo("進撃の巨人完結しないで")
    pub.publish()
    rate.sleep()
