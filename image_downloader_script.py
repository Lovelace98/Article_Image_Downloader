import requests
from bs4 import BeautifulSoup
import urllib.request


def return_hairstyle_name_and_description(article_link):
    """
    this function takes in the article link and produces a json file with the title of the hairstyles,
    its descriptions and the link to corresponding images :param article_link
    """
    response = requests.get(article_link)
    soup = BeautifulSoup(response.content, 'html5lib')

    hairstyle_names = [header.text for header in soup.find_all("h3") if header.find_next_sibling('p')]
    image_links = [image["data-lazy-src"] for image in soup.find_all('img') if
                   image.find_next_sibling('figcaption', class_="wp-element-caption")]
    # print((len(hairstyle_names)))
    # print(len(image_links))
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    for image, name in zip(image_links, hairstyle_names):
        print(f"downloaded {name}")
        urllib.request.urlretrieve(url=image, filename=f"{name}.jpg")


return_hairstyle_name_and_description("https://blackshome.com/knotless-braids-with-color/")
  