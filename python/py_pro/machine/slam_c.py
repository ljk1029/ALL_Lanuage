import numpy as np
import cv2

# 机器人初始位姿
robot_x = 0
robot_y = 0
robot_theta = 0

# 地图中的特征点
landmarks = np.array([[5, 5], [10, 5], [7, 10]])

# 状态向量(机器人位姿 + 特征点位置)
state = np.r_[robot_x, robot_y, robot_theta, landmarks.flatten()]

# 协方差矩阵
cov = np.eye(3 + landmarks.size)

# 运动噪声
motion_noise = np.diag([0.1, 0.1, 0.01])

# 观测噪声
observation_noise = np.diag([0.1, 0.1])

# EKF-SLAM迭代
for i in range(10):
    # 模拟机器人运动
    robot_x += 1
    robot_y += 05
    robot_theta += 0.1

    # 预步骤
    robot_state = np.array([robot_x,_y, robot_theta])
    state_pred = np.r_[robot_state, state[3:]]
    cov_pred = cov + motion_noise

    # 观步骤
    observations = []
    for lm in landmarks:
        dx = l[0] - robot_x
        dy = lm[1] - robot_y
        r = np.sqrt(dx**2 + dy**2)
        phi = np.arctan2(dy, dx) - robot_
        observationsappend(np.array([r, phi]))

    observations = np.array(observations

    # 更新步骤
    for obs, lm in zip(observations, landmarks):
        H = np.zeros((2, 3 + landmarks.size))
        H[:, :3] = np.array[-np.cos(robot_theta), -np.sin(robot_theta), 0],
                             [np.sin(robot_theta), -np.cos(robot_theta), -1]])
        H[:, 3 + lmtolist()] = np.array([[np.cos(robot_theta),.sinrobot_theta)],
                                          [-np.sin(robot_theta), np.cos(robot_theta)]])

        K = cov_pred @ H.T @ np.linalg.inv(H @ cov_pred @ H.T + observation_noise)
        state = state_pred + K @ (obs - np.array([np.sqrt((lm[0] - robot_x)**2 + (lm[1] - robot_y)**2),
                                                  np.tan2(lm[1] - robot_y, lm[0] - robot_x) - robot_theta]))
        c = (np.eye(cov_pred.shape[0]) - K @ H) @ cov_pred

    # 可视化
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    for lm in landmarks:
        cv2circle(img, (int(lm[0]) * 20  250, int(lm[1]) * 20 + 250), 5, (0, 0, 255), -1)
    cv2.circle(img, (int(state[0]) * 20 + 250, int(state[]) * 20 + 250), 5, (0, 255, 0), -1)
    cv2.imshow('EKF-SLAM', img)
    cv2.waitKey(100)

cv2.destroyAllWindows
```这个示例中,我们首先定义了机器人的初始位姿、地图中的特征点以及EKF-SLAM所需的噪声参数。然后进入EKF-SLAM的迭代循环:

1.模拟机器人运动,更新机器人真实位姿。
2. 预测步骤:根据机器人运动,预测的状态向量和协方差矩阵。
3. 观测步骤:根据特征点的真实位置,模拟观测数据。
4. 更新步骤:使用扩展卡尔曼波器,根据观测数据更新状态向量和协方差矩阵的估计值。
5. 可视化:在OpenCV窗口中显机器和地图特征点的位置。

运行这个示,你会看到一个OpenCV窗口,其中有三个色圆点代表地图中的特征点,一个绿色圆点代表机器人的估计位置。随着机器人的运动,绿色圆点会实时更新,反映EKF-SLAM对机器人位姿和地图的计。

需要注意的是,这只是一个简化的EKF-SLAM实现,缺少了一些关键组件,如数据关联、闭环检测和图优化等。在实际应用中,还需要处理这些问题,以提高SLAM算法的鲁棒性和精度。但这个示例可以帮助你理解EKF-SLAM的基本工作原理。