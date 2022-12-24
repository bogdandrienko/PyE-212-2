import React, { useState, useEffect } from 'react'
import s from './Profile.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faYoutube } from '@fortawesome/free-brands-svg-icons'
import { faBars } from '@fortawesome/free-solid-svg-icons'
import { getProfile, updateProfile, uploadProfilePhoto  } from '../../redux/profile-reducer';
import Menu from '../menu/Menu';
import { useDispatch, useSelector } from 'react-redux';



const Profile = () => {

    const [usernameState, setusernameState] = useState('');
    const [emailState, setEmailState] = useState('');
    const [ava, setAvatar] = useState();

    const [avaShow, setAvaShow] = useState('');
    


    const dispatch = useDispatch();

    const profileStore = useSelector(state => state.profileReducerR);
    const {        
        email,
        username,
        
    } = profileStore.profile
    // const avatarRedux = profileStore.profile.avatar[0].avatar

    

    
    useEffect( () => {
    getProfile(dispatch); 
    // console.log(profileStore.profile.avatar.map(item => {
    //     console.log(item)
    // }))
    
  
    
    },[])

    useEffect( () => {
        setusernameState(username)     
        setEmailState(email)
        if (profileStore.avast == '' || profileStore.avast == null){
            console.log('/media/avatars/ava.jpg$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            setAvaShow('/media/avatars/ava.jpg')
        }else{
            setAvaShow(profileStore.avast)
            console.log("noooooooooooooooooooooooooo")
        }
        
    },[username,email,profileStore.avast])
     

    const uploadPhoto = (e) => {
        e.preventDefault()

       

   

        let formdata = new FormData()
        formdata.append('avatar', ava, ava.name);
        formdata.append('name', "avatarnew")


        console.log(formdata)




        // const uploadData = new FormData();
        // uploadData.append('file', imageProf, imageProf.name);
        // console.log(uploadData)

         uploadProfilePhoto(formdata, dispatch);
        

        // console.log("photo")
    }

    const OnupdateProfile = (e) => {
        e.preventDefault();


        console.log("updateProfile")
        updateProfile(emailState, dispatch)

    }


    const getUseSelector = (e) => {
        e.preventDefault();
        
        console.log(profileStore)
        console.log(profileStore.avast)

        console.log(avaShow)
    }

    const handleFile = (e) => {
        // console.log(e.target.files, "$$$$")
        // console.log(e.target.files[0], "$$$$")

        // let file = e.target.files[0]
        // setFile({file: file})
    }

    return (
        
        <div className={s.wrapper}>
            {/* {console.log("render") } */}
            <div className={s.menu}>
                <Menu />
            </div>

            <div className={s.mainBlock}>


                <div className={s.profileblock}>
                    <div className={s.profileImage}>
                      
                       
                        {/* <img src={profileStore.avast &&  profileStore.avast } /> */}
                        <img src={avaShow } />

                
                       
                        {/* <img src='/media/avatars/ava.jpg'  /> */}


                        <form onSubmit={uploadPhoto}>
                           

                            <input onChange={(e) => setAvatar(e.target.files[0])} type="file"  name="file" />
                            
                            <button className={s.btn}>загрузить фото </button>
                        </form>
                    </div>

                    <div className={s.profileForm}>
                        <form onSubmit={OnupdateProfile}>
                            <label>Логин</label>
                            <input type='text' onChange={(e)=>{setusernameState(e.target.value)}} value={usernameState} readOnly={false} />
                            
                            <label>Email</label>
                            <input type='text' onChange={(e)=>{setEmailState(e.target.value)}} value={emailState} placeholder='email' />
                            
                            <button className={s.btn}> Изменить</button>
                        </form>
                        
                    </div>

                    {/* <button onClick={getUseSelector}>useSelector</button> */}

                </div>






            </div>
        </div>
    )
}

export default Profile