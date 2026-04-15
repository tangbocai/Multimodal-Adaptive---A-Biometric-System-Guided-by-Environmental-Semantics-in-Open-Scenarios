import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_light(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Cannot read image '{image_path}'")
        return

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    R = img_rgb[:, :, 0].astype(np.float32)
    G = img_rgb[:, :, 1].astype(np.float32)
    B = img_rgb[:, :, 2].astype(np.float32)

    numerator = 2 * G - R - B
    denominator = 2 * G + R + B + 1e-6
    gli = numerator / denominator

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title('Original')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    gli_display = ((gli + 1) / 2 * 255).astype(np.uint8)
    plt.imshow(gli_display, cmap='Greens')
    plt.title('GLI (Vegetation Index)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(gli, cmap='RdYlGn', vmin=-1, vmax=1)
    plt.title('GLI Colormap')
    plt.colorbar(label='GLI (-1 to 1)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    path = r"D:\PyCharm 2024.1.7\data\aeroscapes\aeroscapes\JPEGImages\000003_026.jpg"
    analyze_light(path)