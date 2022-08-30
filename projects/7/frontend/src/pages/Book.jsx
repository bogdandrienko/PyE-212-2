import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import * as base from "../components/Base";
import * as utils from "../components/utils";
import * as ui from "../components/ui";
import * as constants from "../components/Constants";
import { Link, useNavigate, useParams } from "react-router-dom";

export function Book() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const id = useParams().id;
  const book = useSelector((state) => state.book);

  useEffect(() => {
    console.log(book);
  }, [book]);

  useEffect(() => {
    if (!book.data && book.load !== true) {
      getBook();
    }
  }, [book.data]);

  async function getBook() {
    dispatch(
      utils.ConstructorActionRedux(
        `/api/books/${id}/`,
        "GET",
        {},
        5000,
        constants.C_Book
      )
    );
  }

  return (
    <base.Base1>
      <div>
        <div className="container card p-0">
          <div className="card-header lead">
            <div className="d-flex justify-content-between">
              <button
                onClick={() => navigate(`/books`)}
                className="btn btn-lg btn-outline-primary w-50"
              >
                назад
              </button>
              <div className="w-50 fw-bold display-6">Детали о книге</div>
            </div>
          </div>

          {book.load === true && (
            <div className="card-header">
              <ui.Loader1 color="text-success" />
            </div>
          )}

          <div className="card-body">
            <div className="row row-cols-1 row-cols-lg-2 py-5 text-center">
              {book.data && book.data["object"] ? (
                <div className="col text-center w-75">
                  <div className="card text-center card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg">
                    <div className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
                      <img
                        src={utils.GetStaticFile(book.data["object"]["image"])}
                        alt="img"
                        className="img img-fluid w-50"
                      />

                      {/* {deleteBook.load === true ? (
                          <ui.Loader1 color="text-danger" />
                        ) : (
                          <button
                            onClick={() => removeBook(item.id)}
                            className="btn btn-sm btn-outline-danger text-end w-25"
                          >
                            удалить
                          </button>
                        )} */}

                      <h2 className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold">
                        {book.data["object"].title}
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
                          {book.data["object"].category2.map((category) => (
                            <button key={category.id} className="btn btn-sm btn-outline-secondary">
                              {category.title}
                            </button>
                          ))}
                        </li>
                        <li className="d-flex align-items-center me-3">
                          <svg
                            className="bi me-2"
                            width="1em"
                            height="1em"
                          ></svg>
                          <small>{book.data["object"].description}</small>
                        </li>
                        <li className="d-flex align-items-center">
                          <svg
                            className="bi me-2"
                            width="1em"
                            height="1em"
                          ></svg>
                          <small className="btn btn-sm btn-outline-secondary">
                            {book.data["object"].upload_author1.username}
                          </small>
                        </li>
                      </ul>
                      <div className="">
                        <a
                          rel="noreferrer"
                          target="_blank"
                          href={utils.GetStaticFile(book.data["object"]["instructions"])}
                          className="text-decoration-none text-light btn btn-md btn-primary w-100 m-1 p-1"
                        >
                          скачать
                        </a>
                      </div>
                      <div className="d-flex justify-content-between">
                        <small className="w-50">
                          {utils.FormatDatetimeString(
                            book.data["object"].update_datetime_field,
                            true
                          )}
                        </small>
                        <small className="w-50">
                          <i className="fa-solid fa-book m-1 p-1"></i>
                          {book.data["object"].time_to_read} мин
                        </small>
                      </div>
                    </div>
                  </div>
                </div>
              ) : (
                <ui.Alert.Empty>...данных нет..</ui.Alert.Empty>
              )}
            </div>
          </div>
          <div className="card-footer">
            {book.fail === true && (
              <ui.Alert.Warning>{book.fail}</ui.Alert.Warning>
            )}
            {book.error === true && (
              <ui.Alert.Danger>{book.error}</ui.Alert.Danger>
            )}
          </div>
        </div>
      </div>
    </base.Base1>
  );
}
