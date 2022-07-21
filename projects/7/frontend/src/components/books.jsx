import React from "react";

export function BookMainView({
  title,
  description,
  lindView,
  lindEdit,
  time = "0 минут",
}) {
  return (
    <div class="col col-12 col-sm-12 col-md-6 col-lg-6">
      <div class="card shadow-sm">
        <div className="card-header">{title}</div>
        <img src={"/static/logo512.png"} alt={"ошибка загрузки"} />

        <div class="card-body">
          <p class="card-text">{description}</p>
          
        </div>
        <div className="card-footer">
        <div class="d-flex justify-content-between align-items-center">
            <div class="btn-group">
              <button type="button" class="btn btn-sm btn-outline-secondary">
                {lindView}
              </button>
              <button type="button" class="btn btn-sm btn-outline-secondary">
                {lindEdit}
              </button>
            </div>
            <small class="text-muted">{time}</small>
          </div>
        </div>
      </div>
    </div>
  );
}
