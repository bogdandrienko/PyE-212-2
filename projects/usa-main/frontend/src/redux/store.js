import {applyMiddleware, combineReducers, compose, createStore} from "redux";
import thunkMiddleware from 'redux-thunk';


import authReducer from './auth-reducer';
import profileReducer from './profile-reducer';
import userReducer from './user-reducer';
import videoReducer from './video-reducer';
import postsReducer from './posts-reducer';
import postReducer from './post-reducer'



let reducers = combineReducers({
    authReducerR: authReducer,
    profileReducerR: profileReducer,
    userReducerR: userReducer,
    videoReducerR: videoReducer,
    postsReducerR: postsReducer,
    postReducerR: postReducer  
})

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose; 
const store = createStore(reducers, composeEnhancers( applyMiddleware(thunkMiddleware)));


window.__store__ = store;

export default store;