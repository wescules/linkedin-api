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

        
        
__all__ = [JobId]