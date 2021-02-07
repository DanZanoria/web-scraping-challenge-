#!/usr/bin/env python
# coding: utf-8

# ## Imports And Setting UP the Jupyter

# In[15]:


import os
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd


# In[16]:



#I am having a lot of issues with chromedriver so im including both ways to get it

# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)

executable_path = {'executable_path':r"C:\Users\danza\.wdm\drivers\chromedriver\win32\88.0.4324.96\chromedriver.exe"}
browser = Browser('chrome', **executable_path, headless=False)


# ## Connecting to the Nasa Url

# In[17]:


nasaurl = "https://mars.nasa.gov/news/"

browser.visit(nasaurl)
html = browser.html
nsoup = bs(html, 'html.parser')
# I want to see if this works. After confirming it works it will be commented out since it has no further need for nsoup
# nsoup 


# ## Things that are identified before obtaining the information we need through code
# ### Inspect the Webpage 
# #### item_list - is where the titles and paragraph are located
# #### slide to get each individual slides or news article
# #### content_title is what we need to get a title
# #### "article_teaser_body" is the class to get a paragraph

# In[18]:



# Get the lastest 5 titles om the page. I would prefer if i can loop this this but for now this will do. I went through many variations of this code, and none of them went the way I wanted them.  
Ntitle0 = nsoup.find_all("div", class_ = "content_title")[0].text
Ntitle1 = nsoup.find_all("div", class_ = "content_title")[1].text
Ntitle2 = nsoup.find_all("div", class_ = "content_title")[2].text
Ntitle3 = nsoup.find_all("div", class_ = "content_title")[3].text
Ntitle4 = nsoup.find_all("div", class_ = "content_title")[4].text




# In[19]:



# Get the 5 latest paragraphs of the page I would prefer if i can loop this this but for now this will do. 
Npar0 = nsoup.find_all('div', class_="article_teaser_body")[0].text
Npar1 = nsoup.find_all('div', class_="article_teaser_body")[1].text
Npar2 = nsoup.find_all('div', class_="article_teaser_body")[2].text
Npar3 = nsoup.find_all('div', class_="article_teaser_body")[3].text
Npar4 = nsoup.find_all('div', class_="article_teaser_body")[4].text


#I would prefer to to do a for a loop that would capture the title and paragraph on the same loop. But i couldnt figure it out. So this will do. Either way the result i intended would have been the same. 


# In[20]:


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


# In[21]:


# Images Scraping
## Interesting Information before coding
### link to Featured Image 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg'
### overall class = header
### class = header-image



# In[22]:


#setting up the scrap. By visiting the Website to scrap the image
marspicurl = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
browser.visit(marspicurl)
phtml = browser.html
psoup = bs(phtml, 'html.parser')

#since I already I identified the link the featured image all i have to do is code it. Technically i dont have to do anything beyond this 
featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg'
print(featured_image_url)


# # Mars Data Frame
# ## Scrapping the page to obtain the diameter, weight, mass
# ### Location of all the is in the class  is tabled id = "tablepress-comp-mars"

# In[23]:


#Connect to the Space Facts / Mars Page
marsfacturl= "https://space-facts.com/mars/"


#Reading the website through pandas
mars_read = pd.read_html(marsfacturl)
mars_read


# In[24]:


#The item we want is 0.

MarsFact_df = mars_read[0]

MarsFact_df


# In[25]:


#Renaming the Column Names to give it a better description
MarsFact_df.columns = ["Data Types" , "Data Values"]
MarsFact_df


# In[26]:


#I just wanted to bring up the comparison with Earth
MarsEarthFact_df = mars_read[1]
MarsEarthFact_df

#Both 0 and 1 would have answered the questions. With about a 4 row difference, and 2 of the the rows in 1 are irrelavant to Earth. 


# In[27]:


# Hemisphere Link Scraping
# Not going to link to the website through this markdown like last time. I am purposelly keeping that error to remind this memo actually links things automatically


# In[30]:


#setting up the page to scrape

hemiurl = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemiurl)
hhtml = browser.html
hsoup = bs(hhtml, 'html.parser')


# In[34]:


# Obtaining the links andv put all those commentted section ins a dictionary. 

MarsHemisphere = { "Cereberus" :" https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg",
"Schiaparelli" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg",
"Syrtis Major" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg",
"Valles Marineris" : "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg "}

MarsHemisphere


# In[ ]:




