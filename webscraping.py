from bs4 import BeautifulSoup as bsp4 # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"


soup =bsp4(html, "html.parser")

print(soup.prettify())

print("test")

tag_object=soup.title
print("tag object:",tag_object)


tag_object=soup.h3
print("tag object h3", tag_object)

tag_child =tag_object.b
print("TAG CHILD: ",tag_child)


parent_tag=tag_child.parent
print("tag child parent: ",parent_tag)

tag_object
tag_object.parent


sibling_1=tag_object.next_sibling
print(sibling_1)