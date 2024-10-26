import numpy as np
import matplotlib.pyplot as plt

# 加载训练好的模型
from tensorflow import keras
model = keras.models.load_model('mnist_model.h5')

# 加载并显示一个手写数字图像（可以自己手写一个数字图像，或从测试集中选取）
image_index = 256  # 随机选择一个测试图像
image = test_images[image_index]  # 从测试集中获取图像

# 使用模型进行预测
predictions = model.predict(np.array([image]))
predicted_label = np.argmax(predictions)

# 显示图像和预测结果
plt.imshow(image.reshape(28, 28), cmap='gray')
plt.title(f'Predicted Label: {predicted_label}')
plt.show()

