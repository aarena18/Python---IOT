// Fonction pour calculer les bonnes réponses et donner le résultat à la fin
const correctAnswer = document.querySelectorAll("#correct");
const btnResult = document.getElementById("submit");

let score = 0;

function result() {
  score = 0;
  correctAnswer.forEach((answer) => {
    answer.checked ? score++ : score;
  });
  document.getElementById(
    "my-score"
  ).innerText = `Vous avez marqué ${score} points.`;

  if (score === 3) {
    document.getElementById(
      "my-score"
    ).innerText += ` 🎉 Bravo, vous avez tout bon 🎉 !`;
  }
}
//Fonction pour envoyer les datas au serveur

btnResult.addEventListener("click", () => {
  fetch("http://localhost:3000/api/quizz", {
    method: "POST",
    headers: {
      "Content-Type": "application/json;charset=utf-8",
    },
    body: JSON.stringify({
      data: "result",
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.log(error);
    });
});
