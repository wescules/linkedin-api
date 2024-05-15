from config.config import Settings, initiate_database
from linkedin_api import Linkedin
from linkedin_api.utils.helpers import get_id_from_urn
from models import JobId
from database.database import DB
import asyncio

# Authenticate using any Linkedin account credentials
api = Linkedin(Settings().LINKEDIN_USERNAME, Settings().LINKEDIN_PASSWORD)

# GET a profile
# profile = api.get_profile('wescules')

# companies=["10667"]   This is company urn of Meta

async def insert_jobs(jobs):
    for job in jobs:
        jobId = get_id_from_urn(job['trackingUrn'])
        job_obj = JobId(jobId=jobId, title=job['title'], posterId=job['posterId'], entityUrn=job['entityUrn'])
        await DB.add_job_id(job_obj)
    
async def main():
    await initiate_database()
    # keywords = [
    #     # "Software Engineer"
    #     # "Frontend Engineer",
    #     # "Backend Engineer",
    #     # "Data Engineer",
    #     "Data Scientist",
    #     "Database",
    #     "Devops",
    #     "Developer",
    #     "QA",
    #     "Designer",
    #     "Product Manager",
    #     "Manager",
    #     "Marketing",
    #     "Sales",
    #     "Support"
    #     ]
    # for keyword in keywords:
    #     print(f"Searching for {keyword}")
    #     jobs = api.search_jobs(keywords=keyword, job_type=["F", "C"])
    #     await insert_jobs(jobs)
    
    # api.get_job(job_id="3841566189")
    jobs =  await DB.retrieve_jobIds()
    print(jobs)
    
    
asyncio.run(main())




    
    
    
# jobs[0]["trackingUrn"] = "3921195190"
# job = api.get_job(job_id="3921195190")

# recipient = api.get_profile('abigail-zhang-8260a8232')
# message = api.send_message(message_body="sent from code", conversation_urn_id="2-NjcyOWU2MWYtZmNhNi00YTU4LTkyOTAtM2U3NDMzZDAzM2JmXzAxMA==")
