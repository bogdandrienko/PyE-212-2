import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import * as base from "../components/Base";
import * as utils from "../components/utils";
import * as ui from "../components/ui";

export const Constant_CreateBook = utils.ConstructorConstantRedux(
  "Constant_CreateBook"
);

export const Constant_ChangeBook = utils.ConstructorConstantRedux(
  "Constant_ChangeBook"
);

// КОНСТАНТА ПОЛУЧЕНИЯ
export const Constant_TopBooks =
  utils.ConstructorConstantRedux("Constant_TopBooks");

// РЕДЮСЕР ПОЛУЧЕНИЯ (ПЕРЕКЛЮЧАТЕЛЬ СОСТОЯНИЙ ОДНОГО ОБЪЕКТА ПО КОНСТАНТАМ)
export const Reducer_TopBooks =
  utils.ConstructorReducerRedux(Constant_TopBooks);

// КОНСТАНТА УДАЛЕНИЯ
export const Constant_DeleteBook = utils.ConstructorConstantRedux(
  "Constant_DeleteBook"
);

// РЕДЮСЕР ПОЛУЧЕНИЯ (ПЕРЕКЛЮЧАТЕЛЬ СОСТОЯНИЙ ОДНОГО ОБЪЕКТА ПО КОНСТАНТАМ)
export const Reducer_DeleteBook =
  utils.ConstructorReducerRedux(Constant_DeleteBook);

export function TopList() {
  const dispatch = useDispatch();
  const topBooks = useSelector((state) => state.topBooks);
  const deleteBook = useSelector((state) => state.deleteBook);
  const [avatar, setAvatar] = useState(null);
  const [searchText, setSearchText] = useState("");

  async function removeBook(id) {
    dispatch(
      utils.ConstructorActionRedux(
        `/api/book/${id}/`,
        "DELETE",
        {},
        3000,
        Constant_DeleteBook
      )
    );
  }

  async function GetTopBooks(event) {
    if (event) {
      event.preventDefault(); // отключаем перезагрузку страницы
    }

    dispatch(
      utils.ConstructorActionRedux(
        `/api/top/?search=${searchText}`,
        "GET",
        {},
        5000,
        Constant_TopBooks
      )
    );
  }

  useEffect(
    () => {
    if (!topBooks.data) {
      GetTopBooks();
    }
  },[]);

  useEffect(() => {
    console.log("topBooks", topBooks);
  }, [topBooks]);

  useEffect(() => {
    console.log("deleteBook", deleteBook);
  }, [deleteBook]);

  useEffect(() => {
    if (deleteBook.data) {
      dispatch({ type: Constant_DeleteBook.reset });
      GetTopBooks();
    }
  }, [deleteBook.data]);

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
              <Form className="d-flex m-2 p-2" onSubmit={GetTopBooks}>
                <div className=" input-group">
                  <Form.Control
                    type="search"
                    placeholder="введите часть названия книги"
                    className="w-50"
                    aria-label="Search"
                    required
                    value={searchText}
                    onChange={(event) => setSearchText(event.target.value)}
                  />
                  <Button variant="outline-success" type="submit">
                    искать
                  </Button>
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
                {/* <button
                  className="btn btn-md btn-outline-success"
                  onClick={() => {
                    dispatch({ type: CONST_TOP_BOOKS_RESET });
                  }}
                >
                  сброс
                </button> */}
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
          <div class="container px-4 py-5" id="custom-cards">
            <h2 class="pb-2 border-bottom">Custom cards</h2>


            <div>

          {topBooks.load ? (
            <div className="text-success"><ui.Loader1 color="text-success"/></div>
          ) : (
            <ui.Alert.Success size={0}>загрузка завершена</ui.Alert.Success>
          )}

          {topBooks.data ? (
            <div className="text-success">{topBooks.data["response"]}</div>
          ) : (
            <div className="text-danger"></div>
          )}

          {topBooks.error && <div className="text-danger">{topBooks.error}</div>}
          {topBooks.fail && <div className="text-warning">{topBooks.fail}</div>}
        </div>

            <div class="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5">
              {topBooks.data && topBooks.data["object_list"] ? (
                topBooks.data["object_list"].map((item) => (
                  <div class="col">
                    <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg custom_card">
                      <div class="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
                        
                        {deleteBook.load === true ? (
                          <ui.Loader1 color="text-danger"/>
                        ) : (
                          <button
                            onClick={() => removeBook(item.id)}
                            className="btn btn-sm btn-outline-danger text-end w-25"
                          >
                            удалить
                          </button>
                        )}

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
                <ui.Alert.Empty>данных нет!</ui.Alert.Empty>
              )}
            </div>
          </div>
        </div>
      </div>
    </base.Base1>
  );
}
