def fun_max(nums):

    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num+=num
    return


import requests

url = "https://image-background-removal-v2.p.rapidapi.com/v1.0/transparent-net"

querystring = {"image":"https://i.pinimg.com/474x/77/7f/c2/777fc24364da5dfc590f196a1ef2cdc5.jpg"}

payload = {}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "d20a16e73dmsh40a1ef627fe69ebp187596jsn45f113b23412",
	"X-RapidAPI-Host": "image-background-removal-v2.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())