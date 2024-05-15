from linkedin_api import Linkedin
import os

TEST_LINKEDIN_USERNAME = ("wafermonster@yahoo.com")
TEST_LINKEDIN_PASSWORD = ("*4-SU$=@Cic&dZv")

print(TEST_LINKEDIN_PASSWORD)
# Authenticate using any Linkedin account credentials
api = Linkedin(TEST_LINKEDIN_USERNAME, TEST_LINKEDIN_PASSWORD)

# GET a profile
# profile = api.get_profile('wescules')

jobs = api.search_jobs(companies=["Meta"], limit=1)
# jobs[0]["trackingUrn"] = "3921195190"
job = api.get_job(job_id="3921195190")

# recipient = api.get_profile('abigail-zhang-8260a8232')
# message = api.send_message(message_body="sent from code", conversation_urn_id="2-NjcyOWU2MWYtZmNhNi00YTU4LTkyOTAtM2U3NDMzZDAzM2JmXzAxMA==")


