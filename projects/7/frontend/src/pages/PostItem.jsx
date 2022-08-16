import React, { forwardRef } from "react";
import * as utils from '../components/utils'



const PostItem = forwardRef((props, ref) => {
  const content = `${props.info.id} ${props.info.title}`;

  return <div className="post-list__item" ref={ref}>

    {content}
    <div className="col-md-6">
    <div className="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
      <div className="col p-4 d-flex flex-column position-static">
        <strong className="d-inline-block mb-2 text-success">
        {props.info.title}
        </strong>
        <h3 className="mb-0">{props.info.lindView}</h3>
        <div className="mb-1 text-muted">{props.info.lindEdit} {props.info.time}</div>
        <p className="mb-auto">
          {props.info.description}
        </p>
        <a href={`/static${props.info.instructions}`} className="stretched-link">
          download
        </a>
      </div>
      <div className="col-auto d-none d-lg-block">
        <img
            src={utils.GetStaticFile(props.info.image)}
            alt={"ошибка загрузки"}
            className="bd-placeholder-img img-fluid"
            width="300"
            height={300}
          />
      </div>
    </div>
  </div>

    </div>;

});


export default PostItem;