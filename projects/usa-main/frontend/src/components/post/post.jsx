import React from 'react'
import s from './Post.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faYoutube } from '@fortawesome/free-brands-svg-icons'
import { faSortDown } from '@fortawesome/free-solid-svg-icons'


// import { requestPosts } from '../../redux/posts-reducer';

import Menu from '../menu/Menu';
import { useEffect } from 'react';

import { useDispatch, useSelector } from 'react-redux';
import Paginator from '../Paginator/Paginator';
import {useParams} from "react-router-dom";
import { requestPost } from '../../redux/post-reducer';

const Post = () => {
    const {id} = (useParams())
    const dispatch = useDispatch();

    const postStore = useSelector(state => state.postReducerR);

    const{
        post       
    } = postStore

    useEffect ( () => {
        requestPost(id, dispatch)
    },[])

    // const onPageChanged = (currentPage) => {
    //     requestPosts(currentPage, dispatch, pageSize, 0)    
    //   }

    const testRequest = (e) => {
        e.preventDefault()

        requestPost(id, dispatch)    

    }

    // const testState = (e) => {
    //     e.preventDefault()

    //     console.log(postStore)

    // }


    return (
        <div className={s.wrapper}>

            <div className={s.menu}>
                <Menu />
            </div>


            <div className={s.mainBlock}>

               

              
                <div className={s.videoBlockMain}>

                    
                    <div className={s.contentBlock}>
                        <h1>{post.title} </h1>
                        <img src={post.image_url} />

                        {/* <img src='https://thumbs.dfs.ivi.ru/storage15/contents/7/e/a778cc2d8c23c8c9ea46287764fbf6.jpg/858x483/?q=60' /> */}
                        
                      
                        <p>{post.description}
                        </p>
              
                        
                    </div>

                    {/* {posts && posts.map(item => {
                        return (
                            <div key={item.id} className={s.videoBlock}>  
                                <img src={item.image_url} />                              
                                <p> {item.title}</p>
                            </div>
                        )
                    })} */}






                </div>

                {/* <button onClick={testRequest}>test request</button> */}
                    {/* <button onClick={testState}>test testState</button> */}
                    {/* <button onClick={testState}>test testState</button> */}

               

                
               

            </div>
        </div>
    )

}

export default Post