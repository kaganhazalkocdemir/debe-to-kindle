# coding=utf-8
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import time
from datetime import date, datetime, timedelta
import codecs

session = HTMLSession()


def get_debe():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

	eksi_debe = requests.get('https://eksisozluk.com/m/debe', headers=headers)
	soup = BeautifulSoup(eksi_debe.text, 'lxml')
	content_debe = soup.find("section", id="content-body").find_all("li")

	todaysdebe = {'links': [], 'debe_names': [], 'debe_content': [], 'tarih-saat': [], 'yazar': [], 'yazarlink': [],
				  'etiketler': []}

	for debe in content_debe:
		debe_names = debe.span.string
		debe_links = debe.a["href"]
		todaysdebe['links'].append(debe_links.replace("/entry/", "https://eksisozluk.com/entry/"))
		todaysdebe['debe_names'].append(debe_names)
	time.sleep(2)
	for link in todaysdebe['links']:
		try:
			get_debe = BeautifulSoup(session.get(link).content, 'lxml')
			debe_i = get_debe.find("ul", id="entry-item-list").li.div
			todaysdebe['debe_content'].append(str(debe_i).replace('href="/?q=', 'href="https://eksisozluk.com/?q='))
			todaysdebe['tarih-saat'].append(str(get_debe.find("footer").find('a', class_="entry-date permalink").text))
			todaysdebe['yazar'].append(str(get_debe.find("footer").find('a', class_="entry-author").text))
			todaysdebe['yazarlink'].append(str(get_debe.find("footer").find('a', class_="entry-author").get('href'))
										   .replace('/biri/','https://https://eksisozluk.com/biri/'))
			todaysdebe['etiketler'].append(get_debe.find('section', id='hidden-channels').text.strip())
		except AttributeError:
			print("Ups. Veriyi alamadık tam.")
			break
	return todaysdebe

def create_html(data):
	checklist = [len(data[n]) for i, n in enumerate(data)]
	if checklist.count(checklist[0]) == len(checklist):
		if 0 < datetime.today().hour < 7:
			debedate = (date.today() - timedelta(days=1)).strftime("%d-%m-%Y")
		else:
			debedate = date.today().strftime("%d-%m-%Y")
		head = """<html>
		<head>
			<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
			<title>Ekşi Sözlük - Dünün En Beğenilen Entry'leri - {debedate}</title>
			<guide>
				<reference type="toc" title="Table of Contents" filepos=0000867758/>
			</guide>
		</head>
		<body>
		<mbp:pagebreak/>
		<a id="toc"/>
		<p height="2em" width="0pt" align="center"><font size="5"><b>Dünün En Beğenilen Entry'leri - {debedate}</b>
		</font></p>

		<ol width="0pt">""".format(debedate=debedate)

		debetoc, debecontent = "", ""
		for i, n in enumerate(data['debe_content']):
			debe_baslik, debecontenti, debe_link = data['debe_names'][i], data['debe_content'][i], data['links'][i]
			debe_tarihs, debeyazar, dyazarlink = data['tarih-saat'][i], data['yazar'][i], data['yazarlink'][i]
			debe_etiketler = data['etiketler'][i]

			debetoc += f"""<li value="{i + 1}" height="0pt" width="0pt"><a href="#debe{i + 1}">{debe_baslik}</a></li>\n"""
			debecontent += f"""
			<mbp:pagebreak/>
			<a id="debe{i + 1}"/>
			<p height="4em" width="0pt"><a href="#toc"><font size="6"><font color="#000000">{debe_baslik}</font>
			</font></a>
			<br> ({debe_tarihs} <a href="{dyazarlink}"> {debeyazar} </a>)
			</p>
			<p height="4em" width="0pt" align="justify">
			{debecontenti}
			<p> ( Etiketler : {debe_etiketler}  | <a href="{debe_link}">{debe_link}</a> )
			</p>
			"""
		full_html = head + debetoc + "</ol>" + debecontent + "</body></html>"

		debefilename = "Eksisozluk DEBE - " + str(date.today()) + ".html"
		with codecs.open(debefilename, "w", "utf-8") as file:
			file.write(full_html)
	else:
		print("Veri eksik çıktı :/")

create_html(get_debe())
