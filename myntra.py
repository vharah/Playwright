import csv
import pandas as pd
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as m:
        browse = m.chromium.launch(headless= False)
        page = browse.new_page()
        page.goto('https://www.myntra.com/smart-watch-noise?-smart-watch-noise',timeout= 0)

        Smart_watch_name = page.query_selector_all('[class="product-productMetaInfo"]')
        Company = []
        Watch_name = []
        Price = []
        for i in Smart_watch_name:
            div = i.inner_text().split('\n')
            Company.append(div[0])
            Watch_name.append(div[1])
            Price.append(div[2])
            
        dic_={
            'Brand name':Company,
            'Watch name':Watch_name,
            'Price & Offer':Price,
        }        

        df = pd.DataFrame(dic_)
        df.to_csv('data.csv')

        page.wait_for_timeout(3000)
        page.close()
if __name__ == "__main__":
    main()
