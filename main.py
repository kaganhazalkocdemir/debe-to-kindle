# coding=utf-8
import codecs
import random
import time
from datetime import date, datetime, timedelta

from bs4 import BeautifulSoup
from requests_html import HTMLSession


def main():
    debe_list = get_debe()
    html_content = create_html(debe_list)

    file_name = "Eksisozluk DEBE - " + str(date.today()) + ".html"

    with codecs.open(file_name, "w", "utf-8") as file:
        file.write(html_content)


def get_debe():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

    session = HTMLSession()

    eksi_debe = session.get('https://eksisozluk.com/m/debe', headers=headers)
    soup = BeautifulSoup(eksi_debe.text, 'lxml')

    debe_list = []

    for debe in soup.find("section", id="content-body").find_all("li"):
        debe_names = debe.span.string
        debe_link = debe.a["href"]

        debe_list.append({
            "url": f"https://eksisozluk.com{debe_link}",
            "title": debe_names
        })

    debe_list_full = []

    for debe_item in debe_list[:4]:
        try:
            raw_data = session.get(debe_item['url']).content
            soup = BeautifulSoup(raw_data, 'lxml')

            elem = soup.find("ul", id="entry-item-list").li.div

            content = str(elem).replace('href="/?q=', 'href="https://eksisozluk.com/?q=')
            entry_date = str(soup.find("footer").find('a', class_="entry-date permalink").text)
            author = str(soup.find("footer").find('a', class_="entry-author").text)
            author_url = (str(soup.find("footer").find('a', class_="entry-author").get('href'))
                          .replace('/biri/', 'https://https://eksisozluk.com/biri/'))
            tags = soup.find('section', id='hidden-channels').text.strip()

            debe_item['content'] = content
            debe_item['entry_date'] = entry_date
            debe_item['author'] = author
            debe_item['author_url'] = author_url
            debe_item['tags'] = tags

            debe_list_full.append(debe_item)

            time.sleep(random.randint(2, 5))
        except AttributeError as e:
            print("Ups. Veriyi alamadık tam.")
            raise e

    return debe_list_full


def create_html(data):
    if 0 < datetime.today().hour < 7:
        debedate = (date.today() - timedelta(days=1)).strftime("%d-%m-%Y")
    else:
        debedate = date.today().strftime("%d-%m-%Y")

    head = """
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
        <title>Ekşi Sözlük - Dünün En Beğenilen Entry'leri - {debedate}</title>
        <guide>
            <reference type="toc" title="Table of Contents" filepos=0000867758/>
        </guide>
    </head>
    """

    body = f"""
    <body>
        <mbp:pagebreak/>
        <a id="toc"/>
        <p height="2em" width="0pt" align="center"><font size="5"><b>Dünün En Beğenilen Entry'leri - {debedate}</b>
        </font></p>
    
        <ol width="0pt">
    """.format(debedate=debedate)

    toc, content = "", ""

    for i, item in enumerate(data):
        toc += f"""
            <li value="{i + 1}" height="0pt" width="0pt">
                <a href="#debe{i + 1}">{item['title']}</a>
            </li>\n
        """

        content += f"""
        <mbp:pagebreak/>

        <a id="debe{i + 1}" />

        <p height="4em" width="0pt">
            <a href="#toc">
                <font size="6">
                    <font color="#000000">{item['title']}</font>
                </font>
            </a>

            <br /> 

            ({item['entry_date']} <a href="{item['author_url']}"> {item['author']} </a>)
        </p>

        <p height="4em" width="0pt" align="justify" />

        {item['content']}

        <p> ( Etiketler : {item['tags']}  | <a href="{item['url']}">{item['url']}</a> )</p>
        """

    full_html = "<html>" + head + body + toc + "</ol>" + content + "</body></html>"

    return full_html


main()
