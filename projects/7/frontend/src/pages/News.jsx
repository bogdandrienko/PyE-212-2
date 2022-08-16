import React, { useEffect, useState, forwardRef, createRef, useRef  } from "react";
import Base, {Base1} from "../components/Base";
import {Paginator} from "../components/ui";
import {BookMainView} from "../components/books";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";
import * as constants from '../components/Constants'
import * as ui from '../components/ui'
import * as utils from '../components/utils'


export default function News() {
  const dispatch = useDispatch();
  const newsBooks = useSelector((state)=>state.newsBooks);

  const [viewType, setViewType] = useState(1);
  const [page, setPage] = useState(1);
  const [limit, setLimit] = useState(3);
  const [count, setCount] = useState(1);

  
  const [books, setBooks] = useState([]);

  function AxiosRequest() {
    if (newsBooks.load !== true){
      dispatch({type: constants.CONST_NEWS_BOOKS_LOAD})
      axios
        .get(`/api/news`, {
          params: {
            limit: limit,
            page: page,
          },
        })
        .then((response) => {
          const result = response.data.object_list;
          setCount(response.count);
          if (newsBooks.data){
            setBooks([...books.data, ...result])
            dispatch({type: constants.CONST_NEWS_BOOKS_DATA, payload: [...newsBooks.data, ...result] })
          } else {
            setBooks([...result])
            dispatch({type: constants.CONST_NEWS_BOOKS_DATA, payload: [...result] })
          }
        });
    }
  }

  useEffect(()=> {
    console.log(newsBooks)
  }, [newsBooks])

  useEffect(()=> {
    AxiosRequest();
  }, [])

  useEffect(()=> {
    AxiosRequest();
  }, [page])

  useEffect(()=> {
    console.log(`CURRENT PAGE: ${page}`)
  }, [page])





  const lastItem = createRef();
  const observerLoader = useRef();
  const actionInSight = (entries) => {
    if (entries[0].isIntersecting) {
      console.log("ВАС ЗАМЕТИЛИ")
      setPage(page + 1)
    }
  };
  //регистрируем на последний элемент наблюдателя, когда последний элемент меняется
  useEffect(() => {
    if (observerLoader.current) {
      observerLoader.current.disconnect();
    }
    observerLoader.current = new IntersectionObserver(actionInSight);
    if (lastItem.current) {
      observerLoader.current.observe(lastItem.current);
    }
  }, [lastItem]);







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
            </p>
          </div>
        </div>
      </section>

    <ui.Paginator2 page={page}
    setPage={setPage}
    count={count}
    limit={limit}
    />

<nav aria-label="Page navigation example">
  <ul className="pagination pagination-lg">
    {page > 1 &&
    <li className="page-item">
      <button onClick={()=>setPage(page-1)} className="page-link" href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </button>
    </li>}

    {utils.CreateArrayFromInt(count, limit).map((item) => (
      <li className="page-item"><button type="button" onClick={()=>setPage(item)} class={page===item ?"page-link fw-bold lead active" :"page-link"}>{item}</button></li>
    ))}

{page < utils.CreateArrayFromInt(count, limit).length &&
    <li className="page-item">
      <button onClick={()=>setPage(page+1)} className="page-link" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </button>
    </li>
}
  </ul>
</nav>

      <div className="input-group">
        <button onClick={()=> setViewType(1)} className="btn btn-lg btn-outline-primary">первый вид</button>
        <button onClick={()=> setViewType(2)} className="btn btn-lg btn-outline-warning">второй вид</button>
        <button onClick={()=> setViewType(3)} className="btn btn-lg btn-outline-danger">третий вид</button>
      </div>

      {newsBooks.load &&
      <div className="text-center d-flex justify-content-center">
        <ui.Loader1 color="text-danger"/>
      </div>}


      <BookMainView newsBooks={books} viewType={viewType}></BookMainView>

      <ui.Paginator2 page={page}
    setPage={setPage}
    count={count}
    limit={limit}
    />
    </main>

    <div className="bg-danger bg" ref={lastItem}  id="target">111111</div>
    </Base1>
  );
}

