import React from 'react';
import Image from './Image';

function Gallery({ images }) {
  return (
    <div>
      {images.map((image, index) => (
        <Image key={index} image={image} />
      ))}
    </div>
  );
}

export default Gallery;
