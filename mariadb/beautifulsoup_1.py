from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
'''
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link3'))

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())
a=soup.get_text()
print(a)
print(type(a))

tag = soup.a
print(type(tag))

print(tag.name)
tag.name="block quote"
print(soup) # tag 이름이 바뀜  a->block quote

print(tag['id'])
print(tag.attrs)

tag['id'] = 'verybold'
tag['another-attribute'] = 1
print(tag)

del tag['id']
del tag['another-attribute']
print(tag)

tag['id']
print(tag.get('id'))
'''
'''
att1 = soup.a['class']
print(att1)

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
print(rel_soup.prettify())
tag=rel_soup.a
print(tag.string)
print(type(tag.string))
tag.string.replace_with('홈페이지')
print(tag)
'''
'''
print(rel_soup.a['rel'])
# ['index']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
'''
'''
tag=soup.body
print(tag.contents)
print(len(tag.contents))
print(tag.contents[5])
'''
'''
for child in tag.children:
    print(child)
'''
'''
print(len(list(tag.children)))
print(len(list(tag.descendants)))
'''
print(soup.select("title"))
# [<title>The Dormouse's story</title>]

print(soup.select("p:nth-of-type(3)"))
# [<p class="story">...</p>]

print(soup.select("body a"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.select("html head title"))
# [<title>The Dormouse's story</title>]

print(soup.select("head > title"))
# [<title>The Dormouse's story</title>]

print(soup.select("p > a"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.select("p > a:nth-of-type(2)"))
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

print(soup.select("p > #link1"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

print(soup.select("body > a"))
# []
