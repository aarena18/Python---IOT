///////////////// IMPORT /////////////////////
import express from "express";
import http from "http";
import cors from "cors";

///////////////// CONST /////////////////////

const app = express();
const httpServer = http.createServer(app);
const port = 3000;

///////////////// MIDDLEWARE /////////////////////

app.use(express.json());
app.use(cors());

///////////////// ROUTES /////////////////////

app.get("/api/quizz", (req, res) =>
  res.send(JSON.stringify({ msg: "data received" }))
);
// get data from the client
app.post("/api/quizz", (req, res) => {
  console.log(req.body);
  res.send(JSON.stringify({ msg: "data received" }));
});

// show the data from the client
app.get("/api/quizz", (req, res) => {
  res.send(JSON.stringify({ msg: "data received" }));
});

///////////////// LISTEN /////////////////////

httpServer.listen(port, () =>
  console.log(`Example app listening on port ${port}!`)
);
