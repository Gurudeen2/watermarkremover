from django.shortcuts import render
import cv2

# Create your views here.

def removewatermark(request):
    if request.method == "POST":

        # img = request.FILES["image"]
        img = "84455cover.jpg"
        print(img)
        img = cv2.imread(img, 1)
        _, thresh =cv2.threshold(img, 150, 255,cv2.THRESH_BINARY)
        cv2.imshow("without watermark", thresh)
    return render(request, "page/home.html")