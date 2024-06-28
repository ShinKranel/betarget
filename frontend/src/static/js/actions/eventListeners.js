import { setActiveVacancy } from "./vacancyActions.js";
import { setActiveResume } from "./resumeListActions.js";

function addEventListenerToVacancy(vacancyElement) {
  vacancyElement.addEventListener("click", setActiveVacancy);
}

function addEventListenerToResumeList(resumeElement) {
  resumeElement.addEventListener("click", setActiveResume);
}

export { addEventListenerToVacancy, addEventListenerToResumeList };
