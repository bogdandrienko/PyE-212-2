import React from "react";

export function BookMainView({
  title,
  description,
  lindView,
  lindEdit,
  image,
  time = "0 минут",
}) {
  return (
    <div className="col col-12 col-sm-12 col-md-6 col-lg-6">
      <div className="card shadow-sm">
        <div className="card-header">{title}</div>
        <img src={`/static/${image}`} alt={"ошибка загрузки"} className="img img-fluid" />

        <div className="card-body">
          <p className="card-text">{description}</p>
          
        </div>
        <div className="card-footer">
        <div className="d-flex justify-content-between align-items-center">
            <div className="btn-group">
              <button type="button" className="btn btn-sm btn-outline-secondary">
                {lindView}
              </button>
              <button type="button" className="btn btn-sm btn-outline-secondary">
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
