from selenium import webdriver
import webbrowser

browser = webdriver.Firefox('usr/local/bin')
webbrowser.open('https://speechnotes.co/')
elem = browser.find_element_by_css_selector('Copy the CSS Selector of the Mic and paste here. Install Firefox on Raspbian, and get the CSS Selector of the mic')

elem.click()



#Now what I am doing is saving the object returned by the webdriver.Firefox() and then opening the website with get(). 
#Then, I am using the css selector to find the exact location of the mic and saving it in 'elem'
#The elem will have many functions, but since I only need to turn it on by clicking, to click on that I am using elem.click()

