"use strict";

import { Vacancy } from "./types.d.ts";
async function fetchVacancies() {
  try {
    const response = await fetch("/vacancy", {
      method: "GET",
      headers: {
        // 'accept': 'application/json',
        // accept: "module",
        // "Content-Type": "text/javascript",
        "Content-Type": "text/javascript",
      },
    });
    const data = await response.json();
    return data;
  } catch (error) {
    throw new Error("Ошибка при получении данных о вакансиях");
  }
}
function renderVacancies(vacancies) {
  const vacanciesList = document.querySelector(".vacancies__list");
  vacancies.forEach((vacancy) => {
    const vacancyElement = document.createElement("a");
    vacancyElement.href = "";
    vacancyElement.classList.add("vacancies__vacancy");
    const titleElement = document.createElement("div");
    titleElement.classList.add("vacancies__title");
    titleElement.textContent = vacancy.job_title;
    const subtitleElement = document.createElement("div");
    subtitleElement.classList.add("vacancies__subtitle");
    subtitleElement.textContent = vacancy.company;
    vacancyElement.appendChild(titleElement);
    vacancyElement.appendChild(subtitleElement);
    vacanciesList.appendChild(vacancyElement);
  });
}
async function main() {
  try {
    const vacancies = await fetchVacancies();
    renderVacancies(vacancies);
    console.log(2);
  } catch (error) {
    console.error(error);
  }
}
main();
console.log(111);
//# sourceMappingURL=render.js.map
