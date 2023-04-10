import React from 'react';
import './ComponentMainImage.scss';

function ComponentMainImage({ imageUrl }) {
  var image_src = 'https://cdn-gjkdp.nitrocdn.com/JtLCHzGIeDqwNcPkNDwtksvsgIwnNCEu/assets/images/optimized/rev-1664a36/blog/wp-content/uploads/2021/04/how_to_start_a_mug_printing_business-detail_page.png';

   // If the imageUrl is not null, set the image source to the imageUrl
  if (imageUrl) {
    image_src = imageUrl
  }

  return <img src={image_src} className='mainImage' alt='Main' />;
}

export default ComponentMainImage;
