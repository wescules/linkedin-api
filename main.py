import json
from config.config import Settings, initiate_database
from linkedin_api import Linkedin
from database.database import DB
import asyncio

from models import Company
from scraper.h1bDatabaseScraper import H1BScraper
from scraper.linkedinScraper import scrape_job

# Authenticate using any Linkedin account credentials
api = Linkedin(Settings().LINKEDIN_USERNAME, Settings().LINKEDIN_PASSWORD)

# GET a profile
# profile = api.get_profile('wescules')

# companies=["10667"]   This is company urn of Meta



async def get_all_job_listings():
    keywords = [
        "Software Engineer",
        "Frontend Engineer",
        "Backend Engineer",
        "Data Engineer",
        "Data Scientist",
        "Database",
        "Devops",
        "Developer",
        "QA",
        "Designer",
        "Product Manager",
        "Manager",
        "Marketing",
        "Sales",
        "Support"
        ]
    for keyword in keywords:
        print(f"Searching for {keyword}")
        jobs = api.search_jobs(keywords=keyword, job_type=["F", "C"])
        await DB.insert_jobs(jobs)

async def populate_job_postings():
    job_ids = await DB().get_unused_job_ids()
    
    for job_id in job_ids:
        job = api.get_job(job_id=job_id)
        if not job or job is None:
            continue
            
        if 'com.linkedin.voyager.jobs.OffsiteApply' in job['applyMethod'] or ("com.linkedin.voyager.jobs.ComplexOnsiteApply" in job['applyMethod'] and 'companyApplyUrl' in job['applyMethod']['com.linkedin.voyager.jobs.ComplexOnsiteApply']):
            job = await scrape_job(job, job_id)
            await DB.add_job_posting(job)
        else:
            print(f"this does not have offsite apply {json.dumps(job['applyMethod'])}")
            await DB.delete_jobId(job_id)
            continue

async def get_company_info():
    companies = await DB.retrieve_company_names()
    for company_name in companies:
        if company_name:
            company_name = company_name.strip()
            try:
                company = api.search_companies(keywords=company_name, limit=1)
                if len(company) > 0:
                    company = company[0]
                    company_descriptor, company_legal_name = await H1BScraper().scrape_job(company_name)
                    company = Company(companyId=company['urn_id'], company_name=company_name, company_legal_name=company_legal_name, company_descriptor=company_descriptor)
                    await DB.add_company(company)
            except:
                continue
async def main():
    await initiate_database()
    
    # await get_all_job_listings()
    
    # await populate_job_postings()

    await get_company_info()
    
    
asyncio.run(main())




    
    
    
# jobs[0]["trackingUrn"] = "3921195190"
# job = api.get_job(job_id="3921195190")

# recipient = api.get_profile('abigail-zhang-8260a8232')
# message = api.send_message(message_body="sent from code", conversation_urn_id="2-NjcyOWU2MWYtZmNhNi00YTU4LTkyOTAtM2U3NDMzZDAzM2JmXzAxMA==")








# db.getCollection("jobId").aggregate([
#     {
#         $group: {
#             _id: "$jobId",
#             count: { $sum: 1 },
#             duplicates: { $addToSet: "$_id" } // Store IDs of duplicate documents
#         }
#     },
#     {
#         $match: {
#             count: { $gt: 1 } // Match only those documents with more than one occurrence
#         }
#     }
# ]).forEach(function(doc) {
#     doc.duplicates.shift(); // Remove the first ID, keep one document for each jobId
#     db.getCollection("jobId").remove({ _id: { $in: doc.duplicates } }); // Remove duplicate documents
# });
