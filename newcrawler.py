import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def is_valid_link(link, paragraph):
    """
    Checks whether a link is valid based on several criteria.
    """
    # Check if the link is a wiki link.
    href = link.get('href')
    if not (href and href.startswith('/wiki/')):
        return False

    # Check if the link is in parentheses in the paragraph text.
    if in_parentheses(link, paragraph):
        return False

    # Check if the link is italicized.
    if link.find_parent('i') or link.find_parent('em'):
        return False

    # Exclude administrative links and special pages on Wikipedia.
    administrative_sections = (':', 'Help:', 'Wikipedia:', 'File:', 'Portal:', 'Special:', 'Template:', 'Template_talk:', 'Draft:')
    if any(section in href for section in administrative_sections):
        return False

    # If the link passed all the checks, it is considered valid.
    return True

def in_parentheses(link, paragraph):
    """
    Checks if a link is within parentheses in the text.
    """
    # Get the text of the paragraph up to the link's position.
    text = str(paragraph)
    link_start = text.find(str(link))

    # Count the opening and closing parentheses before the link.
    count_open = text[:link_start].count('(')
    count_close = text[:link_start].count(')')

    return count_open > count_close  # True if the link is in parentheses.

# Usage within the context of the get_first_link function:
def get_first_link(soup):
    """
    Get the first valid link from a Wikipedia page.
    """
    paragraphs = soup.find_all('p')

    for paragraph in paragraphs:
        links = paragraph.find_all('a')

        for link in links:
            if is_valid_link(link, paragraph):
                return link.get('href')

    return None


# def get_first_link(soup):
#     for p in soup.find_all('p', recursive=False):
#         links = p.find_all('a', recursive=False)
#         for link in links:
#             if is_valid_link(link):
#                 return link.get('href')
#     return None

def find_philosophy(url, max_steps=30):
    visited_urls = set()
    for _ in range(max_steps):
        response = requests.get(url)
        if response.status_code != 200:
            print('Failed to fetch page')
            return False
        
        soup = BeautifulSoup(response.text, 'html.parser')
        first_link = get_first_link(soup)
        
        if not first_link:
            print('No valid link found')
            return False
        
        url = urljoin(url, first_link)
        
        if "Philosophy" in url:
            print('Philosophy page found!')
            return True
        
        if url in visited_urls:
            print('Loop detected')
            return False
        
        visited_urls.add(url)
        
    print('Maximum steps reached')
    return False

# Start URL
start_url = 'https://en.wikipedia.org/wiki/Special:Random'
find_philosophy(start_url)
