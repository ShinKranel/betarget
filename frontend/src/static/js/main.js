"use strict";

import { Vacancy } from "./vacancy.js";
import { fetchVacancies } from "./api.js";
import { renderVacancies } from "./render.js";

async function main() {
  try {
    const vacanciesData = await fetchVacancies();
    const vacancies = vacanciesData.map((data) => new Vacancy(data));
    renderVacancies(vacancies);
  } catch (error) {
    console.error(error);
  }
}

main();
