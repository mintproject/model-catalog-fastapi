from pydantic import BaseModel

class ResultItem(BaseModel):
  Name: str

class Result(BaseModel):
  Result: list[ResultItem]

class ResultSet(BaseModel):
  ResultSet: Result

