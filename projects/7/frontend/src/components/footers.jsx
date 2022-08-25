import React from "react";

export function Footer1() {
  return (
    <footer className="footer mt-auto py-3 bg-light">
      <div className="container">
        <span className="text-muted">Place sticky footer content here.</span>
      </div>
    </footer>
  );
}

export function Footer2() {
  return (
    <footer className="text-muted">
      <div class="px-4 text-center">
      <img class="d-block mx-auto mb-4" src="/static/bootstrap-themes.png" alt="" className="img img-fuild w-25"/>
      <h1 class="display-5 fw-bold">Centered hero</h1>
      <div class="col-lg-6 mx-auto">
        <p class="lead mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
      </div>
    </div>
    </footer>
  );
}
