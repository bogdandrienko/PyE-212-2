import React from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import './App.css';
import Home from './pages/Home';
// import "static/css/font_awesome_6_0_0/css/all.min.css";
// import "static/css/font_zen/style.css";


function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Home />}>
        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;
