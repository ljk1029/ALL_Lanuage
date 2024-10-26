import numpy as np
from math import cos, sin, pi

class Robot:
    def __init__(self):
        # 机器人的位置和协方差
        self.x = np.array([0, 0, 0])  # x, y, theta
        self.P = np.eye(3)

    def move(self, u, dt):
        """
        更新机器人的位置，其中 u 是控制输入，dt 是时间间隔。

        Args:
            u: [v, omega]，其中 v 是线速度，omega 是角速度
            dt: 时间间隔
        """
        F = np.array([[1, 0, -dt * sin(self.x[2])],
                      [0, 1, dt * cos(self.x[2])],
                      [0, 0, 1]])

        B = np.array([[dt * cos(self.x[2]), 0],
                      [dt * sin(self.x[2]), 0],
                      [0, dt]])

        self.x = F @ self.x + B @ u
        self.P = F @ self.P @ F.T + B @ np.diag([0.1, 0.1]) @ B.T

    def observe(self, z):
        """
        使用卡尔曼滤波更新机器人的位置和协方差，其中 z 是观测值。

        Args:
            z: [x, y]，其中的 x 和 y 是地标的坐标
        """
        # 观测模型
        H = np.array([[1, 0, 0],
                      [0, 1, 0]])

        # 创新协方差
        S = H @ self.P @ H.T + np.eye(2) * 0.1

        # 卡尔曼增益
        K = self.P @ H.T @ np.linalg.inv(S)

        # 更新状态
        y = z - H @ self.x
        self.x = self.x + K @ y
        self.P = (np.eye(3) - K @ H) @ self.P

# 创建机器人
robot = Robot()

# 模拟机器人移动和观测
for t in range(100):
    # 控制输入
    u = np.array([0.1, 0.1 * np.sin(t/10)])

    # 更新机器人位置
    robot.move(u, 0.1)

    # 模拟观测
    if t % 10 == 0:
        z = np.array([5 * np.cos(t/10), 5 * np.sin(t/10)]) + np.random.normal(0, 0.1, 2)
        robot.observe(z)

# 打印机器人的最终位置和协方差
print("机器人的位置：", robot.x)
print("机器人的协方差：\n", robot.P)