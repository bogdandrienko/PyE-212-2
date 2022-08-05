import React from 'react';
import logo from './logo.svg';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import './App.css';
import './css/my.css';

import Home from './pages/Home';

import About from './pages/About';
import News from './pages/News';

import Login from './pages/Login';
import Register from './pages/Register';
import Auth from './pages/Auth';
import PostList from './pages/PostList';
import {Categories} from './pages/Categories';

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

        <Route path="/posts" element={<PostList />}>
        </Route>

        <Route path="/categories" element={<Categories />}>
        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;
