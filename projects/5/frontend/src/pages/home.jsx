import React, { useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/navbar";
import Footer from "../components/footer";

export default function Home() {
  // логика тут

  //    getter   setter   react hook   default
  const [text, setText] = useState(22222222222);



  const [value, setValue] = useState(0);
  const [multiplayer, setMultiplayer] = useState(1);

  function changeText(text = "") {
    setText(text);
    console.log(text);
  }

  function changeValue(externamlValue = 0) {
    setValue(value + externamlValue*parseInt(multiplayer));
    console.log(value);
  }

  async function fetchMovies() {
    const response = await fetch('api/result/');
    console.log(response.text());
  }

  // логика тут

  return (
    <div>
      <main className="custom_main p-0 m-0 w-100">
        <Navbar />
        <h1 className="text-danger">Home page</h1>
        <div>
          <h6 className="lead">{text}</h6>
          <h5 onClick={() => changeText("Hello")}>click me</h5>
          <input
            type="text"
            value={text}
            onChange={(event) => changeText(event.target.value)}
          ></input>
        </div>
        <div className="card">
          <div className="card-header">
            {value}
          </div>
          <div className="card-body">
            <div className="d-flex justify-content-between">
              <button onClick={()=> changeValue(1)}>increase</button>
              <button onClick={()=> changeValue(-1)}>decrease</button>
            </div>
          </div>
          <div className="card-footer">
            <input
              type="text"
              value={multiplayer}
              onChange={(event) => setMultiplayer(event.target.value)}
            ></input>
          </div>
          <div>
            <button onClick={()=> fetchMovies()}>get</button>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}
