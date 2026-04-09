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
    cv2.namedWindow("Canny Edge Detection")

    # 创建滑块控制 Canny 边缘检测的两个阈值
    # threshold1: 低阈值，范围 0-255，初始值为 50
    # threshold2: 高阈值，范围 0-255，初始值为 150
    cv2.createTrackbar("Threshold1", "Canny Edge Detection", 50, 255, lambda x: None)
    cv2.createTrackbar("Threshold2", "Canny Edge Detection", 150, 255, lambda x: None)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("错误：无法接收画面。")
            break

        # 转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 获取滑块当前值
        threshold1 = cv2.getTrackbarPos("Threshold1", "Canny Edge Detection")
        threshold2 = cv2.getTrackbarPos("Threshold2", "Canny Edge Detection")

        # 应用 Canny 边缘检测
        # cv2.Canny(image, threshold1, threshold2)
        # threshold1: 低阈值，用于边缘连接
        # threshold2: 高阈值，用于初始边缘检测
        # 通常 threshold2 = 2 * threshold1 或 3 * threshold1
        edges = cv2.Canny(gray, threshold1, threshold2)

        # 显示结果
        cv2.imshow("Grayscale", gray)
        cv2.imshow("Canny Edge Detection", edges)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("正在退出...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
