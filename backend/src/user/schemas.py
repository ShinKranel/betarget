from pydantic import EmailStr, AnyHttpUrl , UUID4,  Field, field_validator, BaseModel
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
    telegram: str | None
    whatsapp: str | None
    linkedin: str | None
    email: EmailStr | None
    phone_number: PhoneNumber | None
    profile_picture: str | None


class UserCreate(schemas.BaseUserCreate):
    username: str = Field(..., min_length=1, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=8)
    # contacts
    telegram: AnyHttpUrl | None = Field(None)
    whatsapp: AnyHttpUrl | None = Field(None)
    linkedin: AnyHttpUrl | None = Field(None)
    email: EmailStr | None
    phone_number: PhoneNumber | None
    profile_picture: AnyHttpUrl | None = Field(None)

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

    @field_validator("telegram", "whatsapp", "linkedin", "profile_picture")
    def validate_urls(cls, v):
        if v is None:
            return "https://example.com"
        return str(v)


class UserUpdate(BaseModel):
    username: str = Field(None, min_length=1, max_length=30)
    telegram: AnyHttpUrl | None = Field(None)
    whatsapp: AnyHttpUrl | None = Field(None)
    linkedin: AnyHttpUrl | None = Field(None)
    email: EmailStr | None = Field(None)
    phone_number: PhoneNumber | None
    profile_picture: AnyHttpUrl | None = Field(None)

    @field_validator("telegram", "whatsapp", "linkedin", "profile_picture")
    def validate_urls(cls, v):
        if v is None:
            return "https://example.com"
        return str(v)
