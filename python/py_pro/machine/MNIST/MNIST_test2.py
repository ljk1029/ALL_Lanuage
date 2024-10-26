import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

# 加载训练好的模型
model = keras.models.load_model('mnist_model.h5')

# 选择要显示的测试图像数量
num_images_to_display = 10

# 随机选择10个测试图像的索引
image_indices = np.random.choice(len(test_images), num_images_to_display, replace=False)

# 创建一个2行5列的图像显示窗口
plt.figure(figsize=(10, 4))

# 遍历选择的图像索引
for i, image_index in enumerate(image_indices, 1):
    image = test_images[image_index]  # 从测试集中获取图像
    predictions = model.predict(np.array([image]))
    predicted_label = np.argmax(predictions)

    plt.subplot(2, 5, i)
    plt.imshow(image.reshape(28, 28), cmap='gray')
    plt.title(f'Predicted: {predicted_label}')
    plt.axis('off')

plt.show()