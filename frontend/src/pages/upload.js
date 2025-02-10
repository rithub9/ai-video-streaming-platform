import React, { useState } from "react";

const Upload = () => {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://localhost:8002/upload", {
      method: "POST",
      body: formData,
    });

    alert("Video uploaded successfully!");
  };

  return (
    <div>
      <h2>Upload Video</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default Upload;
