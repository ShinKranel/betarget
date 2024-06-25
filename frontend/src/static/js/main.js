"use strict";

import Vacancy from "./vacancy.js";
import Resume from "./resume.js";
import { fetchVacancies, fetchResumes } from "./api.js";
import { renderVacancies, renderResumeList } from "./render.js";

async function main() {
  try {
    const vacanciesData = await fetchVacancies();
    const vacancies = vacanciesData.map((data) => new Vacancy(data));
    renderVacancies(vacancies);

    const resumesData = await fetchResumes();
    const resumes = resumesData.map((data) => new Resume(data));
    renderResumeList(resumes);
  } catch (error) {
    console.error(error);
  }
}

main();
