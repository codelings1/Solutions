const express = require("express");
const app = express();
const bodyparser = require("body-parser");
const mongoose = require("mongoose");
const getRecommendations = require("./routes/getRecommendations");

app.use(bodyparser.urlencoded({ extended: false }));
app.use(bodyparser.json());

const db = require("./config/keys").mongoURI;
mongoose
  .connect(db, { useNewUrlParser: true })
  .then(() => console.log("Mongo Server connected successfully"))
  .catch(err => console.log(err));

app.use(function(req, res, next) {
  const allowedOrigins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost:3000/",
    "https://localhost:3000/",
    "http://192.168.0.106:3000/"
  ];
  const origin = req.headers.origin;

  if (allowedOrigins.indexOf(origin) > -1) {
    res.setHeader("Access-Control-Allow-Origin", origin);
  }
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, OPTIONS, PUT, PATCH, DELETE"
  );

  res.setHeader(
    "Access-Control-Allow-Headers",
    "X-Requested-With,content-type",
    "multipart/form-data"
  );
  res.setHeader("Access-Control-Allow-Credentials", true);
  next();
});

app.use("/getRecommendations", getRecommendations);

const port = 4000;
app.listen(port, () => {
  console.log(`Server running on port 4000`);
});
