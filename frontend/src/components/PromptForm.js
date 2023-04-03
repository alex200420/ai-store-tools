import React, { useState } from 'react';

function PromptForm({ generateImages, upscaleImage }) {
  const [prompt, setPrompt] = useState('');

  const handleSubmit = event => {
    event.preventDefault();
    generateImages(prompt);
  };

  const handleImageUpload = event => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
      upscaleImage(reader.result);
    };
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Prompt:
          <input type="text" value={prompt} onChange={event => setPrompt(event.target.value)} />
        </label>
        <button type="submit">Generate Images</button>
      </form>
      <input type="file" accept="image/*" onChange={handleImageUpload} />
    </div>
  );
}

export default PromptForm;
