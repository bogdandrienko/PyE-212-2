import React, { useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/navbar";
import Footer from "../components/footer";
import axios from 'axios';

export default function Home() {
  // логика тут

  //    getter   setter   react hook   default
  const [userCount, setUserCount] = useState(0);
  const [text, setText] = useState(22222222222);
  const [arr1, setArr1] = useState([]);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [user, setUser] = useState({"username": "", "password": ""});

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

  async function getRequest1() {

      const config = {
        method: "GET",
        timeout: 3000,
        url: `/api/get_users/`,
        data: null,
      };

      axios(config)
      .then(res => {
        const {result} = res.data;
        console.log(result);
        setArr1(res.data["ingredients"]);
      });

      // axios.get(`/api/get_users`)
      //   .then(res => {
      //     console.log(res.data);
      //     console.log(typeof(res.data)); // object
      //     console.log(typeof(res.data["ingredients"])); // array
      //     console.log(typeof(res.data.ingredients)); // array
      //     // setArr1(res.data["ingredients"]);

      //     // res.data["ingredients"].forEach(element => console.log(element));
      //   });
  }

  async function getRequest2() {
    // let req = new XMLHttpRequests();
    // axios.get(`https://jsonplaceholder.typicode.com/users`)
    //   .then(res => {
    //     const persons = res.data;
    //     console.log({ persons });
    //   });

      axios.get(`/api/get_users`)
        .then(res => {
          console.log(res.data);

          // const {users} = res.data;
          // console.log(users);
          // setUserCount(users);
        });

        // let value = true


    // const response = await fetch('api/result/');
    // console.log(response.text());
  }

  async function postRequest() {
    // let req = new XMLHttpRequests();
    // axios.get(`https://jsonplaceholder.typicode.com/users`)
    //   .then(res => {
    //     const persons = res.data;
    //     console.log({ persons });
    //   });
      // axios.post(`/api/create_user/`, { username: 11111111111111 })
      //   .then(res => {
      //     const {result} = res.data;
      //     console.log(result);
      //   });

        const formData = new FormData();
        formData.append("username", username);
        formData.append("password", password);

        const config = {
          method: "POST",
          timeout: 10000,
          url: `/api/create_user/`,
          data: formData,
        };

        axios(config)
        .then(res => {
          const {result} = res.data;
          console.log(result);
        });

        // const formData = new FormData();
        // formData.append("username", username);
        // formData.append("password", password);
        // const config = {
        //     url: `/api/create_user/`,
        //     method: "POST",
        //     timeout: 10000,
        //     timeoutErrorMessage: "timeout error",
        //     headers: {},
        //     data: formData,
        //   };
        // axios(config).then(res => {
        //   const {result} = res.data;
        //   console.log(result);
        // });


    // const response = await fetch('api/result/');
    // console.log(response.text());
  }

  // логика тут

  return (
    <div>
      <main className="custom_main p-0 m-0 w-100">
        <Navbar />
        <h1 className="text-danger">Home page</h1>
        <div>
          Количество пользователей: {userCount}
        </div>

        {arr1.length <= 0 ? (
          <div>Пустой массив!</div>
        ) : (
          <ul>
            {arr1.map(x => (
              <li>{x.username} {x.last_login}</li>
            )
            )}
          </ul>
        )}

        <div className="card">
        <form>
            <img class="mb-4" src="/docs/5.0/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57"/>
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

            <div class="form-floating">
              <input type="text" value={username} onChange={(event) => setUsername(event.target.value)} class="form-control" id="floatingInput" placeholder="name@example.com"/>
              <label for="floatingInput">Username address</label>
            </div>
            <div class="form-floating">
              <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} class="form-control" id="floatingPassword" placeholder="Password"/>
              <label for="floatingPassword">Password</label>
            </div>

            <div class="form-floating">
              <input type="text" value={user.username} onChange={(event) => setUser({"usename": event.target.value, "password": user.password})} class="form-control" id="floatingInput" placeholder="name@example.com"/>
              <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating">
              <input type="password" value={user.password} onChange={(event) => setUser({"usename": user.username, "password": event.target.value})} class="form-control" id="floatingPassword" placeholder="Password"/>
              <label for="floatingPassword">Password</label>
            </div>

            <div class="checkbox mb-3">
              <label>
                <input type="checkbox" value="remember-me"/> Remember me
              </label>
            </div>
            <button class="w-100 btn btn-lg btn-primary" type="button" onClick={()=> postRequest()}>create</button>
            <p class="mt-5 mb-3 text-muted">© 2017–2021</p>
          </form>
        </div>
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
            <button onClick={()=> getRequest1()}>get 1</button>
            <button onClick={()=> getRequest2()}>get 2</button>
            <button onClick={()=> postRequest()}>post</button>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}
