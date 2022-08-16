import { useEffect, useState } from "react";
import axios from "axios";
import * as base from "../components/Base";
// import { useNavigate } from "react-router-dom";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";


// Тут модераторы или администраторы сайта будут добавлять новые 
// книги полностью: картинка, документа, описание...

export function AdminPage() {
  const [avatar, setAvatar] = useState(null);


  // const navigate = useNavigate();

  // async function getAllCategories() {
  //   try {
  //     const token = `${"Bogdan"}:${"bogdan"}`;
  //     const encodedToken = btoa(token);
  //     console.log(token);
  //     console.log(encodedToken);

  //     const config = {
  //       method: "GET",
  //       timeout: 5000,
  //       timeoutErrorMessage: "timeout error",
  //       url: `/api/categories?limit=${5}&page=${1}`,
  //       data: {},
  //     };
  //     const headers = {
  //       Authorization: `Bearer `,
  //     };
  //     // const response = await axios(config, headers);
  //     // const response = await axios.get(`/api/categories?limit=${5}&page=${1}`, headers);
  //     const response = await axios.get(`/api/categories?limit=${5}&page=${1}`, {
  //       headers: {
  //         Authorization: `Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwMTM1MDgwLCJpYXQiOjE2NjAwNDg2ODAsImp0aSI6IjFiZjczMzM0YzRmNjQ0ZmY4MDE1MGZkZjZjMDc1ZWNlIiwidXNlcl9pZCI6MX0.g4nUUGPrRgBpiTp0doJ4JHavLTIjSRg1mpzWgSV6gMs`,
  //       },
  //     });

  //     // const config = {
  //     //   url: `/api/categories?limit=${5}&page=${1}`,
  //     //   method: "GET",
  //     //   timeout: 5000,
  //     //   timeoutErrorMessage: "timeout error",
  //     //   // headers: {
  //     //   //   Authorization: `Basic ${"Bogdan bogdan"}`,
  //     //   // },
  //     //   data: {},
  //     // };
  //     // const response = await axios(config);
  //     if (response.data) {
  //       console.log(response.data);
  //     } else {
  //       console.log(response);
  //       console.log("ошибка");
  //     }
  //   } catch (error) {
  //     //navigate("/login");
  //     console.log(typeof error);
  //     console.log(`ошибка: ${error}`);
  //   }
  // }

  // async function get_token() {
  //   let username = "admin";
  //   let password = "admin";
  //   const response = await axios.post(`/api/token/`, { username, password });

  //   localStorage.setItem("token", response.data.access);

  //   console.log(response.data);
  // }

  // async function get_data() {
  //   const response = await axios.post(
  //     `/api/get_data/`,
  //     {},
  //     {
  //       headers: {
  //         Authorization: `Bearer ${localStorage.getItem("token")}`,
  //       },
  //     }
  //   );
  //   console.log(response.data);
  // }

  useEffect(() => {

    const data = {
      "username": "admin",
      "password": "admin",
      "email": "ademail min",
      "Отчество": "Николай",
      "аватарка": avatar,
    }

    Action1(`/api/top/`, "123", 500, data);
  }, []);

  function Clic(){
    
    const data = {
      "username": "admin",
      "password": "admin",
      "email": "ademail min",
      "Отчество": "Николай",
      "аватарка": avatar,
    }

    Action1(`/api/top/`, "POST", data, 5000);
  }

  async function Action1(url, method="GET", data={}, timeout=3000) {
    const formData = new FormData();
    Object.keys(data).forEach(function(key){
      formData.append(key.toString(), data[key])
    });
    const config = {
      url: url,
      method: method,
      data: formData,
      timeout: timeout,
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      }
    };
    const response = await axios(config)
    console.log(response.data);
  }

  return (
    <base.Base1>
      <div>
        <h1 className="display-3">Лучшие книги!</h1>
        <div className="card container container-fluid p-0">
          <div className="card-header">выберите нужные настройки или найдите интересующую вас книгу:</div>
          <div className="card-body">

            <div className="d-flex my-1">

              <Form className="d-flex m-2 p-2">
                <div className=" input-group">
                  <Form.Control
                    type="search"
                    placeholder="введите часть названия книги"
                    className="w-25"
                    aria-label="Search"
                  />
                  <Button variant="outline-success">искать</Button>
                </div>
              </Form>

              <input type="file" className="form-control" onChange={(event)=> setAvatar(event.target.files[0])}/>

              <div className="d-flex my-3 input-group">

              <select
                className="form-control"
              >
                <option value="0">
                  Ваша оценка
                </option>
              </select>
              <button className="btn btn-md btn-outline-success" onClick={Clic}>фильтровать</button>
              </div>
            </div>
          </div>
          <div className="card-footer">footer</div>
        </div>

        <div>
        <div className="container px-4 py-5" id="custom-cards">
    <h2 className="pb-2 border-bottom">Custom cards</h2>

    <div className="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5">

      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg custom_card">
          <div className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
            <h2 className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">Another longer title belongs here</h2>
            <ul className="d-flex list-unstyled mt-auto">
              <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"></img>
              </li>
              <li className="d-flex align-items-center me-3">
                <svg className="bi me-2" width="1em" height="1em"></svg>
                <small>California</small>
              </li>
              <li className="d-flex align-items-center">
                <svg className="bi me-2" width="1em" height="1em"></svg>
                <small>5d</small>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg custom_card">
          <div className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
            <h2 className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">Another longer title belongs here</h2>
            <ul className="d-flex list-unstyled mt-auto">
              <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"></img>
              </li>
              <li className="d-flex align-items-center me-3">
                <svg className="bi me-2" width="1em" height="1em"></svg>
                <small>California</small>
              </li>
              <li className="d-flex align-items-center">
                <svg className="bi me-2" width="1em" height="1em"></svg>
                <small>5d</small>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg custom_card">
          <div className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
            <h2 className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">Another longer title belongs here</h2>
            <ul className="d-flex list-unstyled mt-auto">
              <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"></img>
              </li>
              <li className="d-flex align-items-center me-3">
                <svg className="bi me-2" width="1em" height="1em"></svg>
                <small>California</small>
              </li>
              <li className="d-flex align-items-center">
                <svg className="bi me-2" width="1em" height="1em"></svg>
                <small>5d</small>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg custom_card">
          <div className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
            <h2 className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">Another longer title belongs here</h2>
            <ul className="d-flex list-unstyled mt-auto">
              <li className="me-auto">
                <img src="https://github.com/twbs.png" alt="Bootstrap" width="32" height="32" className="rounded-circle border border-white"></img>
              </li>
              <li className="d-flex align-items-center me-3">
                <svg className="bi me-2" width="1em" height="1em"></svg>
                <small>California</small>
              </li>
              <li className="d-flex align-items-center">
                <svg className="bi me-2" width="1em" height="1em"></svg>
                <small>5d</small>
              </li>
            </ul>
          </div>
        </div>
      </div>

    </div>
  </div>
        </div>
        
      </div>
    </base.Base1>
  );
}
