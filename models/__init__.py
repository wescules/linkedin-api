from beanie import Document


class JobId(Document):
    jobId: str = None  #last number from'trackingUrn': 'urn:li:jobPosting:3921698294'
    title:str = None
    posterId: str = None
    entityUrn: str = None #similar to job id

    # def __init__(self, jobId, title, posterId, entityUrn):
    #     self.jobId = jobId
    #     self.title = title
    #     self.posterId = posterId
    #     self.entityUrn = entityUrn
        
    class Settings:
        name = "jobId"
        
        

__all__ = [JobId]