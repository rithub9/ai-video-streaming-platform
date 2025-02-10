export const uploadVideo = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://localhost:8002/upload", {
    method: "POST",
    body: formData,
  });

  return response.json();
};
