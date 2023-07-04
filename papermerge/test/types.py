from fastapi.testclient import TestClient
from pydantic import BaseModel

from papermerge.core.models import User


class AuthTestClient(BaseModel):
    user: User
    test_client: TestClient

    class Config:
        arbitrary_types_allowed = True

    def post(self, *args, **kwargs):
        return self.test_client.post(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.test_client.get(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.test_client.request(
            "DELETE",
            *args,
            **kwargs
        )

    def patch(self, *args, **kwargs):
        return self.test_client.patch(*args, **kwargs)