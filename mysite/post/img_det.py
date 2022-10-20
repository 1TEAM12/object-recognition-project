from django.shortcuts import render, redirect

import torch
import cv2
import random 

# def img_detection(request):
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model_det/best.pt', force_reload=True)
fruit_model = ['apple', 'banana', 'pineapple', 'orange', 'pear', 'guava' ]

def pick_img(img_url):
    img = cv2.imread(img_url)            # load image file root
    results = model(img)                 # detecting image file
    results.save()                       # save the results
    result = results.pandas().xyxy[0].to_numpy()
    
    img_detected = list()                # create list for saving ingredients in image

    for item in result:
        try:
            if item[6] in fruit_model:
                img_detected.append(item[6])            # 이미지 이름 추출
        except:
            return redirect('post:post-create-img',{'error':'재료를 찾을 수 없습니다.'})
        
    picked = random.choice(img_detected)            # choice the ingredient
    return redirect('post:post-create',picked=picked)

