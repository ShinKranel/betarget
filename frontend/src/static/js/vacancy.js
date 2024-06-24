"use strict";

class Vacancy {
  constructor(data) {
    this.city = data.city;
    this.id = data.id;
    this.experience = data.experience;
    this.work_format = data.work_format;
    this.education = data.education;
    this.skills = data.skills;
    this.user_id = data.user_id;
    this.job_title = data.job_title;
    this.company = data.company;
    this.salary = data.salary;
    this.employment_type = data.employment_type;
    this.description = data.description;
  }
}

export { Vacancy };