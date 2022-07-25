import React, { useState } from "react";
import Base, {Base1} from "../components/Base";
import { Paginator } from "../components/ui";
import axios from "axios";
import {useNavigate} from "react-router-dom";

export default function Auth() {
  const [auth, setAuth] = useState(false);


  function Login(form){
    form.preventDefault();
    const formData = new FormData();
    formData.append("username", username)
    formData.append("password", password)

    axios
    .post("/login/", formData)
    .then(
      (result)=> {
        console.log(result)
        if (result.status == 200){
          setAuth(true)
        } else {
          setAuth(false)
        }
      }
    ).catch(()=> {
      setAuth(false)
    });
  }

  function Logout(form){
    setAuth(false)
  }

  // localstorage
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // function Formdata(form) {
  //   form.preventDefault();

  //   axios.post("/login/", {"username": username, "password": password }).then(
  //     (result)=> {
  //       console.log(result);
  //     }
  //   );
  // }

  function TogglePasswordVisibility(uuid="") {
      let x = document.getElementById(uuid);
      if (x.type === "password") {
        x.type = "text";
      } else {
        x.type = "password";
      }
  }

  // function GetData() {
  //   const accessToken = localStorage.getItem('token')

  //   axios.get("/backend_api/get_books/", { headers: {
  //     'Authorization': `Bearer ${accessToken}`
  //   }}).then(
  //     (response)=> {
  //       console.log(response);
  //     }
  //   ).catch((error)=> {
  //     localStorage.removeItem("token");
  //   });
  // }

  return (
    <Base1>
      <main className="custom_main_1">
        <div class="container col-xl-10 col-xxl-8 px-4 py-5">
          <div class="row align-items-center g-lg-5 py-5">
            <div class="col-lg-7 text-center text-lg-start">
              <h1 class="display-4 fw-bold lh-1 mb-3">
                Вход
              </h1>
              <p class="col-lg-10 fs-4">
                ... тут будет умная цитата ...
              </p>
            </div>
            {auth ? "Вы авторизованы" : "Вы не авторизованы"}
            <div class="col-md-10 mx-auto col-lg-5">
              <form class="p-4 p-md-5 border rounded-3 bg-light" onSubmit={Login}>
                <div class="form-floating mb-3">
                  <input
                    type="text"
                    class="form-control"
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
                <div class="form-floating mb-3">
                  <input
                    type="password"
                    class="form-control"
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
                <button class="w-50 btn btn-lg btn-primary" type="submit">
                  Войти
                </button>
                <button onClick={Logout} class="w-50 btn btn-lg btn-danger" type="button">
                  Выйти
                </button>
              </form>
            </div>
          </div>
        </div>
      </main>
    </Base1>
  );
}
