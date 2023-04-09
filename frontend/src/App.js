import React from 'react';
import Headroom from 'react-headroom';
import Logo from './components/Logo';
import RenderSection from './components/Section1.js';
import './components/Main.scss';

function App() {
  return (
    <React.Fragment>
      <div className='main'>
        <RenderSection />
      </div>
    </React.Fragment>
  );
}

export default App;