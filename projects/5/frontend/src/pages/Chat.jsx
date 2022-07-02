import React, { useState, useEffect } from 'react';
import {  useSelector, useDispatch  } from 'react-redux';
import Navbar from "../components/navbar";
import Footer from "../components/footer";
import axios from 'axios';

import * as utils from "../components/utils";
import Counter from '../components/counter';
import {getAllTexts} from '../components/actions';


const Chat = () => {
  // logic is here
  const dispatch = useDispatch()
  const loginStore = useSelector((state) => state.loginState);

  const [loginState1, setLoginState1] = useState({
    "initial": "",
    "load": "загрузка",
    "data": "Богдан",
    "error": "Ошибка сервера",
    "fail": "Ошибка клиента",
    "reset": "",
  });

  const [texts, setTexts] = useState([]);

  // console.log(typeof(texts));
  // console.log(typeof(setTexts));

  const [text, setText] = useState({});
  const [sms, setSms] = useState('');

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
      // console.log(result);
      setTexts(result);
    });
  }

  async function getTextById() {
    const config = {
      method: "GET",
      timeout: 5000,
      url: `/api/chat/read/${100}/`,
      data: null,
    };

    axios(config)
    .then(res => {
      const {result} = res.data;
      console.log(result.one);
      setText(result["one"]);
    });
  }

  async function createText(form) {

    form.preventDefault();

    const formData = new FormData();
    formData.append("text", sms);
    
    const utc = new Date(new Date().getTime() - new Date().getTimezoneOffset() * 60000);
    const strUtc = utc.toISOString().split('.')[0].split('T').join(" ")
    formData.append("dateTime", strUtc);

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

    setSms('');
    setTimeout(()=>getAllTexts(), 50);
  }

  async function deleteSmsById(smsId=0) {
    const config = {
      method: "DELETE",
      timeout: 2000,
      url: `/api/chat/delete/${smsId}/`,
      data: null,
    };

    axios(config)
    .then(res => {
      const {result} = res.data;
      console.log(result);
    });

    setTimeout(()=>getAllTexts(), 50);
  }

  // console.log(`sms: ${sms}`);

  useEffect(
    () => {
      dispatch(getAllTexts)
      // console.log(loginStore);
    },
    [sms, dispatch, loginStore],
  );

  // logic is here
  return (
    <div>
      <main className="custom_main p-0 m-0 w-100">
        <Navbar />
        <div>
        <div className="row g-5">
          <div className="col-md-7 col-lg-8 order-md-last">
            <h4 className="d-flex justify-content-between align-items-center mb-3">
              <span className="text-primary">Our chat</span>
              <span className="badge bg-primary rounded-pill">{texts.length}</span>
            </h4>

            {texts.length <= 0 ? (
              <div>Пустой массив!</div>
            ) : (
              <ul className="list-group mb-3">
                {texts.map(x => (
                  <li key={x.id} className="list-group-item d-flex justify-content-between lh-sm">
                    <div>
                      <h6 className="my-0">{x.text}</h6>
                      <small className="text-muted">{utils.GetClearDateTime(x.created_datetime)}</small>
                    </div>
                    <span className="text-muted">#{x.id}</span>
                    <button type="button" onClick={()=>deleteSmsById(x.id)} className="btn btn-outline-danger">удалить</button>
                  </li>
                ))}
              </ul>
            )}

            <form className="card p-2" onSubmit={(form)=> createText(form)}>
              <div className="input-group">
                <input value={sms} onChange={(event) => setSms(event.target.value)} type="text" className="form-control" placeholder="текст сообщения" required/>
                <button type="submit" className="btn btn-secondary">Отправить</button>
              </div>
            </form>

          </div>
          <div className="col-md-5 col-lg-4">
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
          </div>
        </div>
        </div>

      </main>
      <Counter startValue={100}/>
      <Counter startValue={0}/>
      <Counter startValue={0}/>
      <Counter startValue={-1000000000}/>
      <Footer />
    </div>
  )
}

export default Chat