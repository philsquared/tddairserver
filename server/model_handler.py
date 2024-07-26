from http import HTTPStatus

from server.response_data import ResponseData
from server.settings import Settings


class ModelHandler:

    def __init__(self, settings: Settings, model):
        self.settings = settings
        self.model = model

    def get_member(self, username: str) -> ResponseData:
        with self.model.start_transaction() as tx:
            if data := tx.get_member(username):
                return ResponseData(
                    description="Found member",
                    payload=data)
            else:
                return ResponseData(
                    code=HTTPStatus.NOT_FOUND,
                    status="Member not found"
                )

    def create_member(self, username: str, name: str, password: str, email: str, data: str) -> ResponseData:
        with self.model.start_transaction() as tx:
            tx.create_member(
                username=username,
                name=name,
                password=password,
                email=email,
                data=data)
            tx.commit()
        return ResponseData(description="Created member")
