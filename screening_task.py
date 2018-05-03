import urllib.request
from urllib.parse import urlparse
import bs4
import re

#check website page
def url_size(website):
    try:
        #get website's content, and its length
        with urllib.request.urlopen(website) as url:
            return "Size: " + str(len(url.read()))
    except:
        # check exception if wrong website input given
        return "Check your website, can not get size. "

# find number of links pointing to specific domain
def find_links(website):
    try:
        #get website's content, and its length
        with urllib.request.urlopen(website) as url:
            #get html file
            response = url.read()
            #find all hyperlinks
            link_parser = bs4.SoupStrainer('a')
            #get 2 regex with http and https
            parsed_url = urlparse(website).netloc
            regex1 = re.compile(website)
            regex2 = re.compile("https://" + parsed_url)
            link_count = 0
            all_links = []
            #find links that  points to our domain
            for link in bs4.BeautifulSoup(response, "html.parser", parse_only=link_parser):
                #check only hyperlinks
                if link.has_attr("href"):
                    hyper_link1 = regex1.findall(str(link["href"]))
                    hyper_link2 = regex2.findall(str(link["href"]))
                    # find hyperlinks that matches regex
                    if hyper_link1:
                        link_count += 1
                        all_links.append(str(link["href"]))
                    if hyper_link2:
                        link_count += 1
                        all_links.append(str(link["href"]))
            return (all_links, link_count)

    except:
        # check exception if wrong website input given
        return "Check your website, can not retrieve information. "

def screening_task(website):
    print(website)
    print(url_size(website))
    links = find_links(website)
    print("Number of links: " + str(links[1]))
    print("All links: ")
    for link in links[0]:
        print("   " + link)

# testing
if __name__ == "__main__":
    print(screening_task('http://www.rleonardi.com/'))