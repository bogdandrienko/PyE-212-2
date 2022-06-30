import React, { useState } from 'react';
import Navbar from "../components/navbar";
import Footer from "../components/footer";
import axios from 'axios';

const Chat = () => {
  // logic is here

  const [texts, setTexts] = useState([]);

  const [text, setText] = useState({});



  async function getAllTexts() {
    const config = {
      method: "GET",
      timeout: 5000,
      url: `/api/chat/read/`,
      data: null,
    };

    axios(config)
    .then(res => {
      const {result} = res.data;
      console.log(result);
      setTexts(result);
    });
  }

  async function getTextById() {
    const config = {
      method: "GET",
      timeout: 5000,
      url: `/api/chat/read/${5}/`,
      data: null,
    };

    axios(config)
    .then(res => {
      const {result} = res.data;
      console.log(result.one);
      setText(result["one"]);
    });
  }

  async function createText() {

    const formData = new FormData();
    formData.append("text", 'новое сообщение');

    const config = {
      method: "POST",
      timeout: 10000,
      url: `/api/chat/create/`,
      data: formData,
    };

    axios(config)
    .then(res => {
      const {result} = res.data;
      console.log(result);
    });
  }

  // logic is here
  return (
    <div>
      <main className="custom_main p-0 m-0 w-100">
        <Navbar />
        <div className='card'>
          <div className='card-header'>
            <button className='btn btn-lg btn-outline-primary p-1 m-1' onClick={getAllTexts}>get all texts</button>
          </div>
          <div className='card-body text-start'>

            {texts.length <= 0 ? (
              <div>Пустой массив!</div>
            ) : (
              <ul>
                {texts.map(x => (
                  <li key={x.id}>#{x.id}:  {x.text}</li>
                )
                )}
              </ul>
            )}
          </div>
          <div className='card-footer'>
            <h1>Design by me</h1>
          </div>
        </div>

        <hr/>

        <div className='card'>
          <div className='card-header'>
            <button className='btn btn-lg btn-outline-success p-1 m-1' onClick={getTextById}>get one text</button>
          </div>
          <div className='card-body text-start'>

            {!text.id ? (
              <div>Пустой объект!</div>
            ) : (
              <div>{text["text 5"]} | {text.id}</div>
            )}
          </div>
          <div className='card-footer'>
            <h1>Design by me</h1>
          </div>
        </div>

        <button className='btn btn-lg btn-outline-warning p-1 m-1' onClick={createText}>send</button>
      

      </main>
      <Footer />
    </div>
  )
}

export default Chat