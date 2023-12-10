import os
import glob

# 이미지 파일이 있는 폴더 경로
image_folder = "./class_0_images"  # 이미지 파일이 있는 폴더 경로를 적절히 변경하세요

# YOLO 텍스트 파일이 있는 폴더 경로
yolo_txt_folder = "./YOLO_Text_Files"  # YOLO 텍스트 파일이 있는 폴더 경로를 적절히 변경하세요

# 클래스 종류별로 객체 수를 저장할 딕셔너리
class_counts = {}

# 이미지 파일 이름에서 클래스 레이블을 추출하여 딕셔너리에 저장
for image_file in os.listdir(image_folder):
    if image_file.endswith(".jpg"):
        image_name = os.path.splitext(image_file)[0]
        image_label = int(image_name.split("_")[0])

        if image_label in class_counts:
            class_counts[image_label] += 1
        else:
            class_counts[image_label] = 1

# YOLO 텍스트 파일을 확인하여 클래스 종류별로 객체 수를 업데이트
for txt_file in glob.glob(os.path.join(yolo_txt_folder, "*.txt")):
    with open(txt_file, "r") as infile:
        for line in infile:
            parts = line.strip().split()
            if len(parts) >= 1:
                label = int(parts[0])
                if label in class_counts:
                    class_counts[label] += 1

# 클래스 종류 및 해당 클래스의 객체 수 출력
for label, count in class_counts.items():
    print(f"클래스 {label}: {count}개의 객체")