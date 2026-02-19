from pydantic import BaseModel

# Input Schema: What the user sends to register
class UserCreate(BaseModel):
    username: str
    password: str

# Output Schema: What we return (we don't want to return the password!)
class UserResponse(BaseModel):
    id: int
    username: str
    balance: int

    model_config = {
    "from_attributes": True
} #sql returns an object and pydantic wants dict

# Input Schema: When depositing/withdrawing, user sends this
class Transaction(BaseModel):
    amount: int