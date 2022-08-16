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

  const [paginateObj, setPaginateObj] = useState({
    page: 1,
    limit: 30,
    count: 1,
  });

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
        `/api/top/?page=${paginateObj.page}&limit=${paginateObj.limit}&search=${searchText}`,
        "GET",
        {},
        5000,
        Constant_TopBooks
      )
    );
  }

  useEffect(() => {
    if (!topBooks.data && topBooks.load !== false) {
      // GetTopBooks();
    }
  }, []);

  useEffect(() => {
    console.log(paginateObj);
    GetTopBooks();
  }, [paginateObj.page]);

  useEffect(() => {
    console.log("topBooks", topBooks);
  }, [topBooks]);

  useEffect(() => {
    if (deleteBook.data) {
      dispatch({ type: Constant_DeleteBook.reset });
      GetTopBooks();
    }
  }, [deleteBook.data]);

  function filter(value) {
    // GetTopBooks();
    // console.log("ФИЛЬТРАЦИЯ ДАННЫХ!", value);
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
              <ui.Search1 onSubmitFunc={filter}>
                введите текст для поиска тут...
              </ui.Search1>
            </div>

            <div className="d-flex">
              <ui.Select1
                defaultValue={"нажмите сюда чтобы увидеть список лет..."}
                selects={{
                  2010: "После 2010 года",
                  2020: "После 2020 года",
                  2022: "После 2022 года",
                }}
                onSubmitFunc={filter}
              >
                Выберите год
              </ui.Select1>

              <ui.Select1
                defaultValue={"нажмите сюда чтобы увидеть список категорий..."}
                selects={{
                  new: "Свежак",
                  classic: "Классика для ценителей",
                  programming: "Программирование для гиков!",
                }}
                onSubmitFunc={filter}
              >
                Выберите категорию
              </ui.Select1>
            </div>
          </div>
          <div className="card-footer">footer</div>
        </div>

        <div>
          <div className="container px-4 py-5" id="custom-cards">
            <div>

              <div className="d-flex justify-content-center text-center">
                <ui.Paginator3
                  topBooks={topBooks}
                  paginateObj={paginateObj}
                  setPaginateObj={setPaginateObj}
                />
              </div>

              {topBooks.data ? (
                <div className="text-success">{topBooks.data["response"]}</div>
              ) : (
                <div className="text-danger"></div>
              )}

              {topBooks.error && (
                <div className="text-danger">{topBooks.error}</div>
              )}
              {topBooks.fail && (
                <div className="text-warning">{topBooks.fail}</div>
              )}
            </div>

            {topBooks.load ? (
              <div className="text-success">
                <ui.Loader1 color="text-success" />
              </div>
            ) : (
              <div></div>
              // <ui.Alert.Success size={0}>загрузка завершена</ui.Alert.Success>
            )}

            <div className="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5">
              {topBooks.data && topBooks.data["object_list"] ? (
                topBooks.data["object_list"].map((item, index) => (
                  <div key={index} className="col">
                    <div className="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg custom_card">
                      <div className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
                        {deleteBook.load === true ? (
                          <ui.Loader1 color="text-danger" />
                        ) : (
                          <button
                            onClick={() => removeBook(item.id)}
                            className="btn btn-sm btn-outline-danger text-end w-25"
                          >
                            удалить
                          </button>
                        )}

                        <h2 className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">
                          {item.title}
                        </h2>
                        <ul className="d-flex list-unstyled mt-auto">
                          <li className="me-auto">
                            <img
                              src="https://github.com/twbs.png"
                              alt="Bootstrap"
                              width="32"
                              height="32"
                              className="rounded-circle border border-white"
                            ></img>
                          </li>
                          <li className="d-flex align-items-center me-3">
                            <svg
                              className="bi me-2"
                              width="1em"
                              height="1em"
                            ></svg>
                            <small>California</small>
                          </li>
                          <li className="d-flex align-items-center">
                            <svg
                              className="bi me-2"
                              width="1em"
                              height="1em"
                            ></svg>
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
            <div className="d-flex justify-content-center text-center">
              <ui.Paginator3
                topBooks={topBooks}
                paginateObj={paginateObj}
                setPaginateObj={setPaginateObj}
              />
            </div>
          </div>
        </div>
      </div>
    </base.Base1>
  );
}
