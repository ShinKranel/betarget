import { setActiveVacancy } from "./vacancyActions.js";
import { setActiveResume } from "./resumeListActions.js";
import {
  handleChangeStageButton,
  handleStageInputChanges,
  handleCancelStageButton,
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
  saveStageButton.addEventListener("click", handleSaveStageButton);
}

function addEventListenerToResumeCancelStageButton(cancelStageButton) {
  cancelStageButton.addEventListener("click", handleCancelStageButton);
}

export {
  addEventListenerToVacancy,
  addEventListenerToResumeList,
  addEventListenerToResumeChangeStageButton,
  addEventListenerToResumeStageInput,
  addEventListenerToResumeSaveStageButton,
  addEventListenerToResumeCancelStageButton,
};
