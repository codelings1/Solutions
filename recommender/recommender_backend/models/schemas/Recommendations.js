const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const RecommendationsSchema = new Schema({
  movieName: {
    type: String
  }
});

module.exports = Recommendations = mongoose.model(
  "Recommendations",
  RecommendationsSchema
);
