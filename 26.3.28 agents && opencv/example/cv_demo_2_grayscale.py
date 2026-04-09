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

    while True:
        ret, frame = cap.read()

        if not ret:
            print("错误：无法接收画面。")
            break

        # 将彩色图像转换为灰度图像
        # cv2.cvtColor() 是颜色空间转换函数
        # cv2.COLOR_BGR2GRAY 表示从 BGR（OpenCV 默认格式）转为灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 并排显示原始图像和灰度图像
        cv2.imshow("Original", frame)
        cv2.imshow("Grayscale", gray)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("正在退出...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
