from models import JobId

jobIds_collection = JobId

class DB:
    
    async def add_job_id(jobId: JobId) -> JobId:
        existing_job_id = await jobIds_collection.find_one({"jobId": jobId.jobId})
        if existing_job_id:
            return
        return await jobId.create()
    

    # async def find_user(email: str):
    #     user = await user_collection.find_one({"email": email})
    #     return user


    # async def retrieve_students() -> List[Student]:
    #     students = await student_collection.all().to_list()
    #     return students




    # async def retrieve_student(id: PydanticObjectId) -> Student:
    #     student = await student_collection.get(id)
    #     if student:
    #         return student


    # async def delete_student(id: PydanticObjectId) -> bool:
    #     student = await student_collection.get(id)
    #     if student:
    #         await student.delete()
    #         return True


    # async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
    #     des_body = {k: v for k, v in data.items() if v is not None}
    #     update_query = {"$set": {field: value for field, value in des_body.items()}}
    #     student = await student_collection.get(id)
    #     if student:
    #         await student.update(update_query)
    #         return student
    #     return False