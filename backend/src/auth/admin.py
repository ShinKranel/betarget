from sqladmin import ModelView

from backend.src.auth.models import User

class UserAdmin(ModelView, model=User):
    name='User'
    name_plural='Users'
    column_list = [
        "id",
        "username",
        "email",
        "hashed_password",
        "registered_at",
        "is_active",
        "is_superuser",
        "is_verified",
    ]

    form_create_rules = ["username", "email", "password", "is_active", "is_superuser", "is_verified"]

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
