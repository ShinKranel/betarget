"use strict";

import Vacancy from "./models/vacancy.js";
import Resume from "./models/resume.js";
import { fetchVacancies, fetchResumes } from "./api.js";
import { renderVacancies, renderResumeList } from "./render.js";
import { addClickEventListeners } from "./actions/eventListeners.js";

async function main() {
  try {
    const vacanciesData = await fetchVacancies();
    const vacancies = vacanciesData.map((data) => new Vacancy(data));
    renderVacancies(vacancies);

    const resumesData = await fetchResumes();
    const resumes = resumesData.map((data) => new Resume(data));
    renderResumeList(resumes);
    addClickEventListeners();
  } catch (error) {
    console.error(error);
  }
}

main();
