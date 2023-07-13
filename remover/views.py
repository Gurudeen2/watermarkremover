import sys
from django.shortcuts import render
from django.http import HttpResponse
import cv2
from .models import WaterMarkRemove
from datetime import date
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
from django.core.files import File
# fr

# Create your views here.

def remove_watermark(img_path):
    image = cv2.imread(img_path)

    print("path needed",img_path)

    # im = cv2.imread(sys.path[0]+"/a.jpg", 1)
    #convert BGR image to RGB(if necessary)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BayerGB2RGB)

    #perform inpainting to remove the watermark
    mask = create_watermark_mask(img_rgb)
    # masked_image = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)
    #
    inpainted_img = inpaint(img_rgb, mask)

    #convert the image back to pil image format
    modified_image = Image.fromarray(inpainted_img)
    modified_image.show()
    return modified_image

def create_watermark_mask(image):
    lower_threshold = np.array([255, 255, 255], dtype=np.uint8)
    upper_threshold = np.array([255, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(image, lower_threshold, upper_threshold) 
    return mask

def inpaint(image, mask):
    #perform image inpainting using OpenCV's inpaint function

    inpainted_image = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

    #fiiled
    # inpainted_image = fill
    return inpainted_image

def home(request):
    # WaterMarkRemove.objects.all().delete()
    return render(request, "page/home.html")

def remove_img_background(request):
    return render(request, "page/removebg.html")

def addwatermark(request):
    if request.method == "POST":

        img = request.FILES["image"]
        word = request.POST["text"]



        # img = str(img)
        watermark = WaterMarkRemove.objects.create()
        # watermark.save()

        # today = date.today().strftime("%Y/%m/%d")
        # get_img = WaterMarkRemove.objects.filter(photo=f"photo/{today}/{img}").first().photo

# add text to image
        filename = str(img).split(".")
        im = Image.open(img)
        
        width, height = im.size


        text = Image.new("RGBA", im.size, (255, 255, 255, 0))

        font = ImageFont.truetype("arial.ttf", 50)
        txt = ImageDraw.Draw(text)
        draw = ImageDraw.Draw(im)
        _, _, w, h, = txt.textbbox((0,0), word, font=font)
        
        draw.text(((width-w-10), (height-h-10)), word,(255,255,255), font=font)
        
        # im.show()
        # bufferpng = BytesIO()

        im.save("media/"+filename[0]+"."+im.format)
        l_img = open(f'media/{filename[0]}.{im.format}', "rb")
        convert_img_to_file = File(l_img)
        watermark.photo.save(filename[0]+"."+im.format, convert_img_to_file)

        
        
        

        # print("images", WaterMarkRemove.objects.all())
        

        # # im.save(bufferpng, im.format, quality=60)
        # print("bytes", WaterMarkRemove.objects.all())
        # im.save(im.filename, ContentFile(bufferpng.getvalue()), save=True)
        # im.save(bufferpng, kind=".PNG")
        # img_str = base64.b64encode(bufferpng.getvalue()).decode('utf-8')

        # # img = str(img)
        # #updating the image to db
        # WaterMarkRemove.objects.filter(photo=img).update(photo=im)
      
        return render(request, "page/watermark.html", context={"wimage":WaterMarkRemove.objects.all().first().photo})
    return render(request, "page/watermark.html")