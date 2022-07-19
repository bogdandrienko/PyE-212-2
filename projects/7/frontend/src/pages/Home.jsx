import React, { useState } from "react";
import Base from "../components/Base";
import {Paginator} from "../components/ui";
import axios from "axios";

function Home() {
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
    <Base>
      <main className="custom_main_1">
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
    </Base>
  );
}

export default Home;
