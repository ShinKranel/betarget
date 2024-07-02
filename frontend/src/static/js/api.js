"use strict";

async function fetchVacancies() {
  try {
    const url = new URL("/api/v1/vacancy", window.location.origin);
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

async function fetchResumeList(
  vacancyId = undefined,
  resumeStatus = undefined
) {
  try {
    const url = new URL("/api/v1/resume", window.location.origin);
    if (vacancyId !== undefined) {
      url.searchParams.set("vacancy_id", vacancyId);
    }
    if (resumeStatus !== undefined) {
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
    throw new Error("Ошибка при получении данных о списке резюме");
  }
}

async function fetchResume(resumeId) {
  try {
    const url = new URL(`/api/v1/resume/${resumeId}`, window.location.origin);
    // url.searchParams.set("resume_id", resumeId);

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

export { fetchVacancies, fetchResumeList, fetchResume };
