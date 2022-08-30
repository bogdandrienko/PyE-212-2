import React, { useState } from "react";
import Base, { Base1 } from "../components/Base";
import { BookView } from "../components/books";
import axios from "axios";
import { Link } from "react-router-dom";
import * as actions from "../components/actions";


function Home() {
  return (
    <Base1>
      <div className="px-2 py-2 my-2 text-center">
        <img
          className="d-block mx-auto mb-4 img-fluid img-responsive img-thumbnail w-50"
          src="/static/home_hero.png"
          alt="image"
        />
        <h1 className="display-5 fw-bold" onClick={()=> actions.Logout()} >Книжный сайт</h1>
        <div className="col-lg-6 mx-auto">
          <p className="lead mb-4">
            Совсем перестали читать! Ну ка!
          </p>
          <div className="d-grid gap-2 d-sm-flex justify-content-sm-center input-group">
            <Link
              to="/news"
              type="button"
              className="btn btn-primary btn-md px-4 gap-3"
            >
              Перейти к чтению
            </Link>
            <a
              href="https://github.com/bogdandrienko"
              className="btn btn-outline-secondary btn-md px-4"
            >
              Узнать об авторе побольше
            </a>
          </div>
        </div>
      </div>
    </Base1>
  );
}

export default Home;
