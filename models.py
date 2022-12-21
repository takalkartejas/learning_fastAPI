from typing import Optional, List
from uuid import UUID, uuid4
#pydantic performs data validation
from pydantic import BaseModel
from enum import Enum



#define the enum gender
class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

#define the enum role
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

# We declare the shape of our data as classes with attributes
class User(BaseModel):
    #define the attributes inside class
    #id is an optional entry
    #uuid is a data type, we can also use int
    '''
    The data type uuid stores Universally Unique Identifiers (UUID) as 
    defined by RFC 4122, ISO/IEC 9834-8:2005, and related standards.
    A universally unique identifier (UUID) is a 128-bit number used to 
    identify information in computer systems.
    '''
    #if UUID is not provided use uuid4
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    #middle name is also an optional entry
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]