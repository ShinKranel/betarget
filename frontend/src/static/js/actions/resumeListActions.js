"use strict";

import Resume from "../models/resume.js";
import Vacancy from "../models/vacancy.js";
import { fetchVacancies, fetchResumeList } from "../api.js";
import { renderVacancies, renderResumeList } from "../render.js";
import { displayResume } from "./resumeActions.js";

let currentActiveResume = null;

async function displayResumeList(vacancyId) {
  const resumesData = await fetchResumeList(vacancyId);
  const resumes = resumesData.map((data) => new Resume(data));
  renderResumeList(resumes);
}

async function setActiveResume(event) {
  event.preventDefault();
  const targetElement = event.currentTarget;
  if (currentActiveResume) {
    currentActiveResume.classList.remove("resume-list__resume_active");
  }
  targetElement.classList.add("resume-list__resume_active");
  currentActiveResume = targetElement;
  displayResume(currentActiveResume.dataset.id);
}

export { displayResumeList, setActiveResume };
