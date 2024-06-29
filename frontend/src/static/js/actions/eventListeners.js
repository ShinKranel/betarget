import { setActiveVacancy } from "./vacancyActions.js";
import { setActiveResume } from "./resumeListActions.js";
import {
  openChangingStage,
  handleStageInputChanges,
  cancelStageChanges,
  saveStageChanges,
} from "./resumeActions.js";

function addEventListenerToVacancy(vacancyElement) {
  vacancyElement.addEventListener("click", setActiveVacancy);
}

function addEventListenerToResumeList(resumeElement) {
  resumeElement.addEventListener("click", setActiveResume);
}

function addEventListenerToResumeChangeStageButton(buttonElement) {
  buttonElement.addEventListener("click", openChangingStage);
}

function addEventListenerToResumeStageInput(inputElement) {
  inputElement.addEventListener("change", handleStageInputChanges);
}

function addEventListenerToResumeSaveStageButton(saveStageButton) {
  saveStageButton.addEventListener("click", saveStageChanges);
}

function addEventListenerToResumeCancelStageButton(cancelStageButton) {
  cancelStageButton.addEventListener("click", cancelStageChanges);
}

export {
  addEventListenerToVacancy,
  addEventListenerToResumeList,
  addEventListenerToResumeChangeStageButton,
  addEventListenerToResumeStageInput,
  addEventListenerToResumeSaveStageButton,
  addEventListenerToResumeCancelStageButton,
};
