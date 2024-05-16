from time import sleep
from typing import List
import requests
from bs4 import BeautifulSoup


job_url='https://h1bdata.info/index.php?em={}&job=&city=&year=2023'

class H1BScraper:
    def scrape_job(self, company_name):
        print(f"read jobId:{company_name}")

        resp = requests.get(job_url.format(company_name))
        if resp.status_code != 200:
            sleep(1)
            return  self.scrape_job(company_name) 
        soup = BeautifulSoup(resp.text,'html.parser')
        
        self.write_html_to_file(soup)
                        
        try: 
            help_string = soup.find("p",{"class":"help-block"}).text.strip()
        except:
            help_string = None
            
        try: 
            company_name = soup.find("table",{"class":"tablesorter tablesorter-blue hasStickyHeaders"}).find_all('a')
            company_name = company_name[0].text.strip()
        except:
            company_name = None
            

        help_string = help_string.replace("percents", "percent").replace("records was found", "approved H1B records in 2023")
        print(help_string)
        print(company_name)
        
        
    def scrape_companies(self) -> List[str]:
        resp = requests.get('https://h1bdata.info/topcompanies.php')
        soup = BeautifulSoup(resp.text,'html.parser')
        
        # self.write_html_to_file(soup)
        try: 
            company_names = []
            links = soup.find("table",{"class":"table"}).find_all('a')
            i =1
            for company_name in links:
                if i%2 != 0:
                    company_names.append(company_name.text)
                i+=1
        except:
            company_names = None
            

        return company_names

    def write_html_to_file(self, soup):
        html = soup.prettify()  #bs is your BeautifulSoup object
        with open("html.html","w") as out:
            for i in range(0, len(html)):
                try:
                    out.write(html[i])
                except Exception:
                    1+1
                    
                    
H1BScraper().scrape_job(company_name="CBRE")
# H1BScraper().scrape_companies()
