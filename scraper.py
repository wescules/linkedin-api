import requests
import logging
from bs4 import BeautifulSoup

# jobId = "3841566189"
# url = 'https://www.linkedin.com/jobs/search/?currentJobId={jobId}'


# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'lxml')

# wrapper = soup.find('li', class_="job-details-jobs-unified-top-card__job-insight")



# html = soup.prettify()  #bs is your BeautifulSoup object
# with open("html.html","w") as out:
#     for i in range(0, len(html)):
#         try:
#             out.write(html[i])
#         except Exception:
#             1+1
# print(soup)
# print(wrapper)







def remove_tags(html):
    '''remove html tags from BeautifulSoup.text'''
 
    soup = BeautifulSoup(html, "html.parser")
 
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

list_job_IDs = ["3841566189"]
job_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
job={}
list_jobs=[]

for j in range(0,len(list_job_IDs)):
    print(f"{j+1} ... read jobId:{list_job_IDs[j]}")

    resp = requests.get(job_url.format(list_job_IDs[j]))
    soup=BeautifulSoup(resp.text,'html.parser')
    html = soup.prettify()  #bs is your BeautifulSoup object
    with open("html.html","w") as out:
        for i in range(0, len(html)):
            try:
                out.write(html[i])
            except Exception:
                1+1

    job["Job_ID"] = list_job_IDs[j] 
    
    try: 
        job["Job_txt"] = remove_tags(resp.content)
    except:
        job["Job_txt"] = None
    
    try:
        job["company"]=soup.find("div",{"class":"top-card-layout__card"}).find("a").find("img").get('alt')
    except:
        job["company"]=None

    try:
        job["job-title"]=soup.find("div",{"class":"top-card-layout__entity-info"}).find("a").text.strip()
    except:
        job["job-title"]=None

    try:
        job["level"]=soup.find("ul",{"class":"description__job-criteria-list"}).find("li").text.replace("Seniority level","").strip()
    except:
        job["level"]=None

    try:
        job["location"]=soup.find("span",{"class":"topcard__flavor topcard__flavor--bullet"}).text.strip()
    except:
        job["location"]=None

    try:
        job["posted-time-ago"]=soup.find("span",{"class":"posted-time-ago__text topcard__flavor--metadata"}).text.strip()
    except:
        job["posted-time-ago"]=None

    try:
        nb_candidats = soup.find("span",{"class":"num-applicants__caption topcard__flavor--metadata topcard__flavor--bullet"}).text.strip()
        nb_candidats = int(nb_candidats.split()[0])
        job["nb_candidats"]= nb_candidats
    except:
        job["nb_candidats"]=None

    list_jobs.append(job)
    job={}
