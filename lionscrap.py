from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import os
import urllib


def simple_get(url):
    try:
        with closing(get(url,stream= True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during to {0} : {1}'.format(url,str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code ==200 and content_type is not None and content_type.find('html')>-1)

def save_lion_image(lion_list):

    for name in lion_list:
        print("-------------------------------", name, "---------------------------")
        if name =="Teriano" or name == "Tigis":
            continue

        path = "C:\\Users\\DlaminiN3\\Desktop\\Lion_Data\\"
        try:
            os.makedirs(path+os.sep+name)
        except FileExistsError:
            print("Could not create folder, it exits")
            continue

        url = "http://livingwithlions.org/mara/lions/"+name+"/"
        raw_html = simple_get(url)
        if raw_html is not None:
            html = BeautifulSoup(raw_html, 'html.parser')
            image_div = html.find_all("div", {"id":"tabs-1"})
            image_name_list = []
            for item in image_div:

                body_part_list = item.ul

                for part in body_part_list:
                    try:
                        body_part = part.a.text
                        body_part = body_part.rstrip()
                        body_part = body_part.lstrip()
                        body_part_image = part.a.img['src']
                        image_name = name+"_"+body_part

                        count = image_name_list.count(image_name)
                        if count > 0:
                            image_name = image_name+count

                        image_name_list.append(image_name)
                        image_name = image_name+".png"
                        req = urllib.request.Request(body_part_image)
                        response = urllib.request.urlopen(req)

                        with open(path+os.sep+name+os.sep+image_name, 'wb') as img_file:
                            img_file.write(response.read())
                            print('Url saved as %s' % path+os.sep+name+os.sep+image_name)
                        print(body_part, body_part_image)
                    except:
                        continue
        else:
            print("URL IS None")
def save_to_local(image_url):
    print("Starting to save image\n")

def get_lions_list(url):
    print('Getting Lion names \n')

    lion_list = []
    raw_html = simple_get(url)
    if raw_html is not None:
        html = BeautifulSoup(raw_html, 'html.parser')
        lion_div = html.find_all("div", {"class": "resultBox"})
        for each_lion in lion_div:
            lion_name = each_lion.h2.a.text
            lion_name = lion_name.rstrip()
            lion_name = lion_name.lstrip()
            lion_list.append(lion_name)
    return lion_list

def get_data_features(url):
    raw_html =simple_get(url)
    print('Getting Lion features from living with lions site \n')
    if raw_html is not None:
        html = BeautifulSoup(raw_html,'html.parser')
        lion_div = html.find_all("div",{"class":"resultBox"})

        for each_lion in lion_div:
            lion_name = each_lion.h2.a.text
            data = ""
            data = data+lion_name
            feature_list = each_lion.ul

            for li in feature_list:
                if li is not None:
                    try:
                       data = data+","+(li.text[li.text.rfind(':')+1:].rstrip().lstrip())

                    except:
                        continue
            with open("C:\\Users\\DlaminiN3\\Desktop\\Lion_Data\\" + "lion_features.csv", 'a+') as lion_f_file:
                lion_f_file.write(data+"\n")
                print(data)
def log_error(e):
    print(e)

if __name__ =='__main__':
    url = 'http://livingwithlions.org/mara/browse/all/all/'
    #lion_names = get_lions_list(url)
    #save_lion_image(lion_names)
    get_data_features(url)
    print('Done \n')

