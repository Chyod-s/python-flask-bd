class SuccessAPIResponse:
    def __init__(self, message: str, data: dict = {}, status_code: int = 200):
        self.message = message
        self.data = data or {}
        self.status_code = status_code

    def to_dict(self):
        return {
            "status": "success",
            "message": self.message,
            "data": self.data
        }