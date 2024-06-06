// import { Vacancy } from "./types";

interface Vacancy {
  city: string;
  id: number;
  experience: string;
  work_format: string;
  education: string;
  skills: string;
  user_id: number;
  job_title: string;
  company: string;
  salary: number;
  employment_type: string;
  description: string;
}

async function fetchVacancies(): Promise<Vacancy[]> {
  try {
    const response = await fetch("/vacancy", {
      method: "GET",
      headers: {
        accept: "application/json",
      },
    });
    const data: Vacancy[] = await response.json();
    return data;
  } catch (error) {
    throw new Error("Ошибка при получении данных о вакансиях");
  }
}

function renderVacancies(vacancies: Vacancy[]): void {
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
console.log(2);
