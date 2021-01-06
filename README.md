# Lululemon Inventory Scraper
Find OOS items in-store with web scraping

Since only the app shows all stores with inventory, and items out of stock online don't show up in the app, need to check through all store locations in browser to find stock. But guessing cities is difficult (like how I forget to check Victoria, BC every time).

Python script does the following:
- Gets all cities with stores throughout Canada (this is bad design, should fix this. but i hate text files)
- For a particular item (colour + size), checks every city for inventory and outputs all stores with stock at the end

## Pre-run Instructions:
Requirements: 
* Chrome 87
* Windows

Install the appropriate chromedriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). If not on Windows, just get the appropriate OS binary and fix line 10 to be the path to where it's located. Similarly, can switch Chrome to a different browser, and also fix line 10 to be `webdriver.Firefox()` or something.

Install Selenium:
``` pip install selenium ```

## Run Instructions:
```python inventory.py```

When prompted, type the full URL (with colour and size selected).
Example: ```https://shop.lululemon.com/p/womens-joggers/Dance-Studio-Jogger-29/_/prod9000211?color=47780&sz=10```
(I know this is also bad design but it's easier for me to run on subsequent different items because who in the right mind is going to check the same item over and over again)
After execution finishes, will output a list of all stores with stock (add in phone numbers later).

Like all web scrapers, might break if the site changes ¯\\\_( ͠° ͟ʖ °͠ )\_/¯
