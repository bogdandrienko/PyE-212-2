import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import Navbar from "../components/navbar";
import Footer from "../components/footer";
import axios from 'axios';

export const CHECK_USER_LOAD = "CHECK_USER_LOAD_CONSTANT";
export const CHECK_USER_DATA = "CHECK_USER_DATA_CONSTANT";
export const CHECK_USER_ERROR = "CHECK_USER_ERROR_CONSTANT";
export const CHECK_USER_FAIL = "CHECK_USER_FAIL_CONSTANT";
export const CHECK_USER_RESET = "CHECK_USER_RESET_CONSTANT";

export const CheckUserReducer = (state = {}, action = null) => {
  switch (action.type) {
    case CHECK_USER_LOAD:
      return { load: true };
    case CHECK_USER_DATA:
      return { load: false, data: action.payload };
    case CHECK_USER_ERROR:
      return { error: "ошибка на сервере" };
    case CHECK_USER_FAIL:
      return { fail: "ошибка на клиенте" };
    case CHECK_USER_RESET:
      return {};
    default:
      return state;
  }
};

export const CheckUserAction = (username) => async (dispatch, getState) => {
  try {
    dispatch({
      type: CHECK_USER_LOAD,
    });

    // const { ReduxExampleStore: ReduxExampleStore } = getState();

    const config = {
      method: "GET",
      timeout: 5000,
      url: `/api/check_user/?username=${username}`,
      data: null,
    };
    const response = await axios(config);
    // console.log(response);

    const { data } = response;
    if (data) {
      dispatch({
        type: CHECK_USER_DATA,
        payload: data,
      });
    } else {
      dispatch({
        type: CHECK_USER_ERROR,
        payload: data,
      });
    }
  } catch (error) {
    console.log(error);
    dispatch({
      type: CHECK_USER_FAIL,
      payload: error,
    });
  }
};

export default function Login() {
    // логика тут
    const dispatch = useDispatch();

    

    const CheckUserStore = useSelector((state) => state.CheckUserStore);
    const {
      load: load,
      data: data,
      error: error,
      fail: fail,
      reset: reset,
    } = CheckUserStore;

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const [resultQuery, setResultQuery] = useState("Запрос не был вызван!");

    const [user, setUser] = useState({});

    function checkUser() {

      // dispatch({ type: CHECK_USER_LOAD });
      dispatch(CheckUserAction(username));
      
      // const config = {
      //   method: "GET",
      //   timeout: 5000,
      //   url: `/api/check_user/?username=${username}`,
      //   data: null,
      // };

      // axios(config)
      // .then(res => {
      //   const {result} = res.data;
      //   console.log(result);
      //   setResultQuery(result);
      // });

    }

    function loginUser(someText="111111111") {

      const formData = new FormData();
      formData.append("username", username);
      formData.append("password", password);
      formData.append("apps", [1,2,3,4.5]);
      formData.append("someText", someText);
      
      const config = {
        method: "POST",
        timeout: 7000,
        url: `/api/login_user/`,
        data: formData,
      };

      axios(config)
      .then(res => {
        const {result} = res.data;
        console.log(result);
      });

    }
      
    // логика тут

    useEffect(() => {
      console.log(`load: ${load}`);
      console.log(`data: ${data}`);
      console.log(`error: ${error}`);
      console.log(`fail: ${fail}`);
    }, [CheckUserStore]);
  
    return (
      <div>
        <main className="custom_main p-0 m-0 w-100">
          <Navbar />

          <div className="px-4 py-5 my-5 text-center">
            <img className="d-block mx-auto mb-4" src="/docs/5.0/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57"/>
            <h1 className="display-5 fw-bold">Centered hero</h1>
            <div className="col-lg-6 mx-auto">
              <p className="lead mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
              
              <div className="d-flex">
                <div>{resultQuery}</div>
                <input value={username} onChange={(event)=> {setUsername(event.target.value)}} className="form-control m-1" type='text'></input>
                <input value={password} onChange={(event)=> {setPassword(event.target.value)}}  className="form-control m-1" type='password'></input>
              </div>
              <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
                <button onClick={checkUser} type="button" className="btn btn-primary btn-lg px-4 gap-3">check</button>
                <button onClick={()=> {loginUser("222222222222")}} type="button" className="btn btn-outline-secondary btn-lg px-4">login</button>
              </div>
            </div>
          </div>
          
        </main>
        <Footer />
      </div>
    );
  }