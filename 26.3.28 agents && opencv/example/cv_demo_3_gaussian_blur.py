# /// script
# dependencies = [
#   "opencv-python",
#   "numpy",
# ]
# ///

# 以上为uv声明依赖

import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("错误：无法打开摄像头。")
        return

    # 创建窗口
    cv2.namedWindow("Gaussian Blur")

    # 创建滑块控制高斯模糊的核大小
    # 核大小必须是奇数，范围 1-31，初始值为 5
    cv2.createTrackbar("Kernel Size", "Gaussian Blur", 5, 31, lambda x: None)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("错误：无法接收画面。")
            break

        # 获取滑块当前值
        kernel_size = cv2.getTrackbarPos("Kernel Size", "Gaussian Blur")

        # 确保核大小为奇数且至少为 1
        if kernel_size % 2 == 0:
            kernel_size += 1
        if kernel_size < 1:
            kernel_size = 1

        # 应用高斯模糊
        # cv2.GaussianBlur(src, ksize, sigmaX)
        # ksize: 核大小 (width, height)，必须为奇数
        # sigmaX: X 方向标准差，设为 0 时自动根据核大小计算
        blurred = cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)

        # 显示结果
        cv2.imshow("Original", frame)
        cv2.imshow("Gaussian Blur", blurred)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("正在退出...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
