export async function fetchVacancies() {
    try {
        const response = await fetch("/vacancy", {
            method: "GET",
            headers: {
                accept: "application/json",
            },
        });
        const data = await response.json();
        return data;
    }
    catch (error) {
        throw new Error("Ошибка при получении данных о вакансиях");
    }
}
//# sourceMappingURL=api.js.map