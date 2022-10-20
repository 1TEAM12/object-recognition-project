from django.shortcuts import render, redirect

import torch
import cv2
import random 

# def img_detection(request):
model = torch.hub.load('ultralytics/yolov5', 'custom', path='post/static/best.pt', force_reload=True)
fruit_model = ['apple', 'banana', 'pineapple', 'orange', 'pear', 'guava' ]

def pick_img(request, img_url):
    print('../media/'+ str(img_url))
    test_img = cv2.imread('./media/'+ str(img_url))            # load image file root
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



    # for item in result:
    #     try:
    #         if item[6] in fruit_model:
    #             img_detected.append(item[6])            # 이미지 이름 추출
    #     except:
    #         return render(request, 'post/post/post_create.html', {'error':'재료를 찾을 수 없습니다.'})
        
    # picked = random.choice(img_detected)            # choice the ingredient
    # return render(request, 'post/post/post_create.html', {'picked':picked})




