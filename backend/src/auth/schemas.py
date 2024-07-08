from pydantic import EmailStr, AnyUrl , UUID4,  Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber


from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: UUID4
    username: str = Field(..., min_length=1, max_length=30)
    email: EmailStr

    is_active: bool
    is_superuser: bool
    is_verified: bool

    # contacts
    telegram: str | None = Field(None, max_length=60)
    whatsapp: str | None = Field(None, max_length=60)
    linkedin: str | None = Field(None, max_length=150)
    github: str | None = Field(None, max_length=150)
    email: EmailStr | None
    phone_number: PhoneNumber | None

    profile_picture: str | None


class UserCreate(schemas.BaseUserCreate):
    username: str = Field(..., min_length=1, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=8)

    # contacts
    telegram: AnyUrl | None
    whatsapp: AnyUrl | None
    linkedin: AnyUrl | None
    github: AnyUrl | None
    email: EmailStr | None
    phone_number: PhoneNumber | None

    profile_picture: AnyUrl | None

    @field_validator("password")
    def check_password(cls, value):
        value = str(value)
        if len(value) < 8:
            raise ValueError("Password must have at least 8 characters")
        if not any(c.isupper() for c in value):
            raise ValueError("Password must have at least one uppercase letter")
        if not any(c.islower() for c in value):
            raise ValueError("Password must have at least one lowercase letter")
        if not any(c.isdigit() for c in value):
            raise ValueError("Password must have at least one digit")
        return value 


class UserUpdate(UserRead):
    pass