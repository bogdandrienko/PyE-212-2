import React from 'react'
import s from './Posts.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faYoutube } from '@fortawesome/free-brands-svg-icons'
import { faSortDown } from '@fortawesome/free-solid-svg-icons'


import { requestPosts } from '../../redux/posts-reducer';

import Menu from '../menu/Menu';
import { useEffect } from 'react';

import { useDispatch, useSelector } from 'react-redux';
import Paginator from '../Paginator/Paginator'
import { Link } from 'react-router-dom';

const Posts = () => {
    const dispatch = useDispatch();

    const postStore = useSelector(state => state.postsReducerR);

    const{
        posts,
        pageSize,
        totalPostsCount,
        currentPage,
    } = postStore

    useEffect ( () => {
        requestPosts(1, dispatch, pageSize, 0)
    },[])

    const onPageChanged = (currentPage) => {
        requestPosts(currentPage, dispatch, pageSize, 0)    
      }

    const testRequest = (e) => {
        e.preventDefault()

        requestPosts(currentPage, dispatch, pageSize, 0)    

    }

    const testState = (e) => {
        e.preventDefault()

        console.log(postStore)

    }


    return (
        <div className={s.wrapper}>

            <div className={s.menu}>
                <Menu />
            </div>


            <div className={s.mainBlock}>

                <h1>Посты </h1>

              
                <div className={s.videoBlockMain}>

                    

                    {posts && posts.map(item => {
                        return (

                            
                            <div key={item.id} className={s.videoBlock}>  
                            <Link to={`/post/${item.id}`}>
                                <img src={item.image_url} />                              
                                <p> {item.title}</p>
                            </Link>
                                
                            </div>
                        )
                    })}






                </div>
{/* 
                <button onClick={testRequest}>test request</button>
                    <button onClick={testState}>test testState</button> */}

               

                
                <div className={s.paginator}>

                    <Paginator currentPage={currentPage} totalUsersCount={totalPostsCount} pageSize={pageSize} onPageChanged={onPageChanged} />
                </div>

            </div>
        </div>
    )

}

export default Posts