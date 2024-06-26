"use strict";

import Resume from "../models/resume.js";
import Vacancy from "../models/vacancy.js";
import { fetchVacancies, fetchResumes } from "../api.js";
import { renderVacancies, renderResumeList } from "../render.js";

async function displayResumeList(vacancy) {
  const vacancyId = vacancy.dataset.id;
  const resumesData = await fetchResumes(vacancyId);
  const resumes = resumesData.map((data) => new Resume(data));
  renderResumeList(resumes);
}

export { displayResumeList };
