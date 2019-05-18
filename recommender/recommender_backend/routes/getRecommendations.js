const express = require("express");
const router = express.Router();
const RecommendationsProcessor = require("../processors/recommendationProcess");

router.get("/:searchQuery", async (req, resp) => {
  let searchQuery = req.params.searchQuery;
  let respRecommendations = await RecommendationsProcessor.getRecommendations(
    searchQuery
  );
  if (respRecommendations === false) {
    resp.json({
      status: -1,
      msg: "An error occurred"
    });
  } else {
    resp.json(respRecommendations);
  }
});

module.exports = router;
