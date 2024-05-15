from time import sleep
import requests
import logging
from bs4 import BeautifulSoup
from datetime import datetime

from models import JobPosting

job_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
job={}
list_jobs=[]

async def getWorkplaceType(workplaceType):
    try:
        if 'urn:li:fs_workplaceType:2' in workplaceType:
            return "Remote"
        elif 'urn:li:fs_workplaceType:1' in workplaceType:
            return "In Person"
        else:
            return "Hybrid"
    except:
        return "In Person"


async def scrape_job(jobAPI, job_id) -> JobPosting:
    print(f"read jobId:{job_id}")

    resp = requests.get(job_url.format(job_id))
    if resp.status_code != 200:
        sleep(1)
        scrape_job(job, job_id) 
    soup = BeautifulSoup(resp.text,'html.parser')
    
    # write_html_to_file(soup)
                    
    try: 
        salary = soup.find("div",{"class":"salary compensation__salary"}).text.strip()
    except:
        salary = None
        
    try: 
        description = soup.find("div",{"class":"show-more-less-html__markup"}).decode_contents().strip()
    except:
        description = None
    
    try:
        company=soup.find("div",{"class":"top-card-layout__card"}).find("a").find("img").get('alt')
    except:
        company=None

    try:
        job_title = soup.find("div",{"class":"top-card-layout__entity-info"}).find("a").text.strip()
    except:
        job_title=None

    try:
        level=soup.find("ul",{"class":"description__job-criteria-list"}).find("li").text.replace("Seniority level","").strip()
    except:
        level=None

    try:
        location=soup.find("span",{"class":"topcard__flavor topcard__flavor--bullet"}).text.strip()
    except:
        location=None
        
    try:
        job_type=soup.find("span",{"class":"posted-time-ago__text"}).text.strip()
    except:
        job_type=None

    try:
        nb_candidates = soup.find("span",{"class":"num-applicants__caption"}).text.strip()
        nb_candidates= nb_candidates
    except:
        nb_candidates=None

    workplace_type = await getWorkplaceType(jobAPI)
    listedAt = jobAPI['listedAt']
    remote_work_allowed = jobAPI['workRemoteAllowed']
    company_apply_url = jobAPI['applyMethod']['com.linkedin.voyager.jobs.OffsiteApply']['companyApplyUrl']
    
    return JobPosting(jobId=job_id, salary=salary, description=description, 
                            company=company, job_title=job_title, level=level, location=location, 
                            job_type=job_type,nb_candidates=nb_candidates, 
                            workplace_type=workplace_type, listedAt=listedAt, company_apply_url=company_apply_url,
                            remote_work_allowed=remote_work_allowed
                            )

def write_html_to_file(soup):
    html = soup.prettify()  #bs is your BeautifulSoup object
    with open("html.html","w") as out:
        for i in range(0, len(html)):
            try:
                out.write(html[i])
            except Exception:
                1+1
    
