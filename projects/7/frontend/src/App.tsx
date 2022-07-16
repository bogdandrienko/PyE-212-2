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

function App() {
  return (
    // <BrowserRouter>
    //   <Routes>

    //     <Route path="/" element={<Home />}>
    //     </Route>

    //   </Routes>
    // </BrowserRouter>
    <div>Home</div>
  );
}

export default App;
