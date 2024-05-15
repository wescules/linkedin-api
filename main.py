from linkedin_api import Linkedin

TEST_LINKEDIN_USERNAME = ("wafermonster@yahoo.com")
TEST_LINKEDIN_PASSWORD = ("*4-SU$=@Cic&dZv")

# Authenticate using any Linkedin account credentials
api = Linkedin(TEST_LINKEDIN_USERNAME, TEST_LINKEDIN_PASSWORD)

# GET a profile
# profile = api.get_profile('wescules')

# jobs = api.search_jobs(companies=["Meta"], limit=1)

jobs = [
    {"trackingUrn": "1234", "title": "Swe1", "posterId": '1233', "jobId": '1234124124'},
    {"trackingUrn": "12341", "title": "Swe12", "posterId": '121333', "jobId": '1234124123123124'},
    {"trackingUrn": "12342", "title": "Swe123", "posterId": '1232223', "jobId": '1234123123124124'}
]
    
for job in jobs:
    
    
    
    
# jobs[0]["trackingUrn"] = "3921195190"
# job = api.get_job(job_id="3921195190")

# recipient = api.get_profile('abigail-zhang-8260a8232')
# message = api.send_message(message_body="sent from code", conversation_urn_id="2-NjcyOWU2MWYtZmNhNi00YTU4LTkyOTAtM2U3NDMzZDAzM2JmXzAxMA==")
