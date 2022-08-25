import { Link } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

export function Navbar1() {
  return (
    <header className="p-3 bg-dark text-white">
      <div className="container">
        <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <a
            href="https://www.livelib.ru/genre/%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/best/"
            className="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none lead fw-bold"
          >
            Эталон
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

          <div className="text-end input-group">
            <button type="button" className="btn btn-outline-light">
              <Link to="/login" className="text-decoration-none">
                Зарегистрироваться
              </Link>
            </button>

            <button type="button" className="btn btn-warning">
              Sign-up
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}

export function Navbar2() {
  return <div>Я 2 верхняя часть страницы</div>;
}

export const Navbar3 = () => {
  return (
    <header>
      <div className="collapse bg-dark" id="navbarHeader">
        <div className="container">
          <div className="row">
            <div className="col-sm-8 col-md-7 py-4">
              <h4 className="text-white">About</h4>
              <p className="text-muted">
                Add some information about the album below, the author, or any
                other background context. Make it a few sentences long so folks
                can pick up some informative tidbits. Then, link them off to
                some social networking sites or contact information.
              </p>
            </div>
            <div className="col-sm-4 offset-md-1 py-4">
              <h4 className="text-white">Contact</h4>
              <ul className="list-unstyled">
                <li>
                  <a href="#" className="text-white">
                    Follow on Twitter
                  </a>
                </li>
                <li>
                  <a href="#" className="text-white">
                    Like on Facebook
                  </a>
                </li>
                <li>
                  <a href="#" className="text-white">
                    Email me
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div className="navbar navbar-dark bg-dark shadow-sm">
        <div className="container">
          <a href="#" className="navbar-brand d-flex align-items-center">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              aria-hidden="true"
              className="me-2"
              viewBox="0 0 24 24"
            >
              <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z" />
              <circle cx="12" cy="13" r="4" />
            </svg>
            <strong>Album</strong>
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarHeader"
            aria-controls="navbarHeader"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
    </header>
  );
};

export const Navbar4 = () => {
  return (
    <Navbar bg="light" expand="md">
      <Container fluid>
        <Navbar.Brand href="/">Главная</Navbar.Brand>
        <Navbar.Brand href="https://www.livelib.ru/genre/%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/best/" className="lead fw-bold">Эталон</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: "100px" }}
            navbarScroll
          >
            <NavDropdown title="Что почитать" id="navbarScrollingDropdown">
              <Link to="/news" className="text-decoration-none text-dark m-1 p-1">Новинки</Link>
              
              
              <NavDropdown.Item href="#" className="text-decoration-none">
                <Link to="/top" className="text-decoration-none text-dark m-1 p-1 w-100">
                  Лучшие
                </Link>
              </NavDropdown.Item>
              <NavDropdown.Item href="#" className="text-decoration-none">
                <Link to="/books" className="text-decoration-none text-dark m-1 p-1 w-100">
                  Все книги
                </Link>
              </NavDropdown.Item>
              
              <NavDropdown.Item href="#action4">Рекомендации</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action5">Жанры</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="Лента" id="navbarScrollingDropdown">
              <NavDropdown.Item href="#action3">Рецензии</NavDropdown.Item>
              <NavDropdown.Item href="#action4">Цитаты</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="Авторы" id="navbarScrollingDropdown">
              <NavDropdown.Item href="#action3">Список авторов</NavDropdown.Item>
            </NavDropdown>
            <Nav.Link href="#" disabled>
              Карта развития платформы
            </Nav.Link>
            <Link to={"/auth"} className={"btn btn-sm btn-outline-primary"}>Авторизация</Link>
          </Nav>
          <Form className="d-flex">
            <div className=" input-group">
            <Form.Control
              type="search"
              placeholder="что ищем"
              className="w-25"
              aria-label="Search"
            />
            <Button variant="outline-success">Поиск</Button>
            </div>
          </Form>
          <div className="input-group w-25 p-2">
            <Link to={"/register"} className={"btn btn-sm btn-outline-warning"}>Регистрация</Link>
            <Link to={"/login"} className={"btn btn-sm btn-outline-primary"}>Войти</Link>
          </div>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};
