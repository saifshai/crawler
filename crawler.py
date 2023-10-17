from bs4 import Tag, NavigableString, BeautifulSoup
import requests
def main():

    url = "https://www.newegg.ca/lg-29wp60g-b-29-uw-fhd/p/N82E16824026099"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    print(doc.prettify)
    price = doc.find_all(string="$")
    price = price[0].parent
    strong = price.find("strong")
    print(strong.string)
    # html_doc = """
    # <html><head><title>The Dormouse's story</title></head>
    # <body>
    # <p class="title"><b>The Dormouse's story</b></p>

    # <p class="story">Once upon a time there were three little sisters; and their names were
    # <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    # <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    # <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    # and they lived at the bottom of a well.</p>

    # <p class="story">...</p>
    # """
    # soup  = BeautifulSoup(html_doc,"html.parser")
    # type(soup)
    # print(soup.prettify())


def print_element(element):
    if(isinstance(element, Tag)):
        print(f'{type(element).__name__}<{element.anem}>')
    if isinstance(element, NavigableString):
        print(type(element).__name__)

def print_element_list(element_list):
    print('[')
    for element in element_list:
        print_element(element)
    print(']')

def iterative_DFS(root):
    stack = [root]

    while(stack):
        element = stack.pop()
        if isinstance(element, NavigableString):
            print(element, end='')
        else:
            children = reversed(element.contents)
            stack.extend(children)

main()
