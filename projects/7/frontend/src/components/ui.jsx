import { Link } from "react-router-dom";

export function Navbar() {
  return (
    <header className="p-3 bg-dark text-white">
      <div className="container">
        <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <a
            href="/"
            className="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none"
          >
            <svg
              className="bi me-2"
              width="40"
              height="32"
              role="img"
              aria-label="Bootstrap"
            ></svg>
          </a>

          <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
            <li>
              <a href="#" className="nav-link px-2 text-secondary">
                Home
              </a>
            </li>
            <li>
              <a href="#" className="nav-link px-2 text-white">
                Features
              </a>
            </li>
            <li>
              <a href="#" className="nav-link px-2 text-white">
                Pricing
              </a>
            </li>
            <li>
              <a href="#" className="nav-link px-2 text-white">
                FAQs
              </a>
            </li>
            <li>
              <a href="#" className="nav-link px-2 text-white">
                About
              </a>
            </li>
          </ul>

          <form className="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3">
            <input
              type="search"
              className="form-control form-control-dark"
              placeholder="Search..."
              aria-label="Search"
            />
          </form>

          <div className="text-end">
            <Link to="/login" className="text-decoration-none">
              <button type="button" className="btn btn-outline-light me-2">
                Зарегистрироваться
              </button>
            </Link>

            <button type="button" className="btn btn-warning">
              Sign-up
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}

export function Footer() {
  return (
    <footer className="footer mt-auto py-3 bg-light">
      <div className="container">
        <span className="text-muted">Place sticky footer content here.</span>
      </div>
    </footer>
  );
}

export function Paginator({
  page,
  setPage,
  AxiosRequest,
  createPages,
  pages,
  limit,
}) {
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
