import os
import glob


def map_class_label(label):
    if 1 <= label <= 2: #종이
        return 0
    elif 5 <= label <= 8: #유리
        return 4
    elif label == 13: #이물질종이
        return 0
    elif 20 <=label <= 23: #이물질유리
        return 4
    elif label == 17: #이물질페트
        return 16
    elif label == 24: #이물질페트
        return 16
    elif label == 26:
        return 25
    else:
        return label

#경로 설정
input_folder_path = "./A1label"

output_folder_path = "./ModifiedLabels"

# 폴더생성
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

for txt_file in glob.glob(os.path.join(input_folder_path, "*.txt")):

    output_file = os.path.join(output_folder_path, os.path.basename(txt_file))

    with open(txt_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            parts = line.strip().split()
            if len(parts) >= 2:
                original_label = int(parts[0])
                modified_label = map_class_label(original_label)
                parts[0] = str(modified_label)
                updated_line = " ".join(parts)
                outfile.write(updated_line + "\n")
            else:
                outfile.write(line)

print("test end")