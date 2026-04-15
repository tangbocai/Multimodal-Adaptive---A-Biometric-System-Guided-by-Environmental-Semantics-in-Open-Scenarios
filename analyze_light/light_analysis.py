import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# 添加中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def analyze_light(image_path):
    # 1. 读取图片
    img = cv2.imread(image_path)
    if img is None:
        print(f"错误：无法读取图片 '{image_path}'，请检查路径。")
        return

    # 2. 将图片从BGR转换到HSV色彩空间
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
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('原图')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(v_channel, cmap='gray')
    plt.title(f'亮度通道\n等级: {light_level}')
    plt.axis('off')

    plt.show()


if __name__ == "__main__":
    # 使用文件对话框选择图片，默认打开“我的电脑”目录
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(
        title="请选择一张图片进行分析",
        filetypes=[("图片文件", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if file_path:
        analyze_light(file_path)
    else:
        print("未选择任何文件，程序退出。")
