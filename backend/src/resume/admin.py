from sqladmin import ModelView

from resume.models import Resume, Gender, InterestInJob, ResumeStage


class ResumeAdmin(ModelView, model=Resume):
    name = "Resume"
    name_plural = "Resumes"
    column_list = [
        "id",
        "resume_stage",
        "rating",
        "first_name",
        "last_name",
        "job_title",
        "age",
        "gender",
        "city",
        "expected_salary",
        "interest_in_job",
        "skills",
        "about",
        "experience",
        "education",
        "ready_to_relocate",
        "ready_for_business_trips",
        "telegram",
        "whatsapp",
        "linkedin",
        "github",
        "email",
        "phone_number",
        "user_id",
        "vacancy_id"
    ]

    column_labels = {
        "id": "ID",
        "resume_stage": "Resume Stage",
        "rating": "Rating",
        "first_name": "First Name",
        "last_name": "Last Name",
        "job_title": "Job Title",
        "age": "Age",
        "gender": "Gender",
        "city": "City",
        "expected_salary": "Expected Salary",
        "interest_in_job": "Interest in Job",
        "skills": "Skills",
        "about": "About",
        "experience": "Experience",
        "education": "Education",
        "ready_to_relocate": "Ready to Relocate",
        "ready_for_business_trips": "Ready for Business Trips",
        "telegram": "Telegram",
        "whatsapp": "WhatsApp",
        "linkedin": "LinkedIn",
        "github": "GitHub",
        "email": "Email",
        "phone_number": "Phone Number",
        "user_id": "User ID",
        "vacancy_id": "Vacancy ID",
    }

    form_choices = {
        'resume_stage': [
            (ResumeStage.in_work.value, 'In Work'),
            (ResumeStage.screening.value, 'Screening'),
            (ResumeStage.interview.value, 'Interview'),
            (ResumeStage.rejected.value, 'Rejected'),
            (ResumeStage.offer.value, 'Offer')
        ],
        'gender': [
            (Gender.male.value, 'Male'),
            (Gender.female.value, 'Female'),
            (Gender.other.value, 'Other')
        ],
        'interest_in_job': [
            (InterestInJob.looking_for_job.value, 'Looking for Job'),
            (InterestInJob.not_looking_for_a_job.value, 'Not Looking for a Job'),
            (InterestInJob.considers_proposals.value, 'Considers Proposals'),
            (InterestInJob.offered_a_job_decides.value, 'Offered a Job, Decides')
        ]
    }
