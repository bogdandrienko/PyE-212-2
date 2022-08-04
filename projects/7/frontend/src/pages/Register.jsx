import React, { useState } from "react";
import {Base1} from "../components/Base";
import axios from "axios";

export default function Register() {
  const [username, setUsername] = useState("");
  const [passwords, setPasswords] = useState({
    "password1": "",
    "password2": "",
    "password3": "123",
  });

  function Formdata(form) {
    form.preventDefault();

    axios.post(
      
    )

    console.log(`username: ${username}`)
    console.log(`password1: ${passwords.password1}`)
    console.log(`password2: ${passwords.password2}`)
  }


  return (
    <Base1>
      <main className="custom_main_1">
        <div className="container col-xl-10 col-xxl-8 px-4 py-5">
          <div className="row align-items-center g-lg-5 py-5">
            <div className="col-lg-7 text-center text-lg-start">
              <h1 className="display-4 fw-bold lh-1 mb-3">
                Создание нового пользователя
              </h1>
              <p className="col-lg-10 fs-4">
                ...
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
                    value={passwords.password1}
                    onChange={(event)=> setPasswords({password1: event.target.value,  password2: passwords.password2})}
                  />
                  <label for="floatingPassword">Введите пароль от аккаунта</label>
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
                    value={passwords.password2}
                    onChange={(event)=> setPasswords({ ...passwords, password2: event.target.value})}
                  />
                  <label for="floatingPassword">Повторите пароль</label>
                </div>
                <button className="w-100 btn btn-lg btn-primary" type="submit">
                  Создать аккаунт
                </button>
                <hr className="my-4" />
                <small className="text-muted">
                  Нажимая "создать аккаунт" Вы соглашаетесь с правилами
                </small>
              </form>
            </div>
          </div>
        </div>
      </main>
    </Base1>
  );
}
