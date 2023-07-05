from django.shortcuts import render
import cv2
from .models import WaterMarkRemove
from datetime import date
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create your views here.

#  photo = Image.open(self.image.path)
#         draw = ImageDraw.Draw(photo)
#         font = ImageFont.load_default()
#         width, height = photo.size
#         myword = "Hello world !"
#         margin = 10
#         textwidth, textheight = draw.textsize(myword, font)
#         x = width - textwidth - margin
#         y = height - textheight - margin
#         draw.text((x,y), myword, (255, 255, 255), font=font)
#         photo.save(self.image.path)

def removewatermark(request):
    if request.method == "POST":

        img = request.FILES["image"]
        # img = str(img)
        # watermark = WaterMarkRemove.objects.create(photo=img)
        # watermark.save()

        today = date.today().strftime("%Y/%m/%d")
        # get_img = WaterMarkRemove.objects.filter(photo=f"photo/{today}/{img}").first().photo
        get_img = WaterMarkRemove.objects.filter(photo=f"photo/2023/07/04/{img}").first().photo
        get_img2 = Image.open(get_img.path)
        print(get_img2)

        
        with Image.open(get_img.path) as img:
            # get the height and width
            width, height = img.size
            # preparing d text watermark change the color in the lastparamter below
            txt = Image.new("RGBA", img.size, (255, 255, 255, 0))

            # custom font
            fnt = ImageFont.truetype("arial", 60)

            # create image text

            d = ImageDraw.Draw(txt)
        
            # get width hight of the text
            _, _, w, h, = d.textbbox((0,0), "Akeem Tolani", font=fnt)

            # write into center
            d.text(((width-w)/2, (height-h)/2), "Akeem Tolani", font=fnt, fill=(255,255,255,255))

            # img + text
            result = Image.alpha_composite(get_img, txt)

            result.save("r.png")
            result.show()
        # font = ImageFont.load_default()
        # draw = ImageDraw.Draw(photo)
        # width, height = photo.size
        # myword = "Fatai Akeem Tolani"
        # margin = 10
        # textwidth, textheight = draw.textlength(myword, font)
        # x = width - textwidth - margin
        # y = height - textheight - margin
        # draw.text((x,y), myword, (255, 255, 255), font=font)
        # photo.save(get_img.path)

        # img = cv2.imread(get_img.name, 1)

        # Load image as string from file/database
        # im = open("media/84455cover.jpg", "rb")
        # imgs = im.read()
        # im.close()
        # fd = open(im)
        # img_str = fd.read()
        # fd.close()
        
        
        # img = "84455cover.jpg"
        # print("path",get_img.name)
        # imgCv2=cv2.imdecode(np.fromstring(imgs, np.uint8), 1)
        # imgCv2 = cv2.imread(imgs, 1)
        # print("get", imgCv2)
        # gray = cv2.cvtColor(imgCv2, cv2.COLOR_BGR2GRAY)
        # gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        #                      cv2.THRESH_BINARY, 115, 1)
        # cv2.imshow("Processed image", gray)
        # _, thresh =cv2.threshold(imgCv2, 150, 255,cv2.THRESH_BINARY)
        # print("thresh", thresh)
        # cv2.imshow("without watermark", photo)
        # cv2.waitKey(0)
    return render(request, "page/home.html")