import React from 'react';
import Image from './Image';

function Slideshow({ images, currentImageIndex }) {
  return <Image image={images[currentImageIndex]} />;
}

export default Slideshow;
