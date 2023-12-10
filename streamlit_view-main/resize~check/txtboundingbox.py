import cv2
import os
# 클래스 번호와 이름 매핑 딕셔너리
class_mapping = {
    0: 'c_1',
    1: 'c_2_01',
    2: 'c_2_02',
    3: 'c_3',
    4: 'c_4_01_02',
    5: 'c_4_02_01_02',
    6: 'c_4_02_02_02',
    7: 'c_4_02_03_02',
    8: 'c_4_03',
    9: 'Pet',
    10: 'Plastic',
    11: 'Vinyl',
    12: 'c_1_01',
    13: 'c_2_02_01',
    14: 'c_3_01',
    15: 'c_4_03_01',
    16: 'Pet',
    17: 'c_5_02_01',
    18: 'c_6_01',
    19: 'c_7_01',
    20: 'c_4_01_01',
    21: 'c_4_02_01_01',
    22: 'c_4_02_02_01',
    23: 'c_4_02_03_01',
    24: 'Pet',
    25: 'c_8_01',
    26: 'c_8_02',
    27: 'c_8_01_01',
    28: 'c_9',
}

# YOLO 텍스트 파일 경로
yolo_txt_folder = 'C:/Users/54/Desktop/Practice/A1image'  # YOLO 텍스트 파일이 있는 폴더
image_folder = 'C:/Users/54/Desktop/Practice/A1image'  # 이미지 파일이 있는 폴더

# 출력 이미지 폴더
output_folder = './A1image'
os.makedirs(output_folder, exist_ok=True)

# YOLO 텍스트 파일 읽기 및 바운딩 박스 그리기
for yolo_txt_file in os.listdir(yolo_txt_folder):
    if yolo_txt_file.lower().endswith('.txt'):
        yolo_txt_path = os.path.join(yolo_txt_folder, yolo_txt_file)
        image_path = os.path.join(image_folder, os.path.splitext(yolo_txt_file)[0] + ".png")
        output_image_path = os.path.join(output_folder, os.path.splitext(yolo_txt_file)[0] + "_output.png")

        image = cv2.imread(image_path)
        with open(yolo_txt_path, 'r') as txt_file:
            for line in txt_file:
                parts = line.strip().split()
                class_id = int(parts[0])
                center_x = float(parts[1])
                center_y = float(parts[2])
                width = float(parts[3])
                height = float(parts[4])

                # 좌표 및 크기를 절대 좌표로 변환
                x = int((center_x - width / 2) * 640)
                y = int((center_y - height / 2) * 640)
                x_max = int((center_x + width / 2) * 640)
                y_max = int((center_y + height / 2) * 640)

                # 클래스 번호에 해당하는 클래스 이름 가져오기
                class_name = class_mapping.get(class_id, "Unknown")

                cv2.rectangle(image, (x, y), (x_max, y_max), (0, 255, 0), 1)
                cv2.putText(image, class_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 100), 1)

        # 결과 이미지 저장
        cv2.imwrite(output_image_path, image)

        # 결과 이미지 표시
        cv2.imshow('Result Image', image)
        cv2.waitKey(0)

cv2.destroyAllWindows()