import { fetchResume } from "../api.js";
import Resume from "../models/resume.js";
import { renderResume } from "../render.js";

async function displayResume(resumeId) {
  const resumeData = await fetchResume(resumeId);
  const resume = new Resume(resumeData);
  console.log(resume);
  renderResume(resume);
}

function openChangingStage() {
  const currentStageElement = document.querySelector(
    ".resume-display__current-stage"
  );
  const changeStageButton = document.querySelector(
    ".resume-display__change-stage"
  );
  const stageInputElement = document.querySelector(
    ".resume-display__stage-input"
  );
  const stageActionsButtons = document.querySelector(
    ".resume-display__stage-actions"
  );

  currentStageElement.style.display = "none";
  changeStageButton.style.display = "none";
  stageInputElement.style.display = "block";
  stageActionsButtons.style.display = "block";
}

function closeChangingStage() {
  const currentStageElement = document.querySelector(
    ".resume-display__current-stage"
  );
  const changeStageButton = document.querySelector(
    ".resume-display__change-stage"
  );
  const stageInputElement = document.querySelector(
    ".resume-display__stage-input"
  );
  const stageActionsButtons = document.querySelector(
    ".resume-display__stage-actions"
  );

  currentStageElement.style.display = "block";
  changeStageButton.style.display = "block";
  stageInputElement.style.display = "none";
  stageActionsButtons.style.display = "none";

  stageInputElement.value = currentStageElement.dataset.stage;
}

function handleStageInputChanges() {
  const stageSaveButton = document.querySelector(".resume-display__save-stage");
  const currentStageElement = document.querySelector(
    ".resume-display__current-stage"
  );
  const stageInputElement = document.querySelector(
    ".resume-display__stage-input"
  );

  const currentStage = currentStageElement.dataset.stage;
  const selectedOption = stageInputElement.value;
  if (currentStage === selectedOption) {
    stageSaveButton.disabled = true;
  } else {
    stageSaveButton.disabled = false;
  }
}

function cancelStageChanges() {
  closeChangingStage();
}

async function saveStageChanges() {
  const currentStageElement = document.querySelector(
    ".resume-display__current-stage"
  );
  const stageInputElement = document.querySelector(
    ".resume-display__stage-input"
  );
  
}
export {
  displayResume,
  openChangingStage,
  closeChangingStage,
  handleStageInputChanges,
  cancelStageChanges,
  saveStageChanges,
};
