from django.shortcuts import render, redirect

import torch
import cv2
import random 




def pick_img(request, img_url):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='post/static/best.pt', force_reload=True)
    fruit_model = ['apple', 'banana', 'pineapple', 'orange', 'pear', 'guava' ]
    print(str(img_url))
    # test_img = cv2.imread('d:/sparta_camp/SCC_ML/scc_v5/object-recognition-project/mysite/post/detect/' + str(img_url))            # load image file root
    test_img = cv2.imread('./media/' + str(img_url))
    results = model(test_img)                 # detecting image file
    results.save()                       # save the results
    result = results.pandas().xyxy[0].to_numpy()
    
    img_detected = list()                # create list for saving ingredients in image
    
    for item in result:
        try:
            if item[6] in fruit_model:
                img_detected.append(item[6])            # 이미지 이름 추출
                picked = random.choice(img_detected)  
                context = {'picked':picked}
                return context
        except:
            context = {'error':'재료를 찾을 수 없습니다.'}
            return context





