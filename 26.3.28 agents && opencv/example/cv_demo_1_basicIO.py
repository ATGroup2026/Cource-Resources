# /// script
# dependencies = [
#   "opencv-python",
#   "numpy",
# ]
# ///

# 以上为uv声明依赖

import cv2  # 导入 OpenCV 库
import numpy as np  # 导入矩阵运算库（OpenCV 的底层支撑）

def main():
    cap = cv2.VideoCapture(1) # 初始化cap实例对象
    # 检查摄像头是否成功打开
    if not cap.isOpened(): 
        print("错误：无法打开摄像头。请检查权限或驱动。")
        return

    # 视频处理本质上是一个死循环，每个循环处理一帧图像
    while True:
        ret, frame = cap.read() # cap.read() 返回两个值：frame未这一帧的图像(NumPy 数组)，ret:为布尔值表示是否成功读取到这一帧

        if not ret:
            print("错误：无法接收画面（流结束？）。")
            break


        

        # 在窗口中实时显示这一帧
        # 窗口名称为 "Live Camera"，如果该名称窗口已存在，则只更新内容
        cv2.imshow("Live Camera", frame)

        # waitKey(1) ：
        # 1. 阻塞 1 毫秒等待键盘输入
        # 2. 刷新窗口界面，使图像显示出来
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            # 如果按下 'q' 键，退出循环，视频处理结束，否则继续while循环
            print("正在退出...")
            break
    
    cap.release() # 必须释放摄像头资源，否则其他程序（如腾讯会议）无法再次调用它
    cv2.destroyAllWindows() # 关闭所有 OpenCV 创建的窗口，防止程序残留

if __name__ == "__main__":
    main()