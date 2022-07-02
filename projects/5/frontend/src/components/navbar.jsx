import React from 'react';
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
    <a className="navbar-brand" href="#">Navbar</a>
    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>

    <div className="collapse navbar-collapse" id="navbarColor01">
      <ul className="navbar-nav mr-auto">
        <li className="nav-item active">
          <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
        </li>
        <li className="nav-item">
          <Link to="/" className='btn btn-lg btn-outline-primary m-1'>Home</Link>
        </li>
        <li className="nav-item">
          <Link to="/about" className='btn btn-lg btn-outline-primary m-1'>About</Link>
        </li>
        <li className="nav-item">
          <Link to="/login" className='btn btn-lg btn-outline-primary m-1'>Login</Link>
        </li>
        <li className="nav-item">
          <Link to="/chat" className='btn btn-lg btn-outline-primary m-1'>Chat</Link>
        </li>
        <li className="nav-item">
          <Link to="/redux" className='btn btn-lg btn-outline-primary m-1'>Redux</Link>
        </li>
      </ul>
      <form className="form-inline">
        <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"/>
        <button className="btn btn-outline-info my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
  )
}

