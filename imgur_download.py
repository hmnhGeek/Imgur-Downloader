'''
    Script: imgur_download.py
    Author: Himanshu Sharma
    Description: Takes a keyword as input and downloads
                 all images related to that keyword from imgur.com.
'''

import requests, bs4, os

def scrape_images(keyword, quantity = 1):
    url = 'https://imgur.com/search?q='+keyword
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text)

    cwd = os.getcwd()
    
    if not os.path.isdir(cwd+'/'+keyword):
        # create a new directory for the images to be saved.
        os.mkdir(cwd+'/'+keyword)
    
    # Change the path to the directory where images are to be stored.
    os.chdir(cwd+'/'+keyword)

    #initialise a counter variable to keep track of the number of images downloaded.
    counter = 0

    # find all the <img> tags in the source-code.
    for a in soup.findAll('a', attrs = {'class':'image-list-link'}):
        
        # find sublink for the images which has the full resolution.
        sublink = 'https://www.imgur.com'+a.attrs['href']

        subsoup = bs4.BeautifulSoup(requests.get(sublink).text)
        for img in subsoup.findAll('img', attrs = {'itemprop':'contentURL'}):
            # check how many images are downloaded here.
            if counter != quantity:
                
                source = 'http:'+img.attrs['src']
                print source

                # create a new binary file for the image data to be written in it.
                # basename module takes in the name of the image from the url itself.
                
                with open(os.path.basename(source), 'wb') as f:
                    f.write(requests.get(source).content)
                counter += 1
            break

        if counter == quantity:
            break
        

    print "Number of images downloaded = "+str(counter)+'.'
