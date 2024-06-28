import Resume from "../models/resume.js";
import Vacancy from "../models/vacancy.js";
import { fetchResume } from "../api.js";
import { renderVacancies, renderResumeList } from "../render.js";

async function displayResume(resumeId) {
  const resumeData = await fetchResume(resumeId);
  const resume = new Resume(resumeData);
  console.log(resume);
  //   renderResume(resume);
}
export { displayResume };
