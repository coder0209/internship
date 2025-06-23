class ErrorHandling():
    @staticmethod
    def success(message="Successful",status_code=200,data=None):
        response={
            "status":"success",
            "message": message,
        }
        if data is not None:
            response['data']=data
        return response,status_code

    @staticmethod
    def failure(message="Error!",status_code=500,data=None):
        response={
            "Status":"failure",
            "message": message
        }
        if data:
            response['data']=data
        return response,status_code

