import React, { useEffect } from 'react';
import s from './Home.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faYoutube} from '@fortawesome/free-brands-svg-icons'
import {faBars} from '@fortawesome/free-solid-svg-icons'

import Menu from '../menu/Menu';
import { useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom';
import Login from '../login/Login';




const Home = () => {
  

  const store = useSelector(state => state.authReducerR);

  const navigate = useNavigate();

  useEffect(() => {
    if (!store.isAuth) {   
      
      console.log("main useeffect")
      console.log(store.isAuth)
      console.log("main useeffect")
      navigate("/login");
    }
  }, []);



  
  // if (!store.isAuth) {

  //   console.log('/login')
  //   console.log(store.isAuth)
  //     //return(
  //       // redirect("/login")
  //       // <h1>login</h1>
  //       // <Route path='/login' element={ <Navigate to="/login" /> } />
      
    
  //   navigate("/login");
  //   console.log('/login')
        
  //   //  )
  // }

  const showState = () => {
    console.log(store)
  } 


  return ( 
 
    <div className={s.wrapper}>

    {/* { !store.isAuth && 
      // <Login />
      <h1>{store.isAuth}</h1>
     } */}

   
      
      <div className={s.menu}>
         <Menu/>  
      </div>
      
      <div className={s.mainBlock}>

        <h1>Главная страница!</h1>
        {/* <button onClick={showState}>проверка стате</button> */}
      </div>        
    </div>
  )
}

export default Home