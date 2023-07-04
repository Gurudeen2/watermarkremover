from django.shortcuts import render
import cv2
from .models import WaterMarkRemove
from datetime import date

# Create your views here.

def removewatermark(request):
    if request.method == "POST":

        img = request.FILES["image"]
        # img = str(img)
        # watermark = WaterMarkRemove.objects.create(photo=img)
        # watermark.save()

        today = date.today().strftime("%Y/%m/%d")
        get_img = WaterMarkRemove.objects.filter(photo=f"photo/{today}/{img}").first().photo
        print("date",date.today().strftime("%Y/%m/%d"))
        print("get", get_img)
        
        # img = "84455cover.jpg"
        print("path",get_img.name)
        # img = cv2.imread(get_img.name, 1)
        # _, thresh =cv2.threshold(img, 150, 255,cv2.THRESH_BINARY)
        # print("thresh", thresh)
        # cv2.imshow("without watermark", thresh)
    return render(request, "page/home.html")