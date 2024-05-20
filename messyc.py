from bs4 import BeautifulSoup
import requests
target_website = "https://scrapeme.live/shop/page/1/" # Enter website here
target_page = requests.get(target_website)
soup = BeautifulSoup(target_page.text, 'html.parser')
with open("Output.txt", "w") as text_file:
    text_file.write("--"+ target_website +"--\n" )


#dont know to how to get pages . u'll have to type ir urself :skull:
page_numb = 48  # enter your pages number
number = 0 #"Finds"(counted files) starting number
start_numb = 1 #pages starting number
for x in range(page_numb):
 target_page_in = requests.get("https://scrapeme.live/shop/page/"+ str(start_numb) +"/")
 soup = BeautifulSoup(target_page_in.text, 'html.parser')
 
 titles = soup.findAll('h2', attrs={'class':'woocommerce-loop-product__title'})
 prices = soup.findAll ("span", attrs={"class":"price"})
 print (start_numb)
 start_numb +=1
 #loops to print all the finds and counts them
 for title,price in zip(titles, prices):
  number += 1
  with open("Output.txt", "a") as text_file:
   print (title.text + "--" + price.text)
   text_file.write (title.text + "--" + price.text +"\n")
  
print ("Finds:" + str(number)) # prints the counted finds

