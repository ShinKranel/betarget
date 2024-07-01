"use strict";

import {
  addEventListenerToVacancy,
  addEventListenerToResumeList,
  addEventListenerToResumeChangeStageButton,
  addEventListenerToResumeStageInput,
  addEventListenerToResumeSaveStageButton,
  addEventListenerToResumeCancelStageButton,
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
    if (resume.rating >= 8) {
      resumeScoreNumberElement.classList.add("resume-list__score-number_good");
    }

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

function translateResumeStage(resumeStage) {
  switch (resumeStage) {
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
      return resumeStage;
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
  const resumeStage = resumeDisplaySection.querySelector(
    ".resume-display__current-stage"
  );
  resumeStage.textContent = translateResumeStage(resume.resumeStage);
  resumeStage.dataset.stage = resume.resumeStage;

  const resumeChangeStageButton = resumeDisplaySection.querySelector(
    ".resume-display__change-stage"
  );
  addEventListenerToResumeChangeStageButton(resumeChangeStageButton);

  const resumeStageInput = resumeDisplaySection.querySelector(
    ".resume-display__stage-input"
  );
  resumeStageInput.value = resume.resumeStage;
  addEventListenerToResumeStageInput(resumeStageInput);

  const resumeCancelStageButton = resumeDisplaySection.querySelector(
    ".resume-display__cancel-stage"
  );
  addEventListenerToResumeCancelStageButton(resumeCancelStageButton);

  const resumeSaveStageButton = resumeDisplaySection.querySelector(
    ".resume-display__save-stage"
  );
  addEventListenerToResumeSaveStageButton(resumeSaveStageButton);

  // Resume content
  const skillsList = resumeDisplaySection.querySelector(
    ".resume-content__skills-list"
  );
  skillsList.innerHTML = "";
  if (resume.skills) {
    resume.skills.forEach((skill) => {
      const skillListItem = document.createElement("li");
      skillListItem.textContent = skill;
      skillsList.appendChild(skillListItem);
    });
  }

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
  resumeInfoPhone.href = `tel:${resume.phoneNumber}`;

  const resumeInfoEmail = resumeInfoSection.querySelector(
    ".resume-info__email"
  );
  resumeInfoEmail.textContent = resume.email;
  resumeInfoEmail.href = `mailto:${resume.email}`;

  const resumeInfoCity = resumeInfoSection.querySelector(".resume-info__city");
  resumeInfoCity.textContent = resume.city;

  const resumeInfoSalary = resumeInfoSection.querySelector(
    ".resume-info__salary"
  );
  resumeInfoSalary.textContent = resume.expectedSalary;

  const resumeInfoAge = resumeInfoSection.querySelector(".resume-info__age");
  resumeInfoAge.textContent = resume.age;

  const contactsContainer = document.querySelector(".resume-info__contacts");
  contactsContainer.innerHTML = "";

  const contacts = [
    { title: "GitHub", link: resume.github, icon: "github" },
    { title: "LinkedIn", link: resume.linkedin, icon: "linkedin" },
    { title: "Telegram", link: resume.telegram, icon: "telegram" },
    { title: "WhatsApp", link: resume.whatsapp, icon: "whatsapp" },
  ];

  contacts.forEach((contact) => {
    if (contact.link) {
      const contactLink = document.createElement("a");
      contactLink.href = contact.link;
      contactLink.title = contact.title;
      contactLink.className = "resume-info__contacts-link";
      contactLink.target = "_blank";
      contactLink.rel = "noopener noreferrer";

      const contactIcon = getContactIcon(contact.icon);
      contactLink.innerHTML = contactIcon;

      contactsContainer.appendChild(contactLink);
    }
  });
}

function getContactIcon(iconType) {
  switch (iconType) {
    case "github":
      return '<svg viewBox="0 0 25 23" xmlns="http://www.w3.org/2000/svg"><path d="M16.2123 18.5004C16.2123 18.5964 16.3082 18.6826 16.4582 18.6826C16.6056 18.6826 16.7247 18.6107 16.7247 18.5004C16.7247 18.4161 16.6045 18.3349 16.4748 18.3349C16.3274 18.3235 16.2123 18.3946 16.2123 18.5004ZM17.6811 18.2842C17.7151 18.3802 17.6213 18.5004 17.4652 18.5125C17.345 18.5605 17.2023 18.5125 17.186 18.4286C17.152 18.3326 17.2339 18.2128 17.3851 18.1788C17.5053 18.1561 17.6481 18.1901 17.6813 18.2748L17.6811 18.2842ZM15.5985 18.2124C15.7292 18.2464 15.8314 18.3326 15.8144 18.4453C15.803 18.5295 15.6669 18.5927 15.5309 18.5654C15.4001 18.5314 15.3026 18.4453 15.3196 18.3496C15.3309 18.2536 15.4502 18.2022 15.5992 18.2188L15.5985 18.2124ZM12.4916 0.057943C19.0229 0.057943 24.0473 5.03563 24.0473 11.6176C24.0473 16.8578 20.7583 21.3362 16.0471 22.9404C15.4328 23.0364 15.2169 22.6774 15.2169 22.3645C15.2169 22.0811 15.2282 20.4471 15.2282 19.4523C15.2282 19.4523 18.5341 20.1638 19.2283 18.047C19.2283 18.047 19.7576 16.6587 20.5533 16.3116C20.5533 16.3116 21.6285 15.5665 20.4574 15.5833C20.4574 15.5833 19.2803 15.6793 18.6373 16.8066C17.6126 18.6436 15.873 18.1147 15.2128 17.7966C15.0926 17.0383 14.7856 16.5097 14.4557 16.1965C17.0843 15.8964 19.7469 15.515 19.7469 10.969C19.7469 9.66523 19.3833 9.00074 18.6382 8.17525C18.7584 7.87894 19.1505 6.60487 18.5074 4.9669C17.5295 4.65396 15.2651 6.24091 15.2651 6.24091C14.3208 5.97786 13.2966 5.82579 12.3061 5.82579C11.2815 5.82579 10.2703 5.97808 9.33055 6.24091C9.33055 6.24091 7.06187 4.65362 6.07145 4.9669C5.42828 6.62184 5.822 7.87898 5.95126 8.17525C5.18935 9.01752 4.72794 9.66523 4.72794 10.969C4.72794 15.5319 7.50473 15.896 10.1502 16.1965C9.70139 16.5734 9.3377 17.2716 9.3377 18.3933C9.3377 19.9806 9.34901 21.9658 9.34901 22.3637C9.34901 22.66 9.13783 23.0416 8.52362 22.9228C3.81247 21.3355 0.604004 16.8572 0.604004 11.6169C0.604004 5.03488 5.92901 0.057251 12.4771 0.057251L12.4916 0.057943ZM19.4504 16.3796C19.5222 16.4276 19.5221 16.5452 19.4163 16.6257C19.3566 16.71 19.2343 16.7459 19.1704 16.6737C19.0986 16.6257 19.1223 16.5263 19.2043 16.4242C19.264 16.3645 19.3866 16.3316 19.4504 16.3796ZM19.9628 15.9994C20.0108 16.0591 19.9515 16.1468 19.8668 16.1815C19.7825 16.2295 19.7012 16.2295 19.6509 16.1475C19.6169 16.0995 19.6849 16.0167 19.7469 15.9653C19.867 15.954 19.9245 15.954 19.9582 15.9994H19.9628ZM18.4262 17.6839C18.5105 17.7682 18.4743 17.8997 18.3544 17.9803C18.2584 18.1004 18.1251 18.1159 18.0578 18.0282C17.986 17.9802 18.0237 17.8124 18.1295 17.7485C18.2255 17.6283 18.3589 17.6178 18.4262 17.6767V17.6839ZM18.972 16.9892C19.0438 17.0372 19.0438 17.1548 18.972 17.2727C18.8881 17.3687 18.7562 17.4382 18.7056 17.3686C18.6213 17.3206 18.6213 17.1865 18.7056 17.089C18.7774 16.9688 18.8877 16.9163 18.972 16.9892Z"/></svg>';
    case "linkedin":
      return '<svg viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg"><path d="M21.2671 0.0623779H1.67326C0.780539 0.0623779 0.0522461 0.807555 0.0522461 1.71736V21.328C0.0522461 22.217 0.780425 22.9618 1.67326 22.9618H21.2671C22.1562 22.9618 22.884 22.2167 22.884 21.328V1.71736C22.884 0.806686 22.1557 0.0623779 21.2671 0.0623779ZM6.94739 19.6899H3.57387V8.76067H6.94739V19.6899ZM5.25855 7.27085C4.16672 7.27085 3.29036 6.37819 3.29036 5.30254C3.29036 4.21426 4.16623 3.33861 5.25855 3.33861C6.35042 3.33861 7.22675 4.21449 7.22675 5.30254C7.22675 6.37763 6.35095 7.27085 5.25855 7.27085ZM19.6459 19.6899H16.2723V14.3819C16.2723 13.1079 16.2384 11.4867 14.4861 11.4867C12.7337 11.4867 12.467 12.8623 12.467 14.2676V19.6899H9.08076V8.76067H12.3189V10.2465H12.3669C12.8108 9.38742 13.9204 8.49405 15.5754 8.49405C18.9955 8.49405 19.6431 10.7587 19.6431 13.6878L19.6459 19.6899Z"/></svg>'; // LinkedIn icon SVG
    case "telegram":
      return '<svg xmlns="http://www.w3.org/2000/svg"><path d="M12.3221 0.0623779C6.02373 0.0623779 0.914795 5.18829 0.914795 11.5206C0.914795 17.819 6.02373 22.9618 12.3221 22.9618C18.6375 22.9618 23.7465 17.819 23.7465 11.5206C23.7465 5.18829 18.6375 0.0623779 12.3221 0.0623779ZM17.6302 7.85073C17.4646 9.65387 16.7194 14.0687 16.339 16.0836C16.1735 16.9426 15.8602 17.2258 15.5602 17.2438C14.8835 17.3035 14.3714 16.8119 13.7445 16.3847C12.7367 15.7368 12.1573 15.3264 11.1964 14.6789C10.0745 13.9206 10.7982 13.5234 11.446 12.846C11.6115 12.6804 14.5188 10.0185 14.5697 9.76881C14.581 9.7348 14.581 9.62145 14.5217 9.56967C14.4737 9.50996 14.3561 9.52166 14.3104 9.53565C14.1902 9.56966 12.5877 10.6443 9.48079 12.7273C9.03208 13.0455 8.62183 13.1928 8.24063 13.1928C7.84223 13.1815 7.05155 12.96 6.47128 12.7776C5.75979 12.5448 5.18037 12.414 5.23112 12.0157C5.26514 11.8166 5.52742 11.6054 6.09019 11.3894C9.41293 9.93329 11.6309 8.97676 12.7399 8.51112C15.9145 7.19041 16.5747 6.97457 17.0022 6.95764C17.0982 6.95764 17.3034 6.96895 17.4509 7.08838C17.5352 7.17266 17.5983 7.2876 17.5983 7.40136C17.6323 7.55368 17.6302 7.70326 17.6302 7.85073Z"/></svg>'; // Telegram icon SVG
    case "whatsapp":
      return '<svg xmlns="http://www.w3.org/2000/svg"><path d="M20.1848 3.40205C18.0515 1.23487 15.2069 0.0623779 12.1847 0.0623779C5.94972 0.0623779 0.857605 5.15448 0.857605 11.4232C0.857605 13.4041 1.38683 15.3555 2.36028 17.0782L0.756104 22.9618L6.77511 21.3745C8.41324 22.2852 10.28 22.7629 12.1678 22.7629H12.1791C18.4098 22.7629 23.6035 17.6708 23.6035 11.4232C23.6035 8.37977 22.3124 5.5354 20.179 3.40205H20.1848ZM12.1847 20.8454C10.4788 20.8454 8.82817 20.4014 7.38896 19.5417L7.05885 19.3425L3.48648 20.2701L4.44267 16.778L4.21337 16.4314C3.26909 14.9287 2.77413 13.1932 2.77413 11.424C2.77413 6.21336 7.00699 1.98057 12.1837 1.98057C14.7108 1.98057 17.06 2.95839 18.8293 4.74463C20.5986 6.52668 21.6907 8.89275 21.6907 11.424C21.6907 16.6134 17.3571 20.8454 12.1847 20.8454ZM17.3402 13.7851C17.0609 13.6377 15.6725 12.9596 15.4059 12.8624C15.1599 12.7664 14.962 12.7267 14.7796 13.0098C14.5804 13.2894 14.0512 13.9205 13.8869 14.1148C13.7213 14.314 13.5569 14.3477 13.2737 14.1992C11.589 13.3569 10.5138 12.7093 9.40491 10.8256C9.12523 10.3301 9.70503 10.3637 10.2508 9.27221C10.3351 9.09003 10.2736 8.92559 10.2169 8.77664C10.1451 8.62924 9.58581 7.23581 9.34101 6.66023C9.1252 6.11432 8.87544 6.19471 8.70986 6.17793C8.54432 6.16659 8.36316 6.16662 8.16383 6.16662C7.98166 6.16662 7.66833 6.25087 7.42357 6.53018C7.15711 6.83028 6.42886 7.50803 6.42886 8.89625C6.42886 10.2846 7.43681 11.6392 7.5892 11.8381C7.71997 12.0203 9.57006 14.8984 12.4144 16.1216C14.2177 16.8835 14.9118 16.9472 15.805 16.8164C16.3509 16.7446 17.477 16.1397 17.7056 15.4788C17.9551 14.8141 17.9552 14.2555 17.8712 14.12C17.8115 13.9893 17.6251 13.9258 17.3421 13.7901L17.3402 13.7851Z"/></svg>'; // WhatsApp icon SVG
    default:
      return "";
  }
}

export { renderVacancies, renderResumeList, renderResume };
