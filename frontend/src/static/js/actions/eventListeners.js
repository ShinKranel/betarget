import { setActiveVacancy } from "./vacancyActions.js";
import { setActiveResume } from "./resumeListActions.js";
import {
  handleChangeStageButton,
  handleStageInputChanges,
  handleSaveStageButton,
} from "./resumeActions.js";

function addEventListenerToVacancy(vacancyElement) {
  vacancyElement.addEventListener("click", setActiveVacancy);
}

function addEventListenerToResumeList(resumeElement) {
  resumeElement.addEventListener("click", setActiveResume);
}

function addEventListenerToResumeChangeStageButton(buttonElement) {
  buttonElement.addEventListener("click", handleChangeStageButton);
}

function addEventListenerToResumeStageInput(inputElement) {
  inputElement.addEventListener("change", handleStageInputChanges);
}

function addEventListenerToResumeSaveStageButton(saveStageButton) {
  saveStageButton.addEventListener("change", handleSaveStageButton);
}

export {
  addEventListenerToVacancy,
  addEventListenerToResumeList,
  addEventListenerToResumeChangeStageButton,
  addEventListenerToResumeStageInput,
  addEventListenerToResumeSaveStageButton,
};
