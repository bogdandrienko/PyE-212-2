import { Link } from "react-router-dom";
import * as utils from "../components/utils";
import { useEffect, useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

export function Paginator({
  page,
  setPage,
  AxiosRequest,
  createPages,
  pages,
  limit,
}) {
  // логика
  return (
    <div className="card">
      <nav aria-label="Page navigation example">
        <ul className="pagination">
          {page !== 1 && (
            <li className="page-item">
              <button
                onClick={() => {
                  setPage(page - 1);
                  AxiosRequest();
                }}
                className="page-link"
              >
                <span aria-hidden="true">&laquo;</span>
              </button>
            </li>
          )}
          {createPages(pages).map((cur_page) => (
            <li className="page-item">
              <button
                onClick={() => {
                  setPage(cur_page);
                  AxiosRequest();
                }}
                key={cur_page}
                className={
                  cur_page === page
                    ? `page-link fw-bold text-success bg-secondary`
                    : `page-link`
                }
              >
                {cur_page}
              </button>
            </li>
          ))}
          {pages.length / limit !== page && (
            <li className="page-item">
              <button
                onClick={() => {
                  setPage(page + 1);
                  AxiosRequest();
                }}
                className="page-link"
              >
                <span aria-hidden="true">&raquo;</span>
              </button>
            </li>
          )}
        </ul>
      </nav>
    </div>
  );
}

export function Loader1({ color = "text-black" }) {
  return (
    <div className={`lds-spinner ${color}`}>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  );
}

export function Modal1({ okFunc, cancelFunc }) {
  return (
    <div
      className="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title" id="exampleModalLabel">
              Modal title
            </h5>
            <button
              type="button"
              className="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div className="modal-body">...</div>
          <div className="modal-footer">
            <button
              onClick={() => okFunc(666)}
              type="button"
              className="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Отмена
            </button>
            <button
              onClick={cancelFunc}
              type="button"
              className="btn btn-primary"
            >
              Принять
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export function Modal2({ children, okFunc, cancelFunc }) {
  return (
    <div className="modal__wrap">
      <div className="modal visible">{children}</div>
    </div>
  );
}

export function Paginator2({ page, setPage, count, limit }) {
  return (
    <nav aria-label="Page navigation example">
      <ul className="pagination pagination-lg">
        {page > 1 && (
          <li className="page-item">
            <button
              onClick={() => setPage(page - 1)}
              className="page-link"
              href="#"
              aria-label="Previous"
            >
              <span aria-hidden="true">&laquo;</span>
            </button>
          </li>
        )}

        {utils.CreateArrayFromInt(count, limit).map((item) => (
          <li className="page-item">
            <button
              type="button"
              onClick={() => setPage(item)}
              class={
                page === item ? "page-link fw-bold lead active" : "page-link"
              }
            >
              {item}
            </button>
          </li>
        ))}

        {page < utils.CreateArrayFromInt(count, limit).length && (
          <li className="page-item">
            <button
              onClick={() => setPage(page + 1)}
              className="page-link"
              aria-label="Next"
            >
              <span aria-hidden="true">&raquo;</span>
            </button>
          </li>
        )}
      </ul>
    </nav>
  );
}

export class Alert {
  static Success({ children, size }) {
    return (
      <div className={`alert alert-success m-${size} p-${size}`} role="alert">
        {children}
      </div>
    );
  }
  static Danger({ children }) {
    return (
      <div className="alert alert-danger" role="alert">
        {children}
      </div>
    );
  }
  static Empty({ children }) {
    return (
      <div className="alert alert-secondary" role="alert">
        {children}
      </div>
    );
  }
}

{
  /* <div className="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
<div className="alert alert-secondary" role="alert">
  A simple secondary alert—check it out!
</div>
<div className="alert alert-success" role="alert">
  A simple success alert—check it out!
</div>
<div className="alert alert-danger" role="alert">
  A simple danger alert—check it out!
</div>
<div className="alert alert-warning" role="alert">
  A simple warning alert—check it out!
</div>
<div className="alert alert-info" role="alert">
  A simple info alert—check it out!
</div>
<div className="alert alert-light" role="alert">
  A simple light alert—check it out!
</div>
<div className="alert alert-dark" role="alert">
  A simple dark alert—check it out!
</div> */
}

export function Select1({
  children,
  onSubmitFunc,
  defaultValue,
  selects = { value_1: "Первый", value_2: "Второй" },
}) {
  const [selectedValue, setSelectedValue] = useState("");

  const key = Math.random();

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        onSubmitFunc(selectedValue);
      }}
    >
      <div className="my-2">
        <div className="input-group w-100">
          <label htmlFor={`select ${key}`} className="form-label">
            {children}
          </label>
          <select
            className="form-select"
            id={`select ${key}`}
            required
            onChange={(event) => setSelectedValue(event.target.value)}
          >
            <option value="" className={"w-50"}>
              {defaultValue}
            </option>

            {Object.keys(selects).map((key) => (
              <option key={key} value={`${key}`} className={"w-50"}>
                {selects[key]}
              </option>
            ))}
          </select>
          <button type="submit" className="btn btn-outline-secondary">
            подтвердить
          </button>
        </div>
        <div className="invalid-feedback">Please select a valid country.</div>
      </div>
    </form>
  );
}

export function Search1({ children, onSubmitFunc }) {
  const [searchedText, setSearchedText] = useState("");

  return (
    <Form
      className="d-flex m-2 p-2"
      onSubmit={() => onSubmitFunc(searchedText)}
    >
      <div className=" input-group">
        <Form.Control
          type="search"
          placeholder={children}
          className="w-50"
          aria-label="Search"
          required
          value={searchedText}
          onChange={(event) => setSearchedText(event.target.value)}
        />
        <Button variant="outline-success" type="submit">
          искать
        </Button>
      </div>
    </Form>
  );
}

export function Paginator3({ topBooks, paginateObj, setPaginateObj }) {
  return (
    <nav aria-label="Page navigation example">
      <ul className="pagination pagination-lg">
        {paginateObj.page > 1 && (
          <li className="page-item">
            <button
              onClick={() =>
                setPaginateObj({
                  page: paginateObj.page - 1,
                  limit: paginateObj.limit,
                })
              }
              className="page-link"
              aria-label="Previous"
            >
              <span aria-hidden="true">&laquo;</span>
            </button>
          </li>
        )}

        {topBooks.data &&
          topBooks.data["count"] &&
          utils
            .CreateArrayFromInt(topBooks.data["count"], paginateObj.limit)
            .map((item) => (
              <li key={item} className="page-item">
                <button
                  onClick={() =>
                    setPaginateObj({
                      page: item,
                      limit: paginateObj.limit,
                    })
                  }
                  className={
                    paginateObj.page === item ? "page-link active" : "page-link"
                  }
                >
                  {item}
                </button>
              </li>
            ))}
        {topBooks.data &&
          topBooks.data["count"] &&
          paginateObj.page <
          utils.CreateArrayFromInt(topBooks.data["count"], paginateObj.limit).length && (
          <li className="page-item">
            <button
              onClick={() =>
                setPaginateObj({
                  page: paginateObj.page + 1,
                  limit: paginateObj.limit,
                })
              }
              className="page-link"
              aria-label="Next"
            >
              <span aria-hidden="true">&raquo;</span>
            </button>
          </li>
        )}
      </ul>
    </nav>
  );
}
