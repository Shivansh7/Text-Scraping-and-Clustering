
# coding: utf-8



#COMP41680 Assignment 2 (Part1): Text Scraping and Clustering
#Shivansh Bhandari(16204820)
# Part 1: Text Data Scraping

# Import the required packages
from bs4 import BeautifulSoup
import urllib.request



# The link to the site from whihc the data is to be scraped
url="http://mlg.ucd.ie/modules/COMP41680/news/index.html"
# Open the file to write the collected text
file = open("Articles_Text.txt","w",encoding ="utf-8") 


# method to extract hrefs from the homepage 
def get_address(url):
    response= urllib.request.urlopen(url)
    # parse the response of each request using html parser
    soup = BeautifulSoup(response, 'html.parser')
    # Extract the hrefs from the div whose class is main
    homepage_div=soup.find_all('div',{"class":"main"})
    for div in homepage_div:
        # Find all the tag 'a' in div
        homepage_links=div.find_all('a')
    month_address(homepage_links)

# Method to extract hrefs for articles of each month    
def month_address(homepage_links):
    # A list to store the hrefs from the hoimepage
    listHref=[]
    for link in homepage_links:
        # get the hrefs from each 'a' tag and append the hrefs in the list listHref
        listHref.append(link.get('href'))
    for months in listHref:
        #generate a URL using the hrefs in listHrefs
        monthurl="http://mlg.ucd.ie/modules/COMP41680/news/"+str(months)
        monthwise_response= urllib.request.urlopen(monthurl)
        #parse the response of each request suing html parser
        monthwise_soup = BeautifulSoup(monthwise_response, 'html.parser')
        # Extract the hrefs from the div whose class is main
        monthwise_div=monthwise_soup.find_all('div',{"class":"main"})
        for divs in monthwise_div:
            #Find all the tag 'a' in div
            article_links=divs.find_all('a')
        extract_articles(article_links)
        
def extract_articles(article_links):
        # A list to store the hrefs of the articles page
        articleHref = []
        for links in article_links:
            #get the hrefs from each 'a' tag and append the hrefs in the list articleHref
            articleHref.append(links.get('href'))
        for articles in articleHref:
            #generate a URL using the hrefs in articleHrefs
            article_url="http://mlg.ucd.ie/modules/COMP41680/news/"+str(articles)
            article_response= urllib.request.urlopen(article_url)
            #parse the response of each request using html parser
            article_soup=BeautifulSoup(article_response,'html.parser')
            # Delete the content of 'p' tag whihc belongs to class 'notice'
            article_soup.find('p',class_='notice').decompose()
            for text in article_soup.find_all('p'):
                # Get the text in the tag 'p' of the html page
                article_text=text.getText()
                # Write the text in the text file
                file.writelines(article_text)
            file.write("\n")
            
def main():
    print("Scraping text please wait....")
    get_address(url)  
    file.close()
    print("Scraping Completed ")
    
                       
if __name__=="__main__":           
    main()



