import PostService from "../services/PostService"

const SET_POST = 'SET_POST';



let initialState = {
    post: {}    
};

const postReducer = (state = initialState, action) => {

    switch (action.type){
        case SET_POST:{
            return{...state, post: action.post}
        }
        default:
            return state;        
    }

}

export const setPost = (post) => ({type: SET_POST, post})


export const requestPost = async (postid, dispatch) => {  

    const response  = await PostService.getPost(postid)
    
    console.log(response.data)

   

    dispatch(setPost(response.data.post))
}

export default postReducer