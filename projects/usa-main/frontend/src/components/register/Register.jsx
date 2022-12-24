import React, { useState, useEffect } from 'react'
import s from './Register.module.css';
import axios from 'axios';
import { Link, NavLink } from 'react-router-dom'

import { Navigate } from 'react-router-dom';


function Register() {

    const [name, setName] = useState('');  
    const [password, setPassword] = useState('');
    const [redirect, setRedirect] = useState(false);
    const [errorShow, setErrorShow] = useState('')


    const submit =  (e) => {
        e.preventDefault();

        //  let data = new FormData();
        //  data.append("email",  email);
        //  data.append("subject", subject);
        //  data.append("message", message);

        //  axios.post('/api/sendemail/', data)
        //     .then(res => console.log(res))
        //     .catch(errors => console.log(errors))

        // await axios('/api/register/', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify({
        //         name,               
        //         password
        //     })
        // })


        axios.post("/api/registration/", {"username": name, "password": password }).then(
            response =>{
                console.log(response)
                setErrorShow("Пользователь уиешно добавлен")
             
            
        }).catch(er => {
            console.log (er.response.data.errormessage)
            // console.log ("ошибка")
             setErrorShow("ошибка: " + er.response.data.errormessage)
        })

        // const content = await response.json();
        // console.log(content);
      
    }


    return (
        <div className={`${s.wrapper}`}>

                <div className={s.h1}>
                     <h1>Регистрация</h1>
                </div>
                

                <form className={s.formLogin} onSubmit={submit}>
                    <input className={s.inputformLogin} onChange={(e) => setName(e.target.value)} value={name} type="text" placeholder='Логин' />              
                    <input className={s.inputformLogin} onChange={(e) => setPassword(e.target.value)} value={password} type="password" placeholder='Пароль' />
                    <button className={s.regButton}>РЕГИСТРАЦИЯ</button>
                </form>
                
                   

                

                <div className={`${s.container} ${s.containercolor} `}  >
                   <NavLink type="submit"  className={s.cancelbtn} to="/login"  >У меня уже есть логин</NavLink>  
                   <div className={s.errorshow}>
                    { errorShow && <h2>{errorShow}</h2>}
                    </div>                  
                </div>
           
        </div>
    )
}

export default Register