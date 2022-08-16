import React from "react";
import * as utils from './utils'


export function BookMainView({ newsBooks, viewType }) {
  return (
    <div className="album py-5 bg-light">
      <div className="container">
        {viewType === 1 ? (
          <div className="row mb-2">
            {newsBooks &&
              newsBooks.data &&
              newsBooks.data.map((item, index) => (
                <BookView2
                  view={viewType}
                  key={index}
                  title={item.title}
                  description={item.description}
                  instructions={item.instructions}
                  lindView={"3"}
                  lindEdit={"4"}
                  image={item.image}
                  time={"5 минут"}
                />
              ))}
          </div>
        ) : (
          <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
            {newsBooks &&
              newsBooks.data &&
              newsBooks.data.map((item, index) => (
                <BookView
                  view={viewType}
                  key={index}
                  title={item.title}
                  description={item.description}
                  instructions={item.instructions}
                  lindView={"3"}
                  lindEdit={"4"}
                  image={item.image}
                  time={"5 минут"}
                />
              ))}
          </div>
        )}
      </div>
    </div>
  );
}

export function BookView({
  view,
  title,
  description,
  lindView,
  lindEdit,
  image,
  instructions,
  time = "0 минут",
}) {
  return (
    <div
      className={
        view === 3
          ? "col col-12 col-sm-12 col-md-12 col-lg-12"
          : view === 2
          ? "col-12 col-sm-12 col-md-4 col-lg-4"
          : "col-12 col-sm-12 col-md-6 col-lg-6"
      }
    >
      <div className={view === 1 ? "shadow-sm" : "card shadow-sm"}>
        <div className="card-header">{title}</div>
        <div className="card-header d-flex text-center align-items-center justify-content-center">
          <img
            src={utils.GetStaticFile(image)}
            alt={"ошибка загрузки"}
            className="img text-center img-fluid"
          />
        </div>
        <div className="card-body">
          <p className="card-text">{description}</p>
        </div>
        <a href={`/static/${instructions}`} className="stretched-link">
          download
        </a>
        <div className="card-footer">
          <div className="d-flex justify-content-between align-items-center">
            <div className="btn-group">
              <button
                type="button"
                className="btn btn-sm btn-outline-secondary"
              >
                {lindView}
              </button>
              <button
                type="button"
                className="btn btn-sm btn-outline-secondary"
              >
                {lindEdit}
              </button>
            </div>
            <small className="text-muted">{time}</small>
          </div>
        </div>
      </div>
    </div>
  );
}

export function BookView2({
  view,
  title,
  description,
  lindView,
  lindEdit,
  image,
  instructions,
  time = "0 минут",
}) {
  return (
    <div className="col-md-6">
    <div className="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
      <div className="col p-4 d-flex flex-column position-static">
        <strong className="d-inline-block mb-2 text-success">
        {title}
        </strong>
        <h3 className="mb-0">{lindView}</h3>
        <div className="mb-1 text-muted">{lindEdit} {time}</div>
        <p className="mb-auto">
          {description}
        </p>
        <a href={`/static${instructions}`} className="stretched-link">
          download
        </a>
      </div>
      <div className="col-auto d-none d-lg-block">
        <img
            src={utils.GetStaticFile(image)}
            alt={"ошибка загрузки"}
            className="bd-placeholder-img img-fluid"
            width="300"
            height={300}
          />
      </div>
    </div>
  </div>
  );
}