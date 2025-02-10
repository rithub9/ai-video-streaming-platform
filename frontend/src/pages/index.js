import React, { useEffect, useState } from "react";

const Home = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8002/videos")
      .then((res) => res.json())
      .then((data) => setVideos(data));
  }, []);

  return (
    <div>
      <h1>AI Video Streaming Platform</h1>
      {videos.map((video) => (
        <div key={video.id}>
          <h3>{video.title}</h3>
          <video width="400" controls>
            <source src={video.url} type="video/mp4" />
          </video>
        </div>
      ))}
    </div>
  );
};

export default Home;
