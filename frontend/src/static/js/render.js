"use strict";

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

export { renderVacancies };
