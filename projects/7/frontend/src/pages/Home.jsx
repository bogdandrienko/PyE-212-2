import React, { useState } from "react";
import Base, { Base1 } from "../components/Base";
import { Paginator } from "../components/ui";
import { BookMainView } from "../components/books";
import axios from "axios";
import { Link } from "react-router-dom";

function Home() {
  return (
    <Base1>
      <div class="px-2 py-2 my-2 text-center">
        <img
          class="d-block mx-auto mb-4 img-fluid img-responsive img-thumbnail w-50"
          src="/static/home_hero.png"
          alt="image"
        />
        <h1 class="display-5 fw-bold">Книжный сайт</h1>
        <div class="col-lg-6 mx-auto">
          <p class="lead mb-4">
            Совсем перестали читать! Ну ка!
          </p>
          <div class="d-grid gap-2 d-sm-flex justify-content-sm-center input-group">
            <Link
              to="/news"
              type="button"
              class="btn btn-primary btn-md px-4 gap-3"
            >
              Перейти к чтению
            </Link>
            <a
              href="https://github.com/bogdandrienko"
              class="btn btn-outline-secondary btn-md px-4"
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
