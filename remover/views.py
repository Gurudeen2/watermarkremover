from django.shortcuts import render
import cv2
from .models import WaterMarkRemove
from datetime import date
import numpy as np

# Create your views here.

def removewatermark(request):
    if request.method == "POST":

        img = request.FILES["image"]
        # img = str(img)
        # watermark = WaterMarkRemove.objects.create(photo=img)
        # watermark.save()

        today = date.today().strftime("%Y/%m/%d")
        # get_img = WaterMarkRemove.objects.filter(photo=f"photo/{today}/{img}").first().photo
        # img = cv2.imread(get_img.name, 1)

        # Load image as string from file/database
        im = open("media/84455cover.jpg", "rb")
        imgs = im.read()
        im.close()
        # fd = open(im)
        # img_str = fd.read()
        # fd.close()
        
        
        # img = "84455cover.jpg"
        # print("path",get_img.name)
        imgCv2=cv2.imdecode(np.fromstring(imgs, np.uint8), 1)
        # imgCv2 = cv2.imread(imgs, 1)
        # print("get", imgCv2)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                             cv2.THRESH_BINARY, 115, 1)
        cv2.imshow("Processed image", gray)
        # _, thresh =cv2.threshold(imgCv2, 150, 255,cv2.THRESH_BINARY)
        # print("thresh", thresh)
        # cv2.imshow("without watermark", thresh)
        cv2.waitKey(0)
    return render(request, "page/home.html")