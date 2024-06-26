import { setActiveVacancy } from "./vacancyActions.js";

function addEventListenerToVacancy(vacancyElement) {
  //   document.querySelectorAll(".vacancies__vacancy").forEach((element) => {
  vacancyElement.addEventListener("click", setActiveVacancy);
  //   });
}

export { addEventListenerToVacancy };
