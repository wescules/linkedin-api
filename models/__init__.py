from beanie import Document


class JobId(Document):
    jobId: str  #last number from'trackingUrn': 'urn:li:jobPosting:3921698294'
    title:str
    posterId: str
    trackingUrn: str #similar to job id

__all__ = [JobId]