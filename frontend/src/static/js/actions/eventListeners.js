import { setActiveVacancy } from "./vacancyActions.js";

function addClickEventListeners() {
  document.querySelectorAll(".vacancies__vacancy").forEach((element) => {
    element.addEventListener("click", setActiveVacancy);
  });
}

export { addClickEventListeners };
