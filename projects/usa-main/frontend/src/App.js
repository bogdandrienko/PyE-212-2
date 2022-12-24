import logo from './logo.svg';
import './App.css';
import{BrowserRouter, Routes, Route,} from "react-router-dom";
// import{BrowserRouter, Routes, Route,} from "react-router-dom";
import Header from './components/header/Header';
import Home from './components/home/Home';
import Register from './components/register/Register';
import Login from './components/login/Login';
import Video from './components/video/Video';
import Profile from './components/profile/Profile';
import Users from './components/users/Users';
import Exchange from './components/exhange/Exchange';
import { useSelector, useDispatch } from 'react-redux'
import React, { useEffect } from 'react';

import { checkAuth, logout } from './redux/auth-reducer';
import Posts from './components/posts/posts';
import Post from './components/post/post';






const App = () => {

  const store = useSelector(state => state.authReducerR);
  const dispatch = useDispatch()
  

  // if (!store.isAuth) {
   

  //   console.log("asdadasdasdad")
  //   console.log(store.isAuth)
  //   console.log("asdadasdasdad2")
     
  //   { <Navigate to="/login" /> }
    
  // }

  useEffect( () => {
    if(localStorage.getItem('token')){
      // store.checkAuth()
      console.log("useEffectAPP");
      checkAuth(dispatch)      
    }    

    


  },[store.isAuth])

  
  

  return (

   

    <div className='app-wrapper'>    
      
      {/* <h3>{store.isAuth ? `Пользователь авторизован проверка: ${store.isAuth
      } `: 'АВТОРИЗУЙТЕСЬ'} </h3> */}

      


      <BrowserRouter>
      <Routes>        
      
          <Route path='/' element={<Home />}></Route>   
          <Route path='/register' element={<Register/>} ></Route>
          <Route path='/login' element={<Login/>} ></Route>

          {/* <Route path='/login' element={ !store.isAuth ? <Navigate to="/login" /> : <Login /> }> </Route> */}

          <Route path='/video' element={<Video/>} ></Route>
          <Route path='/profile' element={<Profile/>} ></Route>     
          <Route path='/users' element={<Users/>} ></Route>    
          <Route path='/exchange' element={<Exchange/>}> </Route>
          
          <Route path='/post/:id' element={<Post/>}></Route>
          <Route path='/posts' element={<Posts/>}></Route>  
        </Routes>     
      </BrowserRouter>

      

    </div>
  
  )
}

export default App;


