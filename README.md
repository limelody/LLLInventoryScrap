# Lululemon Inventory Scraper
Find OOS items in-store with web scraping

Since only the app shows all stores with inventory, and items out of stock online don't show up in the app, need to check through all store locations in browser to find stock. But guessing cities is difficult (like how I forget to check Victoria, BC every time).

Python script does the following:
- Gets all cities with stores throughout Canada
- For a particular item, checks every city for inventory and outputs them all at the end

## Pre-run Instructions:
1. Install Selenium:
``` pip install selenium ```
