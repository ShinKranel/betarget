from sqladmin import ModelView

from user.models import User


class UserAdmin(ModelView, model=User):
    name='User'
    name_plural='Users'
    column_list = [
        "id",
        "username",
        "email",
        "hashed_password",
        "registered_at",
        "telegram",
        "whatsapp",
        "linkedin",
        "phone_number",
        "profile_picture",
        "is_active",
        "is_superuser",
        "is_verified",
    ]

    form_create_rules = [
        "username", 
        "email", 
        "password", 
        "telegram", 
        "whatsapp", 
        "linkedin", 
        "phone_number", 
        "profile_picture", 
        "is_active", 
        "is_superuser", 
        "is_verified"
    ]

    form_widget_args = {
        'hashed_password': {
            'type': 'password'
        }
    }

    column_labels = {
        "id": "ID",
        "username": "Username",
        "email": "Email",
        "hashed_password": "Password",
        "registered_at": "Registered At",
        "telegram": "Telegram",
        "whatsapp": "Whatsapp",
        "linkedin": "LinkedIn",
        "phone_number": "Phone Number",
        "profile_picture": "Profile Picture",
        "is_active": "Active",
        "is_superuser": "Superuser",
        "is_verified": "Verified",
    }

    form_choices = {
        'is_active': [
            (True, 'Active'),
            (False, 'Inactive')
        ],
        'is_superuser': [
            (True, 'Yes'),
            (False, 'No')
        ],
        'is_verified': [
            (True, 'Yes'),
            (False, 'No')
        ]
    }
