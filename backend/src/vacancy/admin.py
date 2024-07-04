from sqladmin import ModelView

from backend.src.vacancy.models import Vacancy


class VacancyAdmin(ModelView, model=Vacancy):
    name = "Vacancy"
    name_plural = "Vacancies"
    column_list = [
        "id",
        "job_title",
        "city",
        "company",
        "experience",
        "work_format",
        "salary",
        "education",
        "employment_type",
        "skills",
        "description",
        "user_id"
    ]

    column_labels = {
        "id": "ID",
        "job_title": "Job Title",
        "city": "City",
        "company": "Company",
        "experience": "Experience",
        "work_format": "Work Format",
        "salary": "Salary",
        "education": "Education",
        "employment_type": "Employment Type",
        "skills": "Skills",
        "description": "Description",
        "user_id": "User ID",
    }

    form_choices = {
        'experience': [
            ('no_experience', 'No Experience'),
            ('up_to_1_year', 'Up to 1 year'),
            ('between_1_and_3', '1-3 years'),
            ('between_3_and_6', '3-6 years'),
            ('more_than_6', 'More than 6 years')
        ],
        'work_format': [
            ('office', 'In Office'),
            ('home', 'From Home'),
            ('hybrid', 'Hybrid'),
            ('discuss', 'Discuss')
        ],
        'employment_type': [
            ('full_time', 'Full Time'),
            ('part_time', 'Part Time'),
            ('internship', 'Internship'),
            ('volunteer', 'Volunteer')
        ],
        'education': [
            ('incomplete_secondary', 'Incomplete Secondary'),
            ('secondary', 'Secondary'),
            ('secondary_vocational', 'Secondary Vocational'),
            ('incomplete_higher', 'Incomplete Higher'),
            ('bachelor', 'Bachelor'),
            ('master', 'Master'),
            ('phd', 'PhD')
        ],
    }
