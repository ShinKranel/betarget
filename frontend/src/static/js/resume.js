export default class Resume {
    constructor(data) {
      this.id = data.id;
      this.resumeStatus = data.resume_status;
      this.firstName = data.first_name;
      this.lastName = data.last_name;
      this.jobTitle = data.job_title;
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
      this.userId = data.user_id;
      this.vacancyId = data.vacancy_id;
    }
  }