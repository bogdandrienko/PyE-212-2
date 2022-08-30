import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import * as base from "../components/Base";
import * as utils from "../components/utils";
import * as ui from "../components/ui";
import * as constants from "../components/Constants";
import { Link } from "react-router-dom";

export function Books() {
  const dispatch = useDispatch();
  const books = useSelector((state) => state.books);

  const [paginateObj, setPaginateObj] = useState({
    page: 1,
    limit: 3,
    count: 1,
  });
  
  useEffect(() => {
    console.log(books);
  }, [books]);

  useEffect(() => {
    console.log(paginateObj);
  }, [paginateObj]);

  useEffect(() => {
    getBooks();
  }, [paginateObj.page]);

  function updateData() {
    dispatch({ type: constants.C_Books.reset });
  }

  async function getBooks() {
    if(books.load !== true){
      dispatch(
        utils.ConstructorActionRedux(
          `/api/books/?page=${paginateObj.page}&limit=${paginateObj.limit}`,
          "GET",
          {},
          5000,
          constants.C_Books
        )
      )
    }
  }

  return (
    <base.Base1>
      <div>
        <div className="container card p-0">
          <div className="card-header lead">
            Список всех книг
            <button
              onClick={updateData}
              className="btn btn-sm btn-outline-secondary m-1 p-1"
            >
              <i className="fa-solid fa-rotate"></i>
            </button>
          </div>

          {books.load === true && (
            <div className="card-header">
              <ui.Loader1 color="text-success" />
            </div>
          )}
            <div className="d-flex justify-content-center text-center">
              <ui.Paginator3
                topBooks={books}
                paginateObj={paginateObj}
                setPaginateObj={setPaginateObj}
              />
            </div>
          <div className="card-body">
            <div className="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5">
              {books.data && books.data["object_list"] ? (
                books.data["object_list"].map((item) => (
                  <div key={item.id} className="col">
                    <Link to={`/books/${item.id}`} className="text-decoration-none text-dark">
                        <div className="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg custom_card">
                            <div className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1">
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
                                    {item.category2.map((category) => (<button key={category.id} className="btn btn-sm btn-outline-secondary">{category.title}</button>))}
                                </li>
                                <li className="d-flex align-items-center me-3">
                                    <svg
                                    className="bi me-2"
                                    width="1em"
                                    height="1em"
                                    ></svg>
                                    <small>{utils.SliceDescription(item.description)}</small>
                                </li>
                                <li className="d-flex align-items-center">
                                    <svg
                                    className="bi me-2"
                                    width="1em"
                                    height="1em"
                                    ></svg>
                                    <small className="btn btn-sm btn-outline-secondary">{item.upload_author1.username}</small>
                                </li>
                                </ul>
                                <div className="">
                                    <Link to={`/books/${item.id}`} className="text-decoration-none text-light btn btn-md btn-primary w-100 m-1 p-1">подробнее</Link>
                                </div>
                            </div>
                        </div>
                    </Link>
                  </div>
                ))
              ) : (
                <ui.Alert.Empty>...данных нет..</ui.Alert.Empty>
              )}
            </div>
            <div className="d-flex justify-content-center text-center">
              <ui.Paginator3
                topBooks={books}
                paginateObj={paginateObj}
                setPaginateObj={setPaginateObj}
              />
            </div>
          </div>
          <div className="card-footer">
            {books.fail === true && (
              <ui.Alert.Warning>{books.fail}</ui.Alert.Warning>
            )}
            {books.error === true && (
              <ui.Alert.Danger>{books.error}</ui.Alert.Danger>
            )}
          </div>
        </div>
      </div>
    </base.Base1>
  );
}
