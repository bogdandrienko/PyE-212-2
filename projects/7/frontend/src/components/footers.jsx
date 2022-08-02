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
    <footer className="text-muted pt-3">
      <div className="container" id="hanging-icons">
    <h2 className="pb-2 border-bottom">Hanging icons</h2>
    <div className="row g-4 py-2 row-cols-1 row-cols-lg-3">
      <div className="col d-flex align-items-start">
        <div className="icon-square text-bg-light d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
          <svg className="bi" width="1em" height="1em"></svg>
        </div>
        <div>
          <h2>Featured title</h2>
          <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
          <a href="#" className="btn btn-primary">
            Primary button
          </a>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <div className="icon-square text-bg-light d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
          <svg className="bi" width="1em" height="1em"></svg>
        </div>
        <div>
          <h2>Featured title</h2>
          <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
          <a href="#" className="btn btn-primary">
            Primary button
          </a>
        </div>
      </div>
      <div className="col d-flex align-items-start">
        <div className="icon-square text-bg-light d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
          <svg className="bi" width="1em" height="1em"></svg>
        </div>
        <div>
          <h2>Featured title</h2>
          <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
          <a href="#" className="btn btn-primary">
            Primary button
          </a>
        </div>
      </div>
    </div>
  </div>
    </footer>
  );
}
