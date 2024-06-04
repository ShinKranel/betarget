// fetch("/vacancy/")
//   .then(function (response) {
//     if (response.ok) {
//       return response.json();
//     } else {
//       throw new Error("Ошибка запроса: " + response.status);
//     }
//   })
//   .then(function (data) {
//     console.log("data received");
//   })
//   .catch(function (error) {
//     // Обработка ошибок
//   });

// import axios from "axios";

axios
  .get("http://127.0.0.1:5500/vacancy")
  // .get("https://fortnite-api.com/v1/map")
  .then((response) => {
    if (response.status === 200) {
      console.log("Request successful");
      console.log("Data:", response.data);
    } else {
      console.error("Request failed with status:", response.status);
    }
  })
  .catch((error) => {
    console.error(error);
  });
