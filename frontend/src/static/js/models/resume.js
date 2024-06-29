export default class Resume {
  constructor(data) {
    this.id = data.id;
    this.resumeStage = data.resume_status;
    this.rating = data.rating;

    // content
    this.firstName = data.first_name;
    this.jobTitle = data.job_title;
    this.lastName = data.last_name;
    this.age = data.age;
    this.gender = data.gender;
    this.city = data.city;
    this.expectedSalary = data.expected_salary;
    this.interestInJob = data.interest_in_job;
    this.skills = data.skills;
    this.about = data.about;
    this.experience = data.experience;
    this.education = data.education;
    this.readyToRelocate = data.ready_to_relocate;
    this.readyForBusinessTrips = data.ready_for_business_trips;

    // contacts
    this.telegram = data.telegram;
    this.whatsapp = data.whatsapp;
    this.linkedin = data.linkedin;
    this.github = data.github;
    this.email = data.email;
    this.phoneNumber = data.phone_number;

    // foreign keys
    this.userId = data.user_id;
    this.vacancyId = data.vacancy_id;
  }
}
