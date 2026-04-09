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

        # 转换为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 应用高斯模糊以减少噪声
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 使用 Canny 边缘检测
        edges = cv2.Canny(blurred, 50, 150)

        # 查找轮廓
        # cv2.findContours() 返回轮廓列表和层次结构
        # cv2.RETR_EXTERNAL: 只检测外部轮廓
        # cv2.CHAIN_APPROX_SIMPLE: 压缩轮廓，只保留端点
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)

        # 创建一个副本用于绘制轮廓
        result = frame.copy()

        # 绘制所有轮廓
        # cv2.drawContours(image, contours, contourIdx, color, thickness)
        # contourIdx=-1 表示绘制所有轮廓
        # (0, 255, 0) 是绿色
        # 2 是线条粗细
        cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

        # 在图像上显示轮廓数量
        text = f"Contours: {len(contours)}"
        cv2.putText(result, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                   1, (0, 255, 0), 2)

        # 显示结果
        cv2.imshow("Edges", edges)
        cv2.imshow("Contours", result)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("正在退出...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
