import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import Base, {Base1} from "../components/Base";
import axios from "axios";
import {useNavigate} from "react-router-dom";
import * as bases from '../components/Base'
import * as constants from "../components/Constants";



function Login() {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  // localstorage
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  async function Formdata(form) {
    form.preventDefault();




    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    const response = await axios.post(`/api/login/`, formData);
    //const response = await axios.post(`/api/token/`, formData);















    console.log(`ВХОД ${response.data.response.access}`)

    
    localStorage.setItem("token", response.data.response.access);


    dispatch({ type: bases.CONST_USER_LOGIN.data, payload: response.data.response.access }); // ЗАГРУЗКА
    dispatch({ type: constants.C_Token.data, payload: response.data.response.access });
    
  }

  function TogglePasswordVisibility(uuid="") {
      let x = document.getElementById(uuid);
      if (x.type === "password") {
        x.type = "text";
      } else {
        x.type = "password";
      }
  }

  function GetData() {
    const accessToken = localStorage.getItem('token')

    axios.get("/backend_api/get_books/", { headers: {
      'Authorization': `Bearer ${accessToken}`
    }}).then(
      (response)=> {
        console.log(response);
      }
    ).catch((error)=> {
      localStorage.removeItem("token");
    });
  }

  return (
    <Base1>
      <main className="custom_main_1">
        <div className="container col-xl-10 col-xxl-8 px-4 py-5">
          <div className="row align-items-center g-lg-5 py-5">
            <div className="col-lg-7 text-center text-lg-start">
              <h1 className="display-4 fw-bold lh-1 mb-3">
                Вход
              </h1>
              <p className="col-lg-10 fs-4">
                ... тут будет умная цитата ...
              </p>
            </div>
            <div className="col-md-10 mx-auto col-lg-5">
              <form className="p-4 p-md-5 border rounded-3 bg-light" onSubmit={Formdata}>
                <div className="form-floating mb-3">
                  <input
                    type="text"
                    className="form-control"
                    id="floatingInput"
                    placeholder="name"
                    min="8"
                    max="16"
                    required
                    value={username}
                    onChange={(event)=> setUsername(event.target.value)}
                  />
                  <label for="floatingInput">Имя пользователя</label>
                </div>
                <div className="form-floating mb-3">
                  <input
                    type="password"
                    className="form-control"
                    id="floatingPassword"
                    placeholder="Password"
                    min="8"
                    max="16"
                    required
                    value={password}
                    onChange={(event)=> setPassword(event.target.value)}
                  />
                  <label for="floatingPassword">Введите пароль от аккаунта</label>
                </div>
                <label>показать пароль</label>
                <input onClick={()=> TogglePasswordVisibility("floatingPassword")} type="checkbox" id="vehicle1" name="vehicle1" value="Bike" placeholder="показать пароль"></input>
                <button className="w-100 btn btn-lg btn-primary" type="submit">
                  Войти
                </button>
              </form>
            </div>
          </div>
        </div>
      </main>
    </Base1>
  );
}

export default Login;
