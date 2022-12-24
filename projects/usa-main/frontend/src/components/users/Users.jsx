import React, { useState, useEffect } from 'react'
import s from './Users.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faYoutube } from '@fortawesome/free-brands-svg-icons'
import { faBars } from '@fortawesome/free-solid-svg-icons'
import { requestUsers } from '../../redux/user-reducer';



import Menu from '../menu/Menu';
import { useDispatch, useSelector } from 'react-redux';
import Paginator from '../Paginator/Paginator'



const Users = () => {

    
    const dispatch = useDispatch();
   

    const usersStore = useSelector(state => state.userReducerR);
    const{
        users,
        pageSize,
        totalUsersCount,
        currentPage,
        isFetching,
        followingInProgress
    } = usersStore

    
    useEffect( () => {
     requestUsers(1,dispatch, pageSize)
    
    },[])

    const onPageChanged = (currentPage) => {
        requestUsers(currentPage, dispatch, pageSize)    
      }
    
     

  
    // const getUsers = (e) => {
    //     e.preventDefault();

    //     console.log('getUsers')
    //     requestUsers(1, 3, dispatch)
    // }


    // const selectorTest = () => {
    //     console.log(usersStore)
    // }

    

    return (
        <div className={s.wrapper}>

            <div className={s.menu}>
                <Menu />
            </div>

            <div className={s.mainBlock}>


                <div >
                   <h3>Пользователи</h3>
                     {/* <button onClick={getUsers}>get users</button>
                    <button onClick={selectorTest}>selector Test</button> */}
                </div>                
                    {users && users.map(item => {
                        return <div className={s.usersBlock}>
                                    <div className={s.userImgBlock}>
                                        <img src={item.avatar[0].avatar ? item.avatar[0].avatar : '/media/avatars/ava.jpg' }></img>
                                     
                                    </div>

                                    <div className={s.userTextBlock}>
                                         <p>{item.username}</p>
                                       
                                    </div>
                                 </div>
                    })  }
                
                
            <div className={s.paginator}>
                
                <Paginator currentPage={currentPage} totalUsersCount={totalUsersCount} pageSize={pageSize} onPageChanged={onPageChanged}/>
            </div>
                






            </div>
        </div>
    )
}

export default Users