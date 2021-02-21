from bs4 import BeautifulSoup
import requests
import csv

# with open('sample.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')  #Creating BeautifulSoup object...Input xml file and format in which to parse

# print(soup)  #print input file in xml format

# print(soup.prettify())  #Show which tags are nested inside the other

# title1 = soup.title.text   #Prints the title tag text in the html
# print(title1)


# div = soup.find('div', class_='footer')  #Print div tag of footer class
# print(div)


# article = soup.find('div', class_='article') #Print first div tag of article class
# # print(article)
#
# headline = article.h2.a.text   #Print text of specific tag
# print(headline)


source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

csv_file =  open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

# print(soup.prettify())

for article in soup.find_all('article'):
    # print(article.prettify())

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # print(vid_src)

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # print(vid_id)

        yt_link = f'https://youtube.com/watch?v={vid_id}'

    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()