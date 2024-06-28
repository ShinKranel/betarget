"use strict";

import {
  addEventListenerToVacancy,
  addEventListenerToResumeList,
} from "./actions/eventListeners.js";

function toggleDisplayResume() {
  const resumeNotChosenElement = document.querySelector(".resume__not-chosen");
  const resumeDisplayElement = document.querySelector(".resume-display");
  const resumeInfoElement = document.querySelector(".resume-info");
  if (resumeNotChosenElement.style.display === "none") {
    // резюме отображается, убираем отображение
    resumeDisplayElement.style.display = "none";
    resumeInfoElement.style.display = "none";
    resumeNotChosenElement.style.display = "block";
  } else {
    // резюме не отображается, добавляем отображение
    resumeDisplayElement.style.display = "block";
    resumeInfoElement.style.display = "flex";
    resumeNotChosenElement.style.display = "none";
  }
}

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

    addEventListenerToVacancy(vacancyElement);
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
    addEventListenerToResumeList(resumeElement);
    resumeList.appendChild(resumeElement);
  });
}

function translateResumeStatus(resumeStatus) {
  switch (resumeStatus) {
    case "in_work":
      return "В работе";
    case "screening":
      return "Скрининг";
    case "interview":
      return "Интервью";
    case "review":
      return "На рассмотрении";
    case "accepted":
      return "Принято";
    case "rejected":
      return "Отказ";
    case "offer":
      return "Оффер";
    default:
      return resumeStatus;
  }
}

function renderResume(resume) {
  const resumeNotChosenElement = document.querySelector(".resume__not-chosen");
  if (resumeNotChosenElement.style.display !== "none") {
    toggleDisplayResume();
  }

  const resumeDisplaySection = document.querySelector(".resume-display");
  const resumeInfoSection = document.querySelector(".resume-info");

  // Resume actions
  const resumeActionsStatus = resumeDisplaySection.querySelector(
    ".resume-display__status p"
  );
  resumeActionsStatus.textContent = translateResumeStatus(resume.resumeStatus);

  // Resume content
  const skillsList = resumeDisplaySection.querySelector(
    ".resume-content__skills-list"
  );
  skillsList.innerHTML = "";
  // if (resume.skills) {
  //   resume.skills.forEach((skill) => {
  //     const skillListItem = document.createElement("li");
  //     skillListItem.textContent = skill;
  //     skillsList.appendChild(skillListItem);
  //   });
  // }

  const experienceParagraph = resumeDisplaySection.querySelector(
    ".resume-content__experience p"
  );
  experienceParagraph.textContent = resume.experience;

  const educationParagraph = resumeDisplaySection.querySelector(
    ".resume-content__education p"
  );
  educationParagraph.textContent = resume.education;

  const aboutParagraph = resumeDisplaySection.querySelector(
    ".resume-content__about p"
  );
  aboutParagraph.textContent = resume.about;

  // Resume info
  const resumeInfoName = resumeInfoSection.querySelector(".resume-info__name");
  resumeInfoName.textContent = `${resume.firstName} ${resume.lastName}`;

  const resumeInfoPosition = resumeInfoSection.querySelector(
    ".resume-info__position"
  );
  resumeInfoPosition.textContent = resume.jobTitle;

  const resumeInfoPhone = resumeInfoSection.querySelector(
    ".resume-info__phone"
  );
  resumeInfoPhone.textContent = resume.phoneNumber;

  const resumeInfoEmail = resumeInfoSection.querySelector(
    ".resume-info__email"
  );
  resumeInfoEmail.textContent = resume.email;

  const resumeInfoCity = resumeInfoSection.querySelector(".resume-info__city");
  resumeInfoCity.textContent = resume.city;

  const resumeInfoSalary = resumeInfoSection.querySelector(
    ".resume-info__salary"
  );
  resumeInfoSalary.textContent = resume.expectedSalary;

  const resumeInfoAge = resumeInfoSection.querySelector(".resume-info__age");
  resumeInfoAge.textContent = resume.age;
}

export { renderVacancies, renderResumeList, renderResume };
