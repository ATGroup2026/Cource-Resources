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
    cv2.namedWindow("Binary Threshold")

    # 创建滑块控制二值化阈值，范围 0-255，初始值为 127
    cv2.createTrackbar("Threshold", "Binary Threshold", 127, 255, lambda x: None)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("错误：无法接收画面。")
            break

        # 转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 获取滑块当前阈值
        threshold_value = cv2.getTrackbarPos("Threshold", "Binary Threshold")

        # 应用二值化
        # cv2.threshold(src, thresh, maxval, type)
        # thresh: 阈值
        # maxval: 超过阈值时的赋值（通常为 255）
        # cv2.THRESH_BINARY: 大于阈值的像素设为 maxval，否则设为 0
        _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

        # 显示结果
        cv2.imshow("Grayscale", gray)
        cv2.imshow("Binary Threshold", binary)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("正在退出...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
