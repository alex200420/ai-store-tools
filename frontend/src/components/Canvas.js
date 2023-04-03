import React, { useEffect, useState } from 'react';
import Image from './Image';
import Slideshow from './Slideshow';

function Canvas({ images, downloadImages }) {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  
  // set up interval to display images in a slideshow format
  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentImageIndex(prevIndex => {
        if (prevIndex === images.length - 1) {
          return 0;
        } else {
          return prevIndex + 1;
        }
      });
    }, 3000);
    return () => clearInterval(intervalId);
  }, [images]);

  return (
    <div>
      <Slideshow images={images} currentImageIndex={currentImageIndex} />
      <button onClick={downloadImages}>Download Images</button>
    </div>
  );
}

export default Canvas;
