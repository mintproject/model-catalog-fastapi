from pydantic import BaseModel

class CKANItem(BaseModel):
  Name: str

class CKANResponse(BaseModel):
  ResultSet: list[CKANItem]
