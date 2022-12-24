import PostService from "../services/PostService"

const SET_POSTS = 'SET_POSTS';
const SET_CURRENT_PAGE_POSTS = 'SET_CURRENT_PAGE_POSTS';
const SET_TOTAL_POSTS_COUNT = 'SET_TOTAL_POSTS_COUNT';


let initialState = {
    posts: [],
    pageSize: 3,
    totalPostsCount: 0,
    currentPage: 1,
};

const postsReducer = (state = initialState, action) => {

    switch (action.type){
        case SET_POSTS:{
            return{...state, posts: action.posts}
        }
        case SET_CURRENT_PAGE_POSTS: 
            return{
                ...state, currentPage: action.currentPage
            }
        case SET_TOTAL_POSTS_COUNT:
            return{
                ...state, totalPostsCount: action.totalPostsCount
            }

        default:
            return state;        
    }

}

export const setPosts = (posts) => ({type: SET_POSTS, posts})
export const setCurrentPageAction = (currentPage) => ({type: SET_CURRENT_PAGE_POSTS, currentPage})
export const setTotalPostsCount = (totalPostsCount) => ({type: SET_TOTAL_POSTS_COUNT, totalPostsCount})


export const requestPosts = async (currentPage, dispatch, pageSize, postid) => {  

    const response  = await PostService.getPosts(currentPage, pageSize, postid)
    
    console.log(response.data)

    dispatch(setCurrentPageAction(currentPage))
    dispatch(setTotalPostsCount(response.data.conterPosts))

    dispatch(setPosts(response.data.posts))
}

export default postsReducer