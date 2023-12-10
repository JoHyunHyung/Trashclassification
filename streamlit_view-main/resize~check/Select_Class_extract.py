import os
import random
import shutil

# 원본 이미지 파일이 있는 폴더 경로
input_image_folder = "./images"  # 적절한 경로로 변경하세요

# "0" 클래스에 해당하는 이미지를 저장할 폴더 경로
output_folder = "./class_0_images"  # 적절한 경로로 변경하세요

# "0" 클래스에 해당하는 이미지를 랜덤하게 1000장 추출
class_to_extract = "0"
num_images_to_extract = 1000

# 이미지 파일 리스트 생성
image_files = []
for root, dirs, files in os.walk(input_image_folder):
    for file in files:
        if file.endswith(".jpg"):  # 이미지 파일 확장자에 따라 수정
            image_files.append(os.path.join(root, file))

# 랜덤하게 이미지 추출
random.shuffle(image_files)
output_counter = 0

for image_file in image_files:
    # 이미지 파일에서 클래스 레이블 추출
    # 예를 들어, 파일 이름에서 클래스 정보를 파싱하여 추출
    class_label = image_file.split(os.path.sep)[-1].split("_")[0]

    if class_label == class_to_extract:
        output_counter += 1
        output_image_path = os.path.join(output_folder, os.path.basename(image_file))
        shutil.copy(image_file, output_image_path)

    if output_counter >= num_images_to_extract:
        break

print(f"{output_counter} images from class {class_to_extract} have been extracted and saved in the '{output_folder}' folder.")