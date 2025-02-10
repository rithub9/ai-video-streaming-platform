import React, { useEffect, useState } from "react";

const Recommend = () => {
  const [recommendation, setRecommendation] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8003/recommend")
      .then((res) => res.json())
      .then((data) => setRecommendation(data));
  }, []);

  return (
    <div>
      <h2>Recommended Video</h2>
      {recommendation && <h3>{recommendation.recommendation.title}</h3>}
    </div>
  );
};

export default Recommend;
