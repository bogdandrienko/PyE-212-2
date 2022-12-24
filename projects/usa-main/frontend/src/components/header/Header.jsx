import React from 'react'
import s from './Header.module.css';
import { NavLink } from 'react-router-dom'

const Header = () => {
  return ( 
    <div className={`${s.wrapper}`}> 
             Lan Temir             
    </div>
  )
}

export default Header