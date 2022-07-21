import React, { useState } from "react";
import Base, {Base1} from "../components/Base";
import {Paginator} from "../components/ui";
import {BookMainView} from "../components/books";
import axios from "axios";

export default function News() {
  const [array, setArray] = useState([]);
  const [page, setPage] = useState(3);
  const [limit, setLimit] = useState(20);
  const [pages, setPages] = useState(10); // [1]  -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  function AxiosRequest() {
    axios
      .get(`/backend_api/about/?page=${page}&limit=${limit}&filter=new`)
      .then((response) => {
        console.log(response);
        console.log(response.status);
        console.log(response.data);
        setArray(response.data["current_page"]);
        setPages(response.data["x-total-count"]);
      });
    // console.log('Hello react!');
  }

  function createPages(pages1) {
    const arr1 = [];
    for (var i = 1; i <= pages1 / limit; i++) {
      arr1.push(i);
    }
    return arr1;
  }
  return (
    <Base1>

      <body>
    
    
    
    <main>
    
      <section class="py-5 text-center container">
        <div class="row py-lg-5">
          <div class="col-lg-6 col-md-8 mx-auto">
            <h1 class="fw-light">Album example</h1>
            <p class="lead text-muted">Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.</p>
            <p>
              <a href="#" class="btn btn-primary my-2">Main call to action</a>
              <a href="#" class="btn btn-secondary my-2">Secondary action</a>
            </p>
          </div>
        </div>
      </section>
    
      <div class="album py-5 bg-light">
        <div class="container">
    
          <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

            {[1, 2, 3, 4].map((item, index) => 
              <BookMainView key={index} title={`Номер книги: №${item}`} description={"2"} lindView={"3"} lindEdit={"4"} time={"5 минут"}/>
            )}
          
          </div>
        </div>
      </div>
    
    </main>
    
    
      </body>
    </Base1>
  );

  return (
    <Base1>
      <main className="">
        <h1>Home Page</h1>

        <div className="card d-flex">
          <div>
            <input
              value={page}
              onChange={(event) => setPage(event.target.value)}
              type="number"
              min="1"
              max="10"
              className="form-control"
            />
            <input
              value={limit}
              onChange={(event) => setLimit(event.target.value)}
              type="number"
              min="1"
              max="20"
              className="form-control"
            />
          </div>
          <button
            onClick={AxiosRequest}
            className="btn btn-lg btn-outline-dark"
          >
            кнопка
          </button>
        </div>
        <div>
          <Paginator page={page} setPage={setPage} AxiosRequest={AxiosRequest} createPages={createPages} pages={pages} limit={limit}/>
        </div>
      </main>
    </Base1>
  );
}

