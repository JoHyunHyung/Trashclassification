import yaml
import cv2

# 이미지 로드
#image = cv2.imread('./dataset/train/label/A6label/A6R_20221121_012829.jpg')

# YAML 파일 읽기
with open('../dataset/test/label/A6C_20221118_000007.yaml', 'r', encoding='utf-8') as yaml_file:
    data = yaml.safe_load(yaml_file)

resolution = data["Info"]["RESOLUTION"]
parts = resolution.split("/")

print(parts)
"""
# original image width, height
image_width = float(parts[0].strip())  # 좌측 값
image_height = float(parts[1].strip())  # 우측 값

print("Width:", image_width)
print("Height:", image_height)

# "objects" 항목에서 "class_name"과 "coord" 값을 추출
objects_info = []
for obj in data.get("objects", []):
    class_name = obj.get("class_name")
    coord = obj.get("annotation", {}).get("coord", {})
    x = float(coord.get("x"))
    y = float(coord.get("y"))
    width = float(coord.get("width"))
    height = float(coord.get("height"))
    objects_info.append({"class_name": class_name, "coord": (x, y, width, height)})

# 클래스 이름, 좌표값
for i, info in enumerate(objects_info, 1):
    class_name = info.get("class_name")
    x, y, width, height = info.get("coord")

    # print(f"Object {i}:")
    # print(f"class_name: {class_name}")
    # print(f"x: {x}")
    # print(f"y: {y}")
    # print(f"width: {width}")
    # print(f"height: {height}")


# 변환 함수
def convert_to_yolo(x, y, width, height, image_width, image_height):
    target_size = 640
    resize_ratio = target_size / image_width
    padding_size = target_size - (image_height * resize_ratio)

    x_ = x * resize_ratio
    # y_ = (y + padding_size) * resize_ratio
    y_ = (y * resize_ratio) + (padding_size * 0.5)  # fix

    width_ = width * resize_ratio
    height_ = height * resize_ratio

    center_x = (x_ + width_ / 2) / target_size  # fix: image_size --> target_size
    center_y = (y_ + height_ / 2) / target_size  # fix: image_size --> target_size
    normalized_width = width_ / target_size  # fix: image_size --> target_size
    normalized_height = height_ / target_size  # fix: image_size --> target_size
    return center_x, center_y, normalized_width, normalized_height


center_x, center_y, normalized_width, normalized_height = convert_to_yolo(x, y, width, height, image_width,
                                                                          image_height)
print(center_x)
print(center_y)
print(normalized_width)
print(normalized_height)

# BBOX
target_size = 640

for info in objects_info:
    x, y, width, height = info.get("coord")
    center_x, center_y, normalized_width, normalized_height = convert_to_yolo(x, y, width, height, image_width,
                                                                              image_height)

    x_ = int(center_x * target_size)  # fix: image_size --> target_size
    y_ = int(center_y * target_size)  # fix: image_size --> target_size
    width_ = int(normalized_width * target_size)  # fix: image_size --> target_size
    height_ = int(normalized_height * target_size)  # fix: image_size --> target_size

    # BBOX
    top_left = (x_ - width_ // 2, y_ - height_ // 2)
    bottom_right = (x_ + width_ // 2, y_ + height_ // 2)

    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# 이미지 출력
# cv2.imshow('BBOX Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
"""