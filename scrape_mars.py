


import os
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd


#Unlike Jupyter Im using this version of executable_path so it can be run without issue.

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# ## Connecting to the Nasa Url

nasaurl = "https://mars.nasa.gov/news/"
browser.visit(nasaurl)
html = browser.html
nsoup = bs(html, 'html.parser')

#Unlike Jupyter we need to capture everything to put in a mongodb

Marsmon = {}

# ## Things that are identified before obtaining the information we need through code
# ### Inspect the Webpage 
# #### item_list - is where the titles and paragraph are located
# #### slide to get each individual slides or news article
# #### content_title is what we need to get a title
# #### "article_teaser_body" is the class to get a paragraph



# Get the lastest 5 titles om the page. I would prefer if i can loop this this but for now this will do. I went through many variations of this code, and none of them went the way I wanted them.  
Ntitle0 = nsoup.find_all("div", class_ = "content_title")[0].text
Ntitle1 = nsoup.find_all("div", class_ = "content_title")[1].text
Ntitle2 = nsoup.find_all("div", class_ = "content_title")[2].text
Ntitle3 = nsoup.find_all("div", class_ = "content_title")[3].text
Ntitle4 = nsoup.find_all("div", class_ = "content_title")[4].text




# Get the 5 latest paragraphs of the page I would prefer if i can loop this this but for now this will do. 
Npar0 = nsoup.find_all('div', class_="article_teaser_body")[0].text
Npar1 = nsoup.find_all('div', class_="article_teaser_body")[1].text
Npar2 = nsoup.find_all('div', class_="article_teaser_body")[2].text
Npar3 = nsoup.find_all('div', class_="article_teaser_body")[3].text
Npar4 = nsoup.find_all('div', class_="article_teaser_body")[4].text


#I would prefer to to do a for a loop that would capture the title and paragraph on the same loop. But i couldnt figure it out. So this will do. Either way the result i intended would have been the same. 


# Print the captured Variables and putting them in readable format. the print(" ") is just so i can have an empty space as a seperator between each article/summary group
print(f"News Title: " + Ntitle0)
print(f"Brief Summary: " + Npar0)
print(" ")
print(f"News Title: " + Ntitle1)
print(f"Brief Summary: " + Npar1)
print(" ")
print(f"News Title: " + Ntitle2)
print(f"Brief Summary: " + Npar2)
print(" ")
print(f"News Title: " + Ntitle3)
print(f"Brief Summary: " + Npar3)
print(" ")
print(f"News Title: " + Ntitle4)
print(f"Brief Summary: " + Npar4)

#In Jupyter I did a print statement. Over hear I will capture this through a dictionary. It will be easier for me.
marstp = {Ntitle0:Npar0, Ntitle1:Npar1, Ntitle2:Npar2, Ntitle3:Npar3, Ntitle4:Npar4}

Marsmon[" Mission to Mars Articles"] = marstp

# Images Scraping
#setting up the scrap. By visiting the Website to scrap the image

marspicurl = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
browser.visit(marspicurl)
phtml = browser.html
psoup = bs(phtml, 'html.parser')

#since I already I identified the link the featured image all i have to do is code it. Technically i dont have to do anything beyond this 
featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg'
print(featured_image_url)

Marsmon["Featured Image"] = featured_image_url


# # Mars Data Frame
# ## Scrapping the page to obtain the diameter, weight, mass
# ### Location of all the is in the class  is tabled id = "tablepress-comp-mars"
#Connect to the Space Facts / Mars Page
marsfacturl= "https://space-facts.com/mars/"

#Reading the website through pandas
mars_read = pd.read_html(marsfacturl)
print(mars_read)

#The item we want is 0.
MarsFact_df = mars_read[0]
MarsFact_df

#Renaming the Column Names to give it a better description
MarsFact_df.columns = ["Data Types" , "Data Values"]
MarsFact_df
MarsHTable = MarsFact_df.to_html()
Marsmon["Mars Facts"] = MarsHTable 

#I just wanted to bring up the comparison with Earth
MarsEarthFact_df = mars_read[1]
MarsEarthFact_df
#Saving the camparisont to HTMl Table


#Both 0 and 1 would have answered the questions. With about a 4 row difference, and 2 of the the rows in 1 are irrelavant to Earth. 

# Hemisphere Link Scraping
#setting up the page to scrape
hemiurl = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemiurl)
hhtml = browser.html
hsoup = bs(hhtml, 'html.parser')

# Obtaining the links andv put all those commentted section ins a dictionary. 
MarsHemisphere = { "Cereberus" :" https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg",
"Schiaparelli" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg",
"Syrtis Major" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg",
"Valles Marineris" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg "}
print(MarsHemisphere)