import { Link } from "react-router-dom";





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
        <ul class="pagination">
          {page !== 1 && (
            <li class="page-item">
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
            <li class="page-item">
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
            <li class="page-item">
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
