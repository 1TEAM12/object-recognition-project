from django.shortcuts import render, redirect

import torch
import cv2
import random 

# def img_detection(request):
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model_det/best.pt', force_reload=True)
fruit_model = ['apple', 'banana', 'pineapple', 'orange', 'pear', 'guava' ]

def pick_img(img_url):
    img = cv2.imread(img_url)    # 이미지 불러오기
    results = model(img)                                # 이미지 검사
    img_detected = list()                # 이미지 검사 후 저장할 리스트 지정
    results.save()
    result = results.pandas().xyxy[0].to_numpy()

    for item in result:
        try:
            if item[6] in fruit_model:
                img_detected.append(item[6])            # 이미지 이름 추출
        except:
            return redirect('post:post-create-img',{'error':'재료를 찾을 수 없습니다.'})
        
    picked = random.choice(img_detected)            # 추출한 과일이름 중 하나 선택
    return redirect('post:post-create',picked=picked)

