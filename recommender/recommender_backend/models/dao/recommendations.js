const RecommendationsSchema = require("../schemas/Recommendations");

module.exports.getAllRecommendationsDao = async searchQuery => {
  try {
    let fetchRecord = await RecommendationsSchema.find(
      { $text: { $search: searchQuery } },
      { score: { $meta: "textScore" }, _id: 0 }
    ).sort({ score: { $meta: "textScore" } });
    let responseRecomeendations = fetchRecord.map(data => {
      return data.movieName;
    });
    return responseRecomeendations;
  } catch (err) {
    
    return { status: -1 };
  }
};
