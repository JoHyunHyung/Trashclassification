import glob
import os
import cv2

from ultralytics import YOLO

model=YOLO("./best.pt")

#예측하고자 하는 데이터 할당
results=model.predict(
    "./A1image/A6C_20221118_000007.png",
    save=False,
    imgsz=640,
    conf=0.6,
    device='cuda'
    )
for r in results:
    #박스정보 - cls, conf, data, 변환한 데이터 등등 나옴 .xyxy처럼 어떤 자료를 얻을 수 있을지, 뭘 써야할지 알 수 있다
    #print(r.boxes)
    boxes = r.boxes.xyxy

    #딕셔너리 형태로 주어지는데, 이를 통해 라벨 스트링 값을 뽑아낼 수 있음 이 스트링으로 표기되게도 가능
    #print(r.names)
    #아래에 cls_dict에 할당해서 classname에 할당한 거로 설정한거 뽑음
    cls_dict = r.names

    #cls정보 보는거
    cls=r.boxes.cls
    #print(cls)

    #confidence점수 뽑아서 보는거
    conf=r.boxes.conf
    print(conf)

    #이거 경로 처리가 잘 안되면 window경로처리를 따로 해야된다고 함 강의에선 yolo5에서 했다는디?
    image_path=r.path

    image=cv2.imread(image_path)
    w,h,c=image.shape
    #image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    # 만약 이미지 리사이즈를 해서 보고싶다?
    """
    target = 640
    image=cv2.resize(image,(target,target))
    """

    for box,cls_number, conf in zip(boxes,cls,conf):

        #클래스 넘버 - 초기에 0하고 1로 설정한거 뭔지 나오게 하는거 현 프로젝트에서는 c_06이니 int는 쓸 필요x
        cls_number_int=int(cls_number.item())
        #이건 클래스 넘버 보고 이름 설정한거로 나오게 함
        cls_name=cls_dict[cls_number_int]
        #confidence 점수
        conf_num=float(conf.item())

        #int써야 rectangle에 인식
        x1,y1,x2,y2=box
        x1_int=int(x1.item())
        y1_int=int(y1.item())
        x2_int=int(x2.item())
        y2_int=int(y2.item())

        #resize 했을 때 쓰는거임
        #resize_w_ratio=target/w
        #resize_h_ratio=target/h

        #int를 주는 이유는 rectangle에 int가 아니면 인식을 안함
        # x1_scale=int(x1_int*resize_w_ratio)
        # y1_scale=int(y1_int*resize_h_ratio)
        # x2_scale=int(x2_int*resize_w_ratio)
        # y2_scale=int(y2_int*resize_h_ratio)

        print(x1_int,y1_int,x2_int,y2_int,cls_number_int,cls_name)
        image=cv2.rectangle(image,(x1_int,y1_int),(x2_int,y2_int),(0,255,0),2)
        #image = cv2.rectangle(image, (x1_int, y1_int), (x2_int, y2_int), (0, 255, 0), 6) 축소된거 보려면 위 이미지 축소 안하고 보려면 이거
        label = f"{cls_number_int}: {conf_num:.2f}"
        image = cv2.putText(image, label, (x1_int, y1_int - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imwrite("./test.png",image)
    cv2.imshow("Test",image)
    cv2.waitKey(0)

#print(results)