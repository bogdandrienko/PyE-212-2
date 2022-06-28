import React, { useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/navbar";
import Footer from "../components/footer";
import axios from 'axios';

export default function Login() {
    // логика тут

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const [resultQuery, setResultQuery] = useState("Запрос не был вызван!");

    const [user, setUser] = useState({});

    function checkUser() {
      
      const config = {
        method: "GET",
        timeout: 5000,
        url: `/api/check_user/?username=${username}`,
        data: null,
      };

      axios(config)
      .then(res => {
        const {result} = res.data;
        console.log(result);
        setResultQuery(result);
      });

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
  
    return (
      <div>
        <main className="custom_main p-0 m-0 w-100">
          <Navbar />

          <div class="px-4 py-5 my-5 text-center">
            <img class="d-block mx-auto mb-4" src="/docs/5.0/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57"/>
            <h1 class="display-5 fw-bold">Centered hero</h1>
            <div class="col-lg-6 mx-auto">
              <p class="lead mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
              
              <div className="d-flex">
                <div>{resultQuery}</div>
                <input value={username} onChange={(event)=> {setUsername(event.target.value)}} className="form-control m-1" type='text'></input>
                <input value={password} onChange={(event)=> {setPassword(event.target.value)}}  className="form-control m-1" type='password'></input>
              </div>
              <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
                <button onClick={checkUser} type="button" class="btn btn-primary btn-lg px-4 gap-3">check</button>
                <button onClick={()=> {loginUser("222222222222")}} type="button" class="btn btn-outline-secondary btn-lg px-4">login</button>
              </div>
            </div>
          </div>
          
        </main>
        <Footer />
      </div>
    );
  }