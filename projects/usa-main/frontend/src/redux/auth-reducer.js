import axios from "axios";

import AuthService from "../services/AuthService" 
// import { useDispatch } from 'react-redux';



const SETAUTH = "SETAUTH";
const SETUSER = "SETUSER";


let initialState = {
    user : {},
    isAuth: false,
    
};


const authReducer = (state = initialState, action  ) =>{
    
    switch(action.type){ // switch ("LOAD") 
      
        case SETAUTH: {
            
            return{ ...state,  isAuth: action.isAuth};
        }

        case SETUSER: {
            return{ ...state,  isAuth: action.user};
        }
        // case DELETETOKEN: {
        //     return{ ...state,  load: false, token: null};
        // }
        


        // case ERROR: {
        //     return{load: false, token: undefined, error: "произошла ошибка" }
        // }
        default: return state;

    }
}

const setAuth = (isAuth) => ({type: SETAUTH, isAuth})


const setUser = (user) => ({type: SETUSER,  user})


export const requestLogin = async (userName, password, dispatch) => {  

 

    try{      
        const response = await AuthService.login(userName, password);    
        localStorage.setItem('token', response.data.access);      
        localStorage.setItem('refreshToken', response.data.refresh);    
        dispatch(setAuth(true));
        
      

        // console.log(response);
        // dispatch(setUser(response.data.user))

        console.log("auth-reducer")
        
        

        
    } catch (e) {
        console.log(e)
    }
}   

export const logout = async (dispatch ) => {  
    try{
       // const response = await AuthService.logout();
        localStorage.removeItem('token');
        localStorage.removeItem('refreshToken');
        dispatch(setAuth(false));
        //dispatch(setUser({}))
    } catch (e) {
        console.log(e.response?.data?.message)
    }
}

export default authReducer;


export const checkAuth = async (dispatch) => {

    

    try{ 
        
        const response = await axios.post('/api/token/refresh/', {
            "refresh": localStorage.getItem('refreshToken')
        } ) 

        console.log("checkAuth")
        console.log(response)
        localStorage.setItem('token', response.data.access);      
        localStorage.setItem('refreshToken', response.data.refresh);  
        dispatch(setAuth(true));        
    } catch (e) {
        console.log("ошибка checkAuth")
        console.log(e.response)
    } finally {
        
    }
}




// const LOAD = "LOAD";
// const SUCCESS = "SUCCESS";
// const ERROR = "ERROR";
// const DELETETOKEN = "DELETETOKEN";

// let initialState = {
//     load: false,
//     token: null,
//     error: false,
// };


// // Reducer - "Переключатель состояния хранилища"
// const authReducer = (state = initialState, action  ) =>{
    
//     switch(action.type){ // switch ("LOAD") 
//         case LOAD:{
//             return {"load": true}
//         }
//         case SUCCESS: {
//             return{ ...state,  load: false, token: action.token};
//         }
//         case DELETETOKEN: {
//             return{ ...state,  load: false, token: null};
//         }
        


//         case ERROR: {
//             return{load: false, token: undefined, error: "произошла ошибка" }
//         }
//         default: return state;

//     }
// }



// export const setToken = (token) => ({type: SUCCESS, token})
// export const deleteToken = () => ({type: DELETETOKEN})

// export const requestToken = (token, dispatch) => {  
//     dispatch(setToken(token))
//     localStorage.setItem('tokenHomeWork', token )
// }

// export const requestDeleteToken = (dispatch) => {
//     dispatch(deleteToken)
//     localStorage.removeItem('tokenHomeWork')
// }


// export default authReducer;