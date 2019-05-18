let RecommendationsDao = require("../models/dao/recommendations");

async function getRecommendations(searchQuery) {
  try {
    let respRecommendationsDao = await RecommendationsDao.getAllRecommendationsDao(
      searchQuery
    );
    return respRecommendationsDao;
  } catch (err) {
    console.log("An error occurred while getting RecommendationsDao : " + err);
    return false;
  }
}

module.exports = { getRecommendations: getRecommendations };
