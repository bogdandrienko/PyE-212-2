import React from 'react'
import s from './Video.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faYoutube } from '@fortawesome/free-brands-svg-icons'
import { faSortDown } from '@fortawesome/free-solid-svg-icons'

import { requestVideos, requestCurrentCategory } from '../../redux/video-reducer';

import Menu from '../menu/Menu';
import { useEffect } from 'react';

import { useDispatch, useSelector } from 'react-redux';
import Paginator from '../Paginator/Paginator'

const Video = () => {

    const dispatch = useDispatch();

    const videoStore = useSelector(state => state.videoReducerR);

    const{
        videos,
        pageSize,
        totalVideoCount,
        currentPage,
        isFetching,
        followingInProgress,
        category,
        currentCategory
    } = videoStore
    
    
    useEffect( () =>{
        requestVideos(1, dispatch, pageSize, 0)

    },[])

    useEffect( () =>{
        requestVideos(1, dispatch, pageSize, currentCategory)

    },[currentCategory])

    const onPageChanged = (currentPage) => {
        requestVideos(currentPage, dispatch, pageSize, currentCategory)    
      }

    const testState = () => {
        console.log(videoStore)
    }

    return (
        <div className={s.wrapper}>

            <div className={s.menu}>
                <Menu />
            </div>


            <div className={s.mainBlock}>

                <h1>Видео </h1>

                <div className={s.topListCategory}>
                    <ul>
                        <li onClick={() => requestCurrentCategory(0, dispatch)}><FontAwesomeIcon icon={faSortDown} /> все категории</li>
                        {category && category.map(item => {
                            return(
                                <li onClick={() => requestCurrentCategory(item.id, dispatch)} key={item.id}><FontAwesomeIcon icon={faSortDown} /> {item.title}</li>
                            )
                        }) }
                       
                    </ul>

                </div>
                
                  
             

                <div className={s.videoBlockMain}>

                    {videos && videos.map(item => {
                        return(
                            <div key={item.id} className={s.videoBlock}>
                                <iframe width="100%" height="200px" src={"https://www.youtube.com/embed/"+item.url_from_youtube} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>
                                <p> {item.title}</p>
                            </div>
                        )
                    })}

                   


             

                </div>   

                {/* <button onClick={testState}>test state</button>  */}

                <div className={s.paginator}>
                
                     <Paginator currentPage={currentPage} totalUsersCount={totalVideoCount} pageSize={pageSize} onPageChanged={onPageChanged}/>
                </div>           

            </div>
        </div>
    )
}

export default Video