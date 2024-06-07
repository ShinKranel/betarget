export interface Vacancy {
  city: string;
  id: number;
  experience: string;
  work_format: string;
  education: string;
  skills: string;
  user_id: number;
  job_title: string;
  company: string;
  salary: number;
  employment_type: string;
  description: string;
}

export async function fetchVacancies(): Promise<Vacancy[]> {
  try {
    const response = await fetch("/vacancy", {
      method: "GET",
      headers: {
        accept: "application/json",
      },
    });
    const data: Vacancy[] = await response.json();
    return data;
  } catch (error) {
    throw new Error("Ошибка при получении данных о вакансиях");
  }
}
