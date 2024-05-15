from typing import List
from models import JobId, JobIdList, JobPosting, JobPostingIds
from linkedin_api.utils.helpers import get_id_from_urn

jobIds_collection = JobId
jobPosting_collection = JobPosting

class DB:
    
    async def add_job_id(jobId: JobId) -> JobId:
        return await jobId.create()
        # existing_job_id = await jobIds_collection.find_one({"jobId": jobId.jobId})
        # if existing_job_id is None:
        #     return await jobId.create()
        
    async def add_job_posting(job_posting: JobPosting) -> JobId:
        return await job_posting.create()

    # async def find_user(email: str):
    #     user = await user_collection.find_one({"email": email})
    #     return user


    async def retrieve_jobIds() -> List[JobIdList]:
        return await jobIds_collection.all().project(JobIdList).to_list()
    
    async def retrieve_jobPostingIds() -> List[JobPostingIds]:
        return await jobPosting_collection.all().project(JobPostingIds).to_list()

    async def insert_jobs(jobs):
        for job in jobs:
            jobId = get_id_from_urn(job['trackingUrn'])
            job_obj = JobId(jobId=jobId, title=job['title'], posterId=job['posterId'], entityUrn=job['entityUrn'])
            await DB.add_job_id(job_obj)


    # async def retrieve_student(id: PydanticObjectId) -> Student:
    #     student = await student_collection.get(id)
    #     if student:
    #         return student



    async def delete_jobId(job_id: str) -> bool:
        jobId = await jobIds_collection.find_one({"jobId": job_id})
        if jobId:
            await jobId.delete()
            return True


    # async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
    #     des_body = {k: v for k, v in data.items() if v is not None}
    #     update_query = {"$set": {field: value for field, value in des_body.items()}}
    #     student = await student_collection.get(id)
    #     if student:
    #         await student.update(update_query)
    #         return student
    #     return False