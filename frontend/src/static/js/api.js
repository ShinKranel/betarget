"use strict";

async function fetchVacancies() {
  try {
    const url = new URL("/vacancy", window.location.origin);
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    return data;
  } catch (error) {
    throw new Error("Ошибка при получении данных о вакансиях");
  }
}

async function fetchResumes(vacancyId = 0, resumeStatus = "") {
  try {
    const url = new URL("/resume", window.location.origin);
    if (vacancyId) {
      url.searchParams.set("vacancy_id", vacancyId);
    }
    if (resumeStatus) {
      url.searchParams.set("resume_status", resumeStatus);
    }
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    return data;
  } catch (error) {
    throw new Error("Ошибка при получении данных о резюме");
  }
}

export { fetchVacancies, fetchResumes };
