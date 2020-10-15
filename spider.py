import re, os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

url = 'https://wmathor.com/admin/manage-posts.php'
folder_path="D:\\blog\\"    
cookies = {
    'cookie':'__gads=ID=11ae0698092d435f-22d563a103c30006:T=1597577131:RT=1597577131:S=ALNI_MaWofxAYcYAZYHwqak3V7b9v3exmw; PHPSESSID=kh181pufibbbk3pml928ir7qt9; 42dba681692dfe704cefb5aef6745f7e__post_views=17%2C1498%2C756%2C754%2C1176%2C1436; 42dba681692dfe704cefb5aef6745f7e__typecho_uid=1; 42dba681692dfe704cefb5aef6745f7e__typecho_authCode=%24T%24V2HjYwClXf5a4af603343261fdf44ae6578db6939',
}

def mkdir(path):
    '''Create a folder
    Args:
        path: str
    
    Returns:
        None
    '''
    try:
        folder = os.path.exists(path)
        os.makedirs(path) # makedirs 创建文件时如果路径不存在会创建这个路径
    except BaseException:
        pass

def check(name):
    '''Filter out characters that are not allowed in windows system
    Args:
        name: str
    
    Returns:
        Filtering strings after special characters
    '''
    return name.replace('\\', ' ').replace('/', ' ').replace(':', ' ').replace('*', ' ').replace('?', ' ').replace('<', ' ').replace('>', ' ').replace('|', ' ')


def save(content, article_title, article_category):
    '''Save content to a file. The file name is article_tile.md
    Args:
        content: str
        article_title: str
        article_category: str
    
    Returns:
        None
    '''
    save_name = folder_path + check(article_category) + '\\' + check(article_title) + '.md'
    with open(save_name, 'w', encoding='utf-8') as f:
        f.write(content)


def get_articles(new_url, session):
    '''Get all the articles' information in new_url
    Args:
        new_url: str
        session: session
    
    Returns:
        None
    '''
    # get article information
    response = session.get(new_url)
    soup = BeautifulSoup(response.text, 'lxml')
    tr_iter = soup.tbody.tr.next_siblings
    for tr in tr_iter:
        if isinstance(tr, Tag):
            # print(tr.contents)
            article_url = tr.contents[5].a['href']
            article_title = tr.contents[5].a.contents[0]
            article_category = tr.contents[-4].a.contents[0]

            # get article content
            response = session.get(article_url)
            soup = BeautifulSoup(response.text, 'lxml')
            if len(soup.textarea.contents) != 0:
                content = str(soup.textarea.contents[0]).replace('\n', '')
            else:
                content = ' '
            save(content, article_title, article_category)
    

def main(url, page_number_start=1, page_number_end=1):
    '''
    Args:
        page_number_start: int. The start number of article pages you want to get
        page_number_end: int. The end number of article pages you want to get
        folder_path: str. The path of all articels you want to save
    
    Returns:
        None
    '''

    # login
    session = requests.session()
    requests.utils.add_dict_to_cookiejar(session.cookies, cookies)
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    categories = soup.find_all('option')

    # new folder
    mkdir(folder_path)
    for category in categories[1:]:
        folder_name = re.findall(r'>(.*?)<', str(category))[0]
        mkdir(folder_path + check(folder_name))
    print('---- Folder Creation Complete ----')
    
    # get all articles
    for page in range(page_number_start, page_number_end + 1):
        new_url = url + '?page=' + str(page)
        get_articles(new_url, session)
        print('Page {} Complete'.format(page))

if __name__ == '__main__':
    main(url, page_number_start=1, page_number_end=34)