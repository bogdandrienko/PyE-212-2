import React, { useContext, useState } from 'react'
import s from './Login.module.css';
import Header from '../header/Header';
import { Link, NavLink } from 'react-router-dom'
import axios from 'axios';
import avatarp from '../../../src/static/frontimage/ava.jpg'

import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { requestLogin } from '../../redux/auth-reducer';
import { useEffect } from 'react';






 const Login = () => {

    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');

    const [showError, setShowError] = useState('');
    const [showErrorStatus, setShowErrorStatus] = useState('');

    const store = useSelector(state => state.authReducerR);
    const dispatch = useDispatch()
    const navigate = useNavigate();
 


//   const {
//     icecreams,
//     pageSize: pageSize,
//     totalIcereamsCount,
//     currentPage,
//   } = iceCreamStore

// const api = axios.create({   
//     headers: {
//         "token" : "5bfa63ed-8ed3-4d5b-97e1-6f862dc30e08"
//     }
// });

// api.interceptors.request.use( (config) => {
//     config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`
//     return config
// })

    

    useEffect(() => {
        if (store.isAuth) {   
            
            console.log("store.isAuth")
            console.log(store.isAuth)
            navigate("/");
        }
      }, [store.isAuth]);



    const onLogin = (e) => {
        e.preventDefault();

        console.log(userName)
        console.log(password)

        requestLogin(userName, password, dispatch);

        

        // requestLogin(userName, password ).then(
        //     response =>{

        //         console.log(response.data)
              
        //       // requestToken(response.data.access, dispatch)
        //       // console.log(response)
        //       // console.log(response.data)
        //       // console.log(response.status)
  
        //       //navigate('/');
        //     }
        //   ).catch(
        //     error => {
        //         console.log(error)
        //     //   console.log(error.response.data.detail)
        //     //   console.log(error.response.status)
        //     //   setShowError(error.response.data.detail)
        //     //   setShowErrorStatus(error.response.status)
        //     }
        //   )
    }


    const showState = () => {
        console.log(store)
    }

    const settingState = (e) => {
        e.preventDefault();
        

        // navigate('/');

   
    }

    return (

        <div className={`${s.wrapper}`}>            
            <form className={s.formLogin} onSubmit={onLogin}>
                <div className={`${s.imgcontainer}`}  >
                    <img src={avatarp} alt="Avatar" className={`${s.avatar}`} />
                </div>

                <div className={s.container}>
                    <label className={s.labellog}> <b>Логин</b></label>
                    <input onChange={ (e) => setUserName(e.target.value)} value={userName} className={s.inputformLogin} type="text" placeholder="Введите логин"  required />

                    <label  className={s.labellog}><b>Пароль</b></label>
                    <input onChange={ (e) => setPassword(e.target.value)} value={password} className={s.inputformLogin} type="password" placeholder="Введите пароль"  required />

                    <button className={s.logButton} type="submit">ВОЙТИ</button>
                </div>

                <div className={`${s.container} ${s.containercolor} `}  >
                   <NavLink type="submit"  className={s.cancelbtn} to="/register"  >Регистрация</NavLink>
                    
                   <span className={s.psw}> <Link href="#">Забыли пароль?</Link></span>
                </div>
            </form>
            
            
            <button onClick={showState}>проверка стате</button>


     

        </div>
    )
}

export default Login







