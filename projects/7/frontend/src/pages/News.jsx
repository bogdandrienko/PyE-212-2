import React, { useEffect, useState } from "react";
import Base, {Base1} from "../components/Base";
import {Paginator} from "../components/ui";
import {BookMainView} from "../components/books";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";
import * as constants from '../components/Constants'
import * as ui from '../components/ui'


export default function News() {
  const dispatch = useDispatch();
  const newsBooks = useSelector((state)=>state.newsBooks);

  const [array, setArray] = useState([]);
  const [page, setPage] = useState(3);
  const [limit, setLimit] = useState(20);
  const [pages, setPages] = useState(10); // [1]  -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  function AxiosRequest() {
    dispatch({type: constants.CONST_NEWS_BOOKS_LOAD})
    axios
      .get(`/api/news`)
      .then((response) => {
        const result = response.data;
        //console.log(response);
        //console.log(response.status);
        //console.log(response.data);
        dispatch({type: constants.CONST_NEWS_BOOKS_DATA, payload: result })
      });
    // console.log('Hello react!');
  }

  useEffect(()=> {
    console.log(newsBooks)
  }, [newsBooks])

  function createPages(pages1) {
    const arr1 = [];
    for (var i = 1; i <= pages1 / limit; i++) {
      arr1.push(i);
    }
    return arr1;
  }

  function Ok(value) {
    console.log(`Изменения сохранены! ${value}`)
  }

  function Cancel() {
    console.log("Изменения сохранены!")
  }


  return (
    <Base1>
    <main>
    
      <section className="py-5 text-center container">
        <div className="row py-lg-5">
          <div className="col-lg-6 col-md-8 mx-auto">
            <h1 className="fw-light">Album example</h1>
            <p className="lead text-muted">Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.</p>
            <p>
              <a href="#" className="btn btn-primary my-2">Main call to action</a>
              <a href="#" className="btn btn-secondary my-2">Secondary action</a>
              <button onClick={AxiosRequest}>click</button>
            </p>
          </div>
        </div>
      </section>

      {newsBooks.load &&
      <div className="text-center d-flex justify-content-center">
        <ui.Loader1 color="text-danger"/>
      </div>}

      <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
        Launch static backdrop modal
      </button>

      <div className="text-center d-flex justify-content-center">
        <ui.Modal2 okFunc={Ok} cancelFunc={Cancel} >ребёнок</ui.Modal2>
      </div>

      <div className="album py-5 bg-light">
        <div className="container">
    
          <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
            {newsBooks && newsBooks.data && newsBooks.data.map((item, index) => 
              <BookMainView key={index} title={item.title} 
              description={item.description} lindView={"3"} lindEdit={"4"} image={item.image} time={"5 минут"}/>
            )}
          </div>
        </div>
      </div>
    </main>
    </Base1>
  );
}

