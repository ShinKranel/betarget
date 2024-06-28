"use strict";

import Resume from "../models/resume.js";
import Vacancy from "../models/vacancy.js";
import { fetchVacancies, fetchResumeList } from "../api.js";
import { renderVacancies, renderResumeList } from "../render.js";
import { displayResumeList } from "./resumeListActions.js";

let currentActiveVacancy = null;

async function setActiveVacancy(event) {
  event.preventDefault();
  const targetElement = event.currentTarget;
  if (currentActiveVacancy) {
    currentActiveVacancy.classList.remove("vacancies__vacancy_active");
  }
  targetElement.classList.add("vacancies__vacancy_active");
  currentActiveVacancy = targetElement;
  displayResumeList(currentActiveVacancy.dataset.id);
}

export { setActiveVacancy };
