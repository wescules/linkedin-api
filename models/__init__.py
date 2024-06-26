from typing import Optional
from beanie import Document
import pydantic
from pydantic import BaseModel


class JobIdList(BaseModel):
    jobId: str = None
    
    class Settings:
        name = "jobId"
        projection = {"jobId": 1}

class JobId(Document):
    jobId: str = None  #last number from'trackingUrn': 'urn:li:jobPosting:3921698294'
    title: str = None
    posterId: Optional[str] = None
    entityUrn: Optional[str] = None #similar to job id
        
    model_config = pydantic.ConfigDict(populate_by_name=True)
    
    class Settings:
        name = "jobId"

class Company(Document):
    companyId: Optional[str] = None  #urn id from linkedin
    company_name: Optional[str] = None # meta
    company_legal_name: Optional[str] = None # meta platforms inc
    company_descriptor: Optional[str] = None # scraped information about this company
        
    model_config = pydantic.ConfigDict(populate_by_name=True)
    
    class Settings:
        name = "company"
        
class JobPostingIds(BaseModel):
    jobId: str = None
    
    class Settings:
        name = "jobPostings"
        projection = {"jobId": 1}

class JobPosting(Document):
    jobId: str = None  #last number from'trackingUrn': 'urn:li:jobPosting:3921698294'
    salary: Optional[str] = None
    description: Optional[str] = None
    company: Optional[str] = None 
    job_title: Optional[str] = None 
    level: Optional[str] = None 
    location: Optional[str] = None 
    job_type: Optional[str] = None 
    nb_candidates: Optional[str] = None 
    workplace_type: Optional[str] = None
    listedAt: int
    remote_work_allowed: Optional[bool] = False
    company_apply_url: Optional[str] = None
    
    
    class Settings:
        name = "jobPostings"
    
class CompanyName(Document):
    company: Optional[str] = None     
            
    class Settings:
        name = "jobPostings"

        
        
__all__ = [JobId, JobPosting, Company]