import { Link } from "react-router-dom";
import * as utils from "../components/utils";

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
      class="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">
              Modal title
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">...</div>
          <div class="modal-footer">
            <button
              onClick={() => okFunc(666)}
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Отмена
            </button>
            <button onClick={cancelFunc} type="button" class="btn btn-primary">
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
      <ul class="pagination pagination-lg">
        {page > 1 && (
          <li class="page-item">
            <button
              onClick={() => setPage(page - 1)}
              class="page-link"
              href="#"
              aria-label="Previous"
            >
              <span aria-hidden="true">&laquo;</span>
            </button>
          </li>
        )}

        {utils.CreateArrayFromInt(count, limit).map((item) => (
          <li class="page-item">
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
          <li class="page-item">
            <button
              onClick={() => setPage(page + 1)}
              class="page-link"
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
