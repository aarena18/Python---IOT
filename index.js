///////////////// IMPORT /////////////////////

import express from "express";
import http from "http";


///////////////// CONST /////////////////////

const app = express();
const httpServer = http.createServer(app);
const port = 3000;

///////////////// ROUTES /////////////////////

app.get("/api/quizz", (req, res) => res.send("you'll find the quizz here 🤓"));

///////////////// LISTEN /////////////////////

httpServer.listen(port, () =>
  console.log(`Example app listening on port ${port}!`)
);
