// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// // export default App;
// import React, { useState } from 'react';
// import Canvas from './components/Canvas';
// import Gallery from './components/Gallery';
// import PromptForm from './components/PromptForm';

// function App() {
//   const [images, setImages] = useState([]);

//   const generateImages = async prompt => {
//     const response = await fetch('/generate_images', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify({ prompt }),
//     });
//     const { images } = await response.json();
//     setImages(images);
//   };

//   const upscaleImage = async image => {
//     const response = await fetch('/upscale_image', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify({image})
//     });
//     const { upscaledImage } = await response.json();
//     const updatedImages = [...images, upscaledImage];
//     setImages(updatedImages);0
//   };

//   const downloadImages = () => {
//   images.forEach(image => {
//   const link = document.createElement('a');
//   link.href = image;
//   link.download = 'generated_image.jpg';
//   link.click();
//   });
//   };
  
//   return (
//       <div>
//         <PromptForm generateImages={generateImages} upscaleImage={upscaleImage} />
//         <div>
//           <h2>Canvas</h2>
//           <Canvas images={images} downloadImages={downloadImages} />
//         </div>
//         <div>
//           <h2>Gallery</h2>
//           <Gallery images={images} />
//         </div>
//       </div>
//     );
//   }
  
//   export default App;

import { useState, useEffect, useRef } from 'react';
import JSZip from 'jszip';
import { saveAs } from 'file-saver';

function ImageGenerationApp() {
  const [images, setImages] = useState([]);
  const [prompt, setPrompt] = useState('');

  const canvasRef = useRef(null);

  useEffect(() => {
    if (images.length === 0) {
      return;
    }
    // Function to draw an image on the canvas
    const drawImage = (imageIndex) => {
      const canvas = canvasRef.current;
      const context = canvas.getContext('2d');
      const image = new Image();
      const objectUrl = URL.createObjectURL(images[imageIndex]);
      image.onload = () => {
        context.drawImage(image, 0, 0, canvas.width, canvas.height);
        URL.revokeObjectURL(objectUrl);
      };
      image.onerror = () => {
        console.error('Failed to load image:', images[imageIndex]);
        URL.revokeObjectURL(objectUrl);
      };
      image.src = objectUrl;
    };

    // Start slideshow of the generated images
    let currentIndex = 0;
    const intervalId = setInterval(() => {
      drawImage(currentIndex);
      currentIndex = (currentIndex + 1) % images.length;
    }, 3000);

    // Cleanup function to clear the interval
    return () => clearInterval(intervalId);
  }, [images]);

  // Function to generate the images
  const generateImages = async () => {
    const response = await fetch('/generate_images', {
      method: 'POST',
      body: JSON.stringify({ prompt }),
    });
    const generatedImages = await response.json();
    setImages(generatedImages);
  };

  // Function to upscale an image
  const upscaleImage = async (imageIndex) => {
    const response = await fetch('/upscale_image', {
      method: 'POST',
      body: JSON.stringify({ image: images[imageIndex] }),
    });
    const upscaledImage = await response.blob();
    const updatedImages = [...images];
    updatedImages[imageIndex] = upscaledImage;
    setImages(updatedImages);
  };

  // Function to download all the images
  const downloadImages = () => {
    const zip = new JSZip();
    for (let i = 0; i < images.length; i++) {
      const fileName = `image_${i}.jpg`;
      zip.file(fileName, images[i]);
    }
    zip.generateAsync({ type: 'blob' }).then(function (content) {
      saveAs(content, 'generated_images.zip');
    });
  };

  return (
    <div>
      <h1>Image Generation App</h1>
      <div>
        <label htmlFor="prompt">Prompt:</label>
        <input type="text" id="prompt" value={prompt} onChange={(e) => setPrompt(e.target.value)} />
        <button id="generate-btn" onClick={generateImages}>Generate Images</button>
        <button id="upscale-btn" onClick={() => upscaleImage(0)}>Upscale Images</button>
        <button id="download-btn" onClick={downloadImages}>Download Images</button>
      </div>
      <canvas ref={canvasRef} width="600" height="400"></canvas>
    </div>
  );
}

export default ImageGenerationApp;
