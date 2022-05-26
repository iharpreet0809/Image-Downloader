import requests
url="https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
resp=requests.get(url)
resp.status_code

with open('image.jpg', 'wb') as fp:
    fp.write(resp.content)
    
def download(url, filename):
    try:
        resp = requests.get(url)
        if resp.status_code==200:
            with open(filename, 'wb') as fp:
                fp.write(resp.content)
                print("Image downloaded Successfully")
        else:
            return "Invalid Url"
    except Exception as error:
        return error
# url1=input("Enter the url= ")
# format=".jpg"
# filename1= input("Enter the file name you want= ")
# download(url1,filename1)

download("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg","tree.jpg")
