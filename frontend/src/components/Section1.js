import React from 'react';
import './Main_Section1.scss';
import logo from '../logo.svg'
import user_icon from '../user_icon.svg'
import ComponentMainImage from './ComponentMainImage.js'

function RenderSection() {
  return (
    <div className="section1">
      <div className="content_box2">
        <div className="flexRow">
          <div className="group">
            <h1 className="title">AI Store Tool</h1>
            <img
              src={logo}
              alt="alt text"
              className="icon1"
            />
          </div>

          <div className="flexRow__spacer" />

          <div className="content_box">
            <h5 className="highlights">Imagine</h5>
          </div>

          <div className="flexRow__spacer1" />

          <div className="content_box1">
            <h5 className="highlights1">History</h5>
          </div>

          <div className="flexRow__spacer2" />
          <div className="flexRow__cell">
            <img
              src={user_icon}
              alt="alt text"
              className="icon"
            />
          </div>
        </div>
      </div>

      <div className="rect" >
        <ComponentMainImage />
      </div>

      <div
        className="content_box3">
        <div className="flexRow1">
          <div className="flexRow1__cell">
            <div className="rect5" />
          </div>
          <div className="flexRow1__spacer"/>
          <div className="flexRow1__cell">
            <div className="rect5"/>
          </div>
          <div className="flexRow1__spacer1" />
          <div className="flexRow1__cell">
            <div className="rect5" />
          </div>
          <div className="flexRow1__spacer" />
          <div className="flexRow1__cell">
            <div className="rect5" />
          </div>
          <div className="flexRow1__spacer1"/>
          <div className="flexRow1__cell1">
            <div className="rect51" />
          </div>
        </div>
      </div>

      <h2 className="medium_title">CREATE YOUR IDEAS</h2>
      <div className="rect1" />
      <div className="buttonBox">
        <button type="button" className="box">
          <span className = "submitButtonStyle">Generate</span>
        </button>
      </div>

    </div>
  );
}

export default RenderSection;