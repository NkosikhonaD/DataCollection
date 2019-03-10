from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


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

def get_data_features(url):
    raw_html =simple_get(url)

    if raw_html is not None:
        html = BeautifulSoup(raw_html,'html.parser')
        lion_div = html.find_all("div",{"class":"resultBox"})

        for each_lion in lion_div:
            lion_name = each_lion.h2.a.text
            data = ""
            data=data+lion_name
            feature_list = each_lion.ul
            #print(lion_name)
            for li in feature_list:
                if li is not None:
                    try:
                       data=data+","+(li.text[li.text.rfind(':')+1:].rstrip().lstrip())

                    except:
                        continue
            print(data)

def log_error(e):
    print(e)

if __name__ =='__main__':
    print('Getting Lion features from living with lions site\n')
    url = 'http://livingwithlions.org/mara/browse/all/all/'
    get_data_features(url)
    print('Done \n')

