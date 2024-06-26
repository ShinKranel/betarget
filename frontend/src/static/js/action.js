"use strict";

let currentActiveVacancy = null;
import Vacancy from "./vacancy.js";
import Resume from "./resume.js";
import { fetchVacancies, fetchResumes } from "./api.js";
import { renderVacancies, renderResumeList } from "./render.js";

function addClickEventListeners() {
  document.querySelectorAll(".vacancies__vacancy").forEach((element) => {
    element.addEventListener("click", setActiveVacancy);
  });
}

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

export { addClickEventListeners };
