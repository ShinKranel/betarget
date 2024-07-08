from sqladmin import ModelView
from resume.models import Resume, Candidate, Gender, InterestInJob, ResumeStage

class ResumeAdmin(ModelView, model=Resume):
    name = "Resume"
    name_plural = "Resumes"
    column_list = [
        "id",
        "resume_stage",
        "rating",
        "job_title",
        "expected_salary",
        "interest_in_job",
        "skills",
        "experience",
        "education",
        "ready_to_relocate",
        "ready_for_business_trips",
        "vacancy_id",
    ]
    column_labels = {
        "id": "ID",
        "resume_stage": "Resume Stage",
        "rating": "Rating",
        "job_title": "Job Title",
        "expected_salary": "Expected Salary",
        "interest_in_job": "Interest in Job",
        "skills": "Skills",
        "experience": "Experience",
        "education": "Education",
        "ready_to_relocate": "Ready to Relocate",
        "ready_for_business_trips": "Ready for Business Trips",
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
        'interest_in_job': [
            (InterestInJob.looking_for_job.value, 'Looking for Job'),
            (InterestInJob.not_looking_for_a_job.value, 'Not Looking for a Job'),
            (InterestInJob.considers_proposals.value, 'Considers Proposals'),
            (InterestInJob.offered_a_job_decides.value, 'Offered a Job, Decides')
        ]
    }

class CandidateAdmin(ModelView, model=Candidate):
    name = "Candidate"
    name_plural = "Candidates"
    column_list = [
        "id",
        "first_name",
        "last_name",
        "age",
        "gender",
        "city",
        "about",
        "telegram",
        "whatsapp",
        "linkedin",
        "github",
        "email",
        "phone_number",
        "profile_picture",
        "resume_id",
    ]
    column_labels = {
        "id": "ID",
        "first_name": "First Name",
        "last_name": "Last Name",
        "age": "Age",
        "gender": "Gender",
        "city": "City",
        "about": "About",
        "telegram": "Telegram",
        "whatsapp": "WhatsApp",
        "linkedin": "LinkedIn",
        "github": "GitHub",
        "email": "Email",
        "phone_number": "Phone Number",
        "profile_picture": "Profile Picture",
        "resume_id": "Resume ID",
    }
    form_choices = {
        'gender': [
            (Gender.male.value, 'Male'),
            (Gender.female.value, 'Female'),
            (Gender.other.value, 'Other')
        ]
    }
