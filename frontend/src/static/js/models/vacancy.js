"use strict";

export default class Vacancy {
  constructor(data) {
    this.id = data.id;
    this.jobTitle = data.job_title;
    this.city = data.city;
    this.company = data.company;
    this.experience = data.experience;
    this.workFormat = data.work_format;
    this.salary = data.salary;
    this.education = data.education;
    this.employmentType = data.employment_type;
    this.skills = data.skills;
    this.description = data.description;
    this.userId = data.user_id;
  }
}
