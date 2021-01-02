# Lululemon Inventory Scraper
Find OOS items in-store with web scraping

Since only the app shows all stores with inventory, and items out of stock online don't show up in the app, need to check through all store locations in browser to find stock. But guessing cities is difficult (like how I forget to check Victoria, BC every time).

Python script does the following:
- Gets all cities with stores throughout Canada
- For a particular item, checks every city for inventory and outputs them all at the end

## Pre-run Instructions:
Requirements: 
* Chrome 87
* Windows

If not on Windows, just get the appropriate OS binary [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and fix line 10. Similarly, can switch Chrome to a different browser, and also fix line 10.

Install Selenium:
``` pip install selenium ```

## Run Instructions:
```python inventory.py```

When prompted, type the full URL.
Example: ```https://shop.lululemon.com/p/womens-joggers/Dance-Studio-Jogger-29/_/prod9000211?color=47780&sz=10```

After execution finishes, will output a list of all stores with stock (add in phone numbers later).

Like all web scrapers, might break if the site changes ¯\\_( ͠° ͟ʖ °͠ )_/¯
