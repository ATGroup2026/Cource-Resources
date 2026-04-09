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
    cv2.namedWindow("Morphology")

    # 创建滑块控制形态学运算的核大小，范围 1-21，初始值为 5
    cv2.createTrackbar("Kernel Size", "Morphology", 5, 21, lambda x: None)
    # 创建滑块选择形态学运算类型：0=腐蚀, 1=膨胀, 2=开运算, 3=闭运算
    cv2.createTrackbar("Operation", "Morphology", 0, 3, lambda x: None)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("错误：无法接收画面。")
            break

        # 转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 自适应二值化
        # cv2.adaptiveThreshold() 根据局部区域自动计算阈值
        # cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 使用高斯加权
        # cv2.THRESH_BINARY: 二值化类型
        # 11: 邻域大小
        # 2: 常数 C，从计算的均值中减去
        binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY, 11, 2)

        # 获取滑块值
        kernel_size = cv2.getTrackbarPos("Kernel Size", "Morphology")
        operation = cv2.getTrackbarPos("Operation", "Morphology")

        # 确保核大小至少为 1
        if kernel_size < 1:
            kernel_size = 1

        # 创建结构元素（核）
        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        # 根据选择的操作类型进行形态学运算
        if operation == 0:
            # 腐蚀：缩小白色区域，去除小噪点
            result = cv2.erode(binary, kernel, iterations=1)
        elif operation == 1:
            # 膨胀：扩大白色区域，填充小孔洞
            result = cv2.dilate(binary, kernel, iterations=1)
        elif operation == 2:
            # 开运算：先腐蚀后膨胀，去除小物体
            result = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        else:
            # 闭运算：先膨胀后腐蚀，填充物体内的小孔
            result = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

        # 显示结果
        cv2.imshow("Binary", binary)
        cv2.imshow("Morphology", result)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("正在退出...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
