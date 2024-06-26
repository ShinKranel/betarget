"use strict";

function renderVacancies(vacancies) {
  const vacanciesList = document.querySelector(".vacancies__list");
  vacanciesList.innerHTML = "";
  vacancies.forEach((vacancy) => {
    const vacancyElement = document.createElement("a");
    vacancyElement.href = "";
    vacancyElement.classList.add("vacancies__vacancy");
    vacancyElement.dataset.id = vacancy.id;
    const titleElement = document.createElement("div");
    titleElement.classList.add("vacancies__title");
    titleElement.textContent = vacancy.jobTitle;
    const subtitleElement = document.createElement("div");
    subtitleElement.classList.add("vacancies__subtitle");
    subtitleElement.textContent = vacancy.company;
    vacancyElement.appendChild(titleElement);
    vacancyElement.appendChild(subtitleElement);
    vacanciesList.appendChild(vacancyElement);
  });
}

function renderResumeList(resumes) {
  const resumeList = document.querySelector(".resume-list");
  resumeList.innerHTML = "";
  resumes.forEach((resume) => {
    const resumeElement = document.createElement("a");
    resumeElement.href = "";
    resumeElement.classList.add("resume-list__resume");
    resumeElement.dataset.id = resume.id;

    const resumeInfoElement = document.createElement("div");
    resumeInfoElement.classList.add("resume-list__info");

    const resumeNameElement = document.createElement("div");
    resumeNameElement.classList.add("resume-list__name");
    resumeNameElement.textContent = resume.firstName + " " + resume.lastName;

    const resumeJobTitleElement = document.createElement("div");
    resumeJobTitleElement.classList.add("resume-list__job-title");
    resumeJobTitleElement.textContent = resume.jobTitle;

    const resumeScoreElement = document.createElement("div");
    resumeScoreElement.classList.add("resume-list__score");

    const resumeScoreNumberElement = document.createElement("span");
    resumeScoreNumberElement.classList.add("resume-list__score-number");
    resumeScoreNumberElement.textContent = resume.rating;

    const resumeScoreTextElement = document.createTextNode(" / 10");

    resumeScoreElement.appendChild(resumeScoreNumberElement);
    resumeScoreElement.appendChild(resumeScoreTextElement);

    resumeInfoElement.appendChild(resumeNameElement);
    resumeInfoElement.appendChild(resumeJobTitleElement);
    resumeInfoElement.appendChild(resumeScoreElement);
    // resumeElement.innerHTML =
    //   '<div class="resume-list__photo-container"><img  class="resume-list__photo" /></div>';
    const photoContainer = document.createElement("div");
    photoContainer.className = "resume-list__photo-container";
    const photo = document.createElement("img");
    photo.className = "resume-list__photo";
    photoContainer.appendChild(photo);

    resumeElement.appendChild(photoContainer);
    resumeElement.appendChild(resumeInfoElement);

    resumeList.appendChild(resumeElement);
  });
}

export { renderVacancies, renderResumeList };
