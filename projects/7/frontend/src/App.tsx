import React from 'react';
import logo from './logo.svg';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import { Counter } from './features/counter/Counter';
import './App.css';
import Home from './pages/Home';
import About from './pages/About';
import Login from './pages/Login';

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

      </Routes>
    </BrowserRouter>
  );
}

export default App;
