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
import News from './pages/News';

import Login from './pages/Login';
import Register from './pages/Register';
import Auth from './pages/Auth';

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Home />}>
        </Route>

        <Route path="/news" element={<News />}>
        </Route>

        <Route path="/auth" element={<Auth />}>
        </Route>

        <Route path="/about" element={<About />}>
        </Route>

        <Route path="/login" element={<Login />}>
        </Route>

        <Route path="/register" element={<Register />}>
        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;
