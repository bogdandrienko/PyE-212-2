import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import * as base from "../components/Base";
import * as utils from "../components/utils";
// import { useNavigate } from "react-router-dom";

export const CONST_TOP_BOOKS_LOAD = "CONST_TOP_BOOKS_LOAD"; // данные грузятся, нужно показывать крутилку, а данные спрятать
export const CONST_TOP_BOOKS_DATA = "CONST_TOP_BOOKS_DATA"; // крутилку не показываем, а данные показываем, ошибки прячем
export const CONST_TOP_BOOKS_ERROR = "CONST_TOP_BOOKS_ERROR"; // всё прячем, кроме ошибок
export const CONST_TOP_BOOKS_FAIL = "CONST_TOP_BOOKS_FAIL"; // всё прячем, кроме ошибок
export const CONST_TOP_BOOKS_RESET = "CONST_TOP_BOOKS_RESET"; // всё прячем

export function getAllTopBooks(state = {}, action = null) {
  switch (action.type) {
    case CONST_TOP_BOOKS_LOAD:
      return { load: true, data: undefined, error: undefined, fail: undefined };
    case CONST_TOP_BOOKS_DATA:
      return {
        load: false,
        data: action.payload,
        error: undefined,
        fail: undefined,
      };
    case CONST_TOP_BOOKS_ERROR:
      return {
        load: false,
        data: undefined,
        error: "Ошибка на сервере",
        fail: undefined,
      };
    case CONST_TOP_BOOKS_FAIL:
      return {
        load: false,
        data: undefined,
        error: undefined,
        fail: "Ошибка на клиенте",
      };
    case CONST_TOP_BOOKS_RESET:
      return {
        load: false,
        data: undefined,
        error: undefined,
        fail: undefined,
      };
    default:
      return state;
  }
}

export function TopList() {
  const dispatch = useDispatch();

  const topBooks = useSelector((state) => state.topBooks);
  const { load, data, error, fail } = topBooks;

  const [avatar, setAvatar] = useState(null);
  const [searchText, setSearchText] = useState("");

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
    // const data = {
    //   username: "admin",
    //   password: "admin",
    //   email: "ademail min",
    //   Отчество: "Николай",
    //   аватарка: avatar,
    // };
    // utils.ActionClearReact(`/api/top/`, "123", 500, data);
  }, []);

  useEffect(() => {
    console.log(data);
  }, [data]);

  async function GetTopBooks() {
    try {
      dispatch({ type: CONST_TOP_BOOKS_LOAD }); // ЗАГРУЗКА
      const config = {
        url: `/api/top/?search=${searchText}`,
        method: "GET",
        data: {},
        timeout: 5000,
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      };
      const response = await axios(config);
      if (response.status === 200) {
        dispatch({ type: CONST_TOP_BOOKS_DATA, payload: response.data }); // ДАННЫЕ ПРИШЛИ
      } else {
        dispatch({ type: CONST_TOP_BOOKS_ERROR }); // Ошибка на сервере
      }
    } catch (error) {
      dispatch({ type: CONST_TOP_BOOKS_FAIL }); // Ошибка на клиенте
    }
  }

  function GetData(event){
    event.preventDefault();

    GetTopBooks()
  }

  return (
    <base.Base1>
      <div>
        <h1 className="display-3">Лучшие книги!</h1>
        <div className="card container container-fluid p-0">
          <div className="card-header">
            выберите нужные настройки или найдите интересующую вас книгу:
          </div>
          <div className="card-body">
            <div className="d-flex my-1">
              <Form className="d-flex m-2 p-2" onSubmit={GetData}>
                <div className=" input-group">
                  <Form.Control
                    type="search"
                    placeholder="введите часть названия книги"
                    className="w-50"
                    aria-label="Search"
                    required
                    value={searchText}
                    onChange={(event)=> setSearchText(event.target.value)}
                  />
                  <Button variant="outline-success" type="submit">искать</Button>
                </div>
              </Form>

              <input
                type="file"
                className="form-control w-25"
                onChange={(event) => setAvatar(event.target.files[0])}
              />

              <div className="d-flex my-3 input-group">
                <select class="form-control">
                  <option value="0">Ваша оценка</option>
                </select>
                <button
                  className="btn btn-md btn-outline-success"
                  onClick={GetTopBooks}
                >
                  фильтровать
                </button>
                <button
                  className="btn btn-md btn-outline-success"
                  onClick={() => {
                    dispatch({ type: CONST_TOP_BOOKS_RESET });
                  }}
                >
                  сброс
                </button>
              </div>

              
              <select class="form-control">
                  <option value="0">Сортировка по имени: А-Я</option>
                  <option value="0">Сортировка по имени: Я-А</option>
                  <option value="0">Сортировка по рейтингу: вверх</option>
                  <option value="0">Сортировка по рейтингу: вниз</option>
                  <option value="0">Ваша оценка</option>
                </select>
            </div>
          </div>
          <div className="card-footer">footer</div>
        </div>

        <div>
          {topBooks.load ? (
            <div className="text-success">Идёт загрузка...</div>
          ) : (
            <div className="text-danger"></div>
          )}
          {topBooks.data ? (
            <div className="text-success">{topBooks.data["response"]}</div>
          ) : (
            <div className="text-danger"></div>
          )}
          {/* {topBooks.fail ? <div className="text-success">ошибка клиента есть</div> : <div className="text-danger">ошибки клиента нет</div>} */}
          {/* <div>topBooks</div>
          <div>topBooks</div>
          <div>topBooks</div>
          <div>topBooks</div> */}
        </div>

        <div>
          <div class="container px-4 py-5" id="custom-cards">
            <h2 class="pb-2 border-bottom">Custom cards</h2>

            <div class="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5">
              {data && data["object_list"] ? (
                data["object_list"].map((item) => (
                  <div class="col">
                    <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg custom_card">
                      <div class="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
                        <h2 class="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">
                          {item.title}
                        </h2>
                        <ul class="d-flex list-unstyled mt-auto">
                          <li class="me-auto">
                            <img
                              src="https://github.com/twbs.png"
                              alt="Bootstrap"
                              width="32"
                              height="32"
                              class="rounded-circle border border-white"
                            ></img>
                          </li>
                          <li class="d-flex align-items-center me-3">
                            <svg class="bi me-2" width="1em" height="1em"></svg>
                            <small>California</small>
                          </li>
                          <li class="d-flex align-items-center">
                            <svg class="bi me-2" width="1em" height="1em"></svg>
                            <small>5d</small>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                ))
              ) : (
                <div>данных нет</div>
              )}
            </div>
          </div>
        </div>
      </div>
    </base.Base1>
  );
}
