// Fonction pour calculer les bonnes réponses et donner le résultat à la fin
const correctAnswer = document.querySelectorAll("#correct");
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
