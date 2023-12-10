import os
import glob

# 클래스 종류별로 객체 수를 저장할 딕셔너리
class_counts = {}

# YOLO 텍스트 파일이 있는 폴더 경로 설정
folder_path = "./ModifiedLabels"  # 폴더 경로를 적절히 변경하세요

# 폴더 내의 모든 txt 파일을 반복
for txt_file in glob.glob(os.path.join(folder_path, "*.txt")):
    # 텍스트 파일 읽기
    with open(txt_file, "r") as infile:
        for line in infile:
            parts = line.strip().split()
            if len(parts) >= 1:  # 최소한 클래스 레이블을 포함하는 줄
                label = int(parts[0])
                if label in class_counts:
                    class_counts[label] += 1
                else:
                    class_counts[label] = 1

# 클래스 레이블을 정렬
sorted_class_counts = sorted(class_counts.items(), key=lambda x: x[0])

# 정렬된 클래스 종류 및 해당 클래스의 객체 수 출력
for label, count in sorted_class_counts:
    print(f"클래스 {label}: {count}개의 객체")