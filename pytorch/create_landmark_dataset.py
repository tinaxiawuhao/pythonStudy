"""Create a sample face landmarks dataset.

Adapted from dlib/python_examples/face_landmark_detection.py
See this file for more explanation.

Download a trained facial shape predictor from:
    http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
"""
# dlib：用于人脸检测和关键点提取。
# glob：用于查找匹配特定模式的文件路径。
# csv：用于读写 CSV 文件。
# skimage.io：用于读取图像文件。
import dlib
import glob
import csv
from skimage import io

"""
detector：使用 dlib.get_frontal_face_detector() 初始化人脸检测器。
predictor：使用 dlib.shape_predictor 加载预训练的关键点预测模型（shape_predictor_68_face_landmarks.dat），该模型可以检测 68 个人脸关键点。
"""
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# num_landmarks：设置为 68，表示每个人脸有 68 个关键点。
num_landmarks = 68

"""
face_landmarks.csv：输出 CSV 文件的路径。
header：CSV 文件的表头，包含 image_name 和每个关键点的 x、y 坐标（例如 part_0_x, part_0_y, ..., part_67_x, part_67_y）。
csv_writer.writerow(header)：将表头写入 CSV 文件。
"""
with open('face_landmarks.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    header = ['image_name']
    for i in range(num_landmarks):
        header += ['part_{}_x'.format(i), 'part_{}_y'.format(i)]

    csv_writer.writerow(header)

    # 遍历所有 .jpg 文件：
    for f in glob.glob('*.jpg'):
        # 读取图像：
        img = io.imread(f)
        # 使用 detector 检测图像中的人脸，返回检测到的人脸框列表 dets。
        dets = detector(img, 1)  # face detection

        # 只处理检测到恰好一张人脸的图像，忽略没有检测到人脸或检测到多张人脸的图像。
        if len(dets) == 1:
            row = [f]

            d = dets[0]
            # 使用 predictor 提取人脸关键点，返回 shape 对象。
            shape = predictor(img, d)
            # 将图像文件名和每个关键点的 x、y 坐标添加到 row 列表中。
            for i in range(num_landmarks):
                part_i_x = shape.part(i).x
                part_i_y = shape.part(i).y
                row += [part_i_x, part_i_y]

            csv_writer.writerow(row)
