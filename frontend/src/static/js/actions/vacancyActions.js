"use strict";

import Resume from "../models/resume.js";
import Vacancy from "../models/vacancy.js";
import { fetchVacancies, fetchResumes } from "../api.js";
import { renderVacancies, renderResumeList } from "../render.js";

let currentActiveVacancy = null;

async function setActiveVacancy(event) {
  event.preventDefault();
  const targetElement = event.currentTarget;
  if (currentActiveVacancy) {
    currentActiveVacancy.classList.remove("vacancies__vacancy_active");
  }
  targetElement.classList.add("vacancies__vacancy_active");
  currentActiveVacancy = targetElement;
  displayActiveVacancyResumes();
}

async function displayActiveVacancyResumes() {
  const activeVacancyId = currentActiveVacancy.dataset.id;
  const resumesData = await fetchResumes(activeVacancyId);
  const resumes = resumesData.map((data) => new Resume(data));
  renderResumeList(resumes);
}

export { setActiveVacancy, displayActiveVacancyResumes };
