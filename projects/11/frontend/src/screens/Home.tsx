import axios from "axios";
import React, { useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import CounterCustom from "../components/CounterCustom";
import CounterRedux from "../components/CounterRedux";
import * as actions from "../components/Actions";

axios.defaults.baseURL = "http://127.0.0.1:8000"

function Home() {
  const dispatch = useDispatch();

  const [value1, setValue1] = useState(0);

  function getData(value: number) {
    setValue1(value);
  }

  // @ts-ignore
  const counterRedux = useSelector((state) => state.counterRedux); // {load, data, eror}

  return (
    <div>
      <div>
        <h1>React redux typescript axios jwt</h1>
      </div>
      <div><button onClick={()=>actions.getToken(dispatch)}>getToken</button></div>
      <div>Значение из детей: {counterRedux.data}</div>
      <main>
        <CounterRedux defaultValue={100} multiply={3} />
        <CounterCustom defaultValue={666} multiply={3} callbackGetData={getData} />
        <CounterCustom defaultValue={1} multiply={1} callbackGetData={getData} />
        <CounterCustom defaultValue={-100} multiply={-1} callbackGetData={getData} />
      </main>
    </div>
  );
}

export default Home;
