# Standard Library imports

# Core Flask imports

# Third-party imports
from pydantic import BaseModel, EmailStr, constr, field_validator

# App imports


class AccountValidator(BaseModel):
    username: constr(min_length=1, max_length=15) = ...  # type: ignore
    email: EmailStr = ...
    password: str = ...

    @field_validator("username")
    def username_valid(cls, v):  # noqa: N805
        if not v[0].isalpha():
            raise ValueError("Username must start with a letter")
        if not v.isalnum():
            raise ValueError(
                "Username must contain only letters, numbers, and underscores"
            )
        return v


class EmailValidator(BaseModel):
    email: EmailStr
