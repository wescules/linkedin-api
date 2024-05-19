from time import sleep
from typing import List
import requests
from bs4 import BeautifulSoup


job_url='https://h1bdata.info/index.php?em={}&job=&city=&year=2023'

class H1BScraper:
    async def scrape_job(self, company_name:str) -> tuple:
        company_name = company_name.replace(" ", "%20")
        print(f"read company_name:{company_name}")
        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'ezoab_73160=mod94-c; ezosuibasgeneris-1=3950a267-d579-417c-5fcc-04b921254ffb; ezds=ffid%3D1%2Cw%3D2560%2Ch%3D1440; _gid=GA1.2.392303287.1715819269; _sharedid=9b7fc9b0-5970-4b36-bf8b-7aef0c520e49; _sharedid_cst=zix7LPQsHA%3D%3D; _cc_id=1b5f9f47b5e415ac1a114f0472adfcb2; panoramaIdType=panoIndiv; _pbjs_userid_consent_data=3524755945110770; panoramaId_expiry=1715905672810; pbjs-unifiedid=%7B%22TDID%22%3A%220e5eb463-1217-4e84-8df4-f53fbeb80213%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-04-16T00%3A27%3A52%22%7D; pbjs-unifiedid_cst=zix7LPQsHA%3D%3D; __qca=P0-1160528939-1715819275136; __gads=ID=17c661f4a46bf763:T=1715823669:RT=1715823669:S=ALNI_Ma0kOgxAgrsIs9S1cVeKNeaYPuRHQ; __gpi=UID=00000e06b615ef94:T=1715823669:RT=1715823669:S=ALNI_MZNJUd4SnsrrlIpoAASNimWwhOGeg; __eoi=ID=ba552a2efd41fe50:T=1715823669:RT=1715823669:S=AA-AfjYTqRsfzIzD7sb4amqxN2nx; ezohw=w%3D2560%2Ch%3D1326; ezoadgid_73160=-2; lp_73160=https://h1bdata.info/index.php?em=meta&job=&city=&year=2023; ezovuuid_73160=3171ec9e-eaa5-46ad-66a1-10af0eed76cb; ezoref_73160=; _au_1d=AU1D-0100-001715835711-2HMG91H0-26JD; active_template::73160=pub_site.1715837077; ezopvc_73160=10; ezovuuidtime_73160=1715837077; _ga_Q3WTCGM1NM=GS1.1.1715835710.3.1.1715837078.37.0.0; _ga=GA1.1.1524273485.1715819269; ezux_lpl_73160=1715837078682|aff01a62-080d-420e-4971-7cee45cc58bb|true; cto_bundle=ffpHRl9VQ2p5Q3J4NkFvOUlaaWRhc0daNUR3aiUyRm9OdjFtOUpnZkoxUHRyNGIzSEhnOUozTXVENUxIajdWM1ZTUXY2QW1lWW03YlBXVUpWU1ZVYWoyTDJndnRPVjZMV3pkenlVald3ZjI4Z1RrN2VHRW5sSEZWZHRRZmZKZ2lxY0p6QXQ0TU9VRmxqZEFnVFYzNGhPMXY5MWRqeEpkVnJ0WldlZWUxVFMxQmxhTXZVVFpYQlVDblRqeiUyQlpsUXhkOWFteEFaZjJSJTJGT050ZWx0RzlWWUFSdkR3YyUyRnJTYzVoTUNQMWxBZHVETDN5REQzMWFGJTJGUzNEVXJ5SW84MGhzVTRNN1VmdUh6QWo5czNqZ2JxRm1IeElmTG9QUDBZQmVJWnJPRjQlMkY2VTcwNExkWkNBRUhTMWZzSjZSYiUyQk5XOU5mTzRqT2VF; cto_bidid=OnygAV8lMkZyeVF3cjRMTEpnVTVNRm9ab3dCTlUzcGQ2OXBaQ2cxUmFURmdSWUlEU2dnb09PNlRaRnZlNGRJSDFITlFub2l3STBuOXRXaVhqUEx1ckYza3VIc0l3UmdnME0zJTJGTnNUT213S3NaaDB0NDglM0Q'
        }
        resp = requests.get(job_url.format(company_name), headers=headers)
        if resp.status_code == 301:
            return ("", "")
        if resp.status_code != 200:
            print(resp)
            sleep(1)
            return await self.scrape_job(company_name) 
        soup = BeautifulSoup(resp.text,'html.parser')
        
        # self.write_html_to_file(soup)
                        
        try: 
            help_string = soup.find("p",{"class":"help-block"}).text.strip()
        except:
            help_string = None
            
        try: 
            company_legal_name = soup.find("table",{"class":"tablesorter tablesorter-blue hasStickyHeaders"}).find_all('a')
            company_legal_name = company_legal_name[0].text.strip()
        except:
            company_legal_name = None
            

        help_string = help_string.replace("percents", "percent").replace("records was found", "approved H1B records in 2023")
        print(help_string)
        if 'try search again' in help_string:
            return ("", "")
        return (help_string, company_legal_name)
        
        
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
            
        with open("output.txt", "a") as f:
            for company in company_names:
                f.write(company+'\n')
        return company_names

    def write_html_to_file(self, soup):
        html = soup.prettify()  #bs is your BeautifulSoup object
        with open("html.html","w") as out:
            for i in range(0, len(html)):
                try:
                    out.write(html[i])
                except Exception:
                    1+1
                    
                    
# H1BScraper().scrape_job(company_name="Abbott")
# H1BScraper().scrape_companies()
