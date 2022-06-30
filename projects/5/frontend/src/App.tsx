import React from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import './App.css';
import Home from './pages/home';
import About from './pages/about';
import Login from './pages/login';
import Chat from './pages/Chat';
import "./css/my.css";
import "./css/bootstrap/bootstrap.css";
// import "static/css/font_awesome_6_0_0/css/all.min.css";
// import "static/css/font_zen/style.css";


function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Home />}>
        </Route>
        
        <Route path="/about" element={<About />}>
        </Route>

        <Route path="/login" element={<Login />}>
        </Route>

        <Route path="/chat" element={<Chat />}>
        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;
