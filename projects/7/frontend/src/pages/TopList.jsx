import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import * as base from "../components/Base";
import * as utils from "../components/utils";
import * as ui from "../components/ui";
import * as constants from "../components/Constants";

export function TopList() {
  const dispatch = useDispatch();

  const topBooks = useSelector((state) => state.topBooks);
  const deleteBook = useSelector((state) => state.deleteBook);

  const categories = useSelector((state) => state.categories);

  const [paginateObj, setPaginateObj] = useState({
    page: 1,
    limit: 30,
    count: 1,
  });

  const [searchText, setSearchText] = useState("");
  const [categoryText, setCategoryText] = useState("");
  const [filterText, setFilterText] = useState("");

  async function removeBook(id) {
    dispatch(
      utils.ConstructorActionRedux(
        `/api/book/${id}/`,
        "DELETE",
        {},
        3000,
        constants.C_DeleteBook
      )
    );
  }

  async function GetTopBooks(options) {
    //search=searchText, category=categoryText, filter=filterText
    dispatch(
      utils.ConstructorActionRedux(
        `/api/top/?page=${paginateObj.page}&limit=${paginateObj.limit}&search=${options.search}&category=${options.category}&filter=${options.filter}`,
        "GET",
        {},
        5000,
        constants.C_TopBooks
      )
    );
  }

  useEffect(() => {
    if (!topBooks.data && topBooks.load !== false) {
      // GetTopBooks({search: searchText, category: categoryText, filter: filterText});
    }
  }, []);

  useEffect(() => {
    GetTopBooks({search: searchText, category: categoryText, filter: filterText});
  }, [paginateObj.page]);

  useEffect(() => {
    // console.log("topBooks", topBooks);
  }, [topBooks]);

  useEffect(() => {
    if (deleteBook.data) {
      dispatch({ type: constants.C_DeleteBook.reset });
      GetTopBooks({search: searchText, category: categoryText, filter: filterText});
    }
  }, [deleteBook.data]);

  function searchFunc(value) {
    setSearchText(value)
    GetTopBooks({search: value, category: categoryText, filter: filterText});
  }

  function categoryFunc(value) {
    setCategoryText(value)
    GetTopBooks({search: searchText, category: value, filter: filterText});
  }

  function filterFunc(value) {
    setFilterText(value)
    GetTopBooks({search: searchText, category: categoryText, filter: value});
  }

  useEffect(() => {
    console.log("categories", categories);
  }, [categories]);

  useEffect(() => {

    dispatch(
      utils.ConstructorActionRedux(
        `/api/categories`,
        "GET",
        {},
        5000,
        constants.C_Categories
      )
    );

  }, []);



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
              <ui.Search1 onSubmitFunc={searchFunc}>
                введите текст для поиска тут...
              </ui.Search1>
            </div>

            <div className="d-flex">
              <ui.Select1
                defaultValue={"нажмите сюда чтобы увидеть список лет..."}
                selects={{
                  "меньше минуты назад": "меньше минуты назад",
                  "более минуты назад": "более минуты назад",
                }}
                onSubmitFunc={filterFunc}
              >
                Выберите год
              </ui.Select1>

                {categories && categories.data && categories.data["object_list"] &&
                (
                  <ui.Select1
                  defaultValue={"нажмите сюда чтобы увидеть список категорий..."}

                  selects={Object.assign({}, ...categories.data["object_list"].map((x) => ({[x.title]: x.title})))}

                  // selects={{
                  //   new: "Свежак",
                  //   classic: "Классика для ценителей",
                  //   programming: "Программирование для гиков!",
                  // }}
                  onSubmitFunc={categoryFunc}
                >
                  Выберите категорию
                </ui.Select1>
                )
                }
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
