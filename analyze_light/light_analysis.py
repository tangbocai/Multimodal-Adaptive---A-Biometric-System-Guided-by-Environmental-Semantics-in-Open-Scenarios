import cv2
import numpy as np
import matplotlib.pyplot as plt

# 添加中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False   # 解决负号 '-' 显示为方块的问题

def analyze_light(image_path):
    # 1. 读取图片
    img = cv2.imread(image_path)
    if img is None:
        print(f"错误：无法读取图片 '{image_path}'，请检查路径。")
        return

    # 2. 将图片从BGR转换到HSV色彩空间 (OpenCV默认读取为BGR)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 3. 提取亮度 (Value) 通道
    v_channel = hsv_img[:, :, 2]

    # 4. 计算亮度统计值
    avg_brightness = np.mean(v_channel)
    std_brightness = np.std(v_channel)

    # 5. 进行光照分级
    if avg_brightness < 85:
        light_level = "暗"
    elif avg_brightness < 170:
        light_level = "中等"
    else:
        light_level = "亮"

    print(f"图片: {image_path}")
    print(f"  平均亮度 (0-255): {avg_brightness:.2f}")
    print(f"  亮度标准差: {std_brightness:.2f}")
    print(f"  光照等级: {light_level}")

    # 6. 可视化原图和亮度通道
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 显示需转回RGB
    plt.title('原图')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(v_channel, cmap='gray')
    plt.title(f'亮度通道\n等级: {light_level}')
    plt.axis('off')

    plt.show()


if __name__ == "__main__":
    # 在下方填写图片路径
    analyze_light("Black_Footed_Albatross_0002_55.jpg")