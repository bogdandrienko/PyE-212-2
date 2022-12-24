import VideoService from "../services/VideoService"

const SET_VIDEOS = "SET_VIDEOS";
const SET_CURRENT_PAGE_VIDEO = "SET_CURRENT_PAGE_VIDEO";
const SET_TOTAL_VIDEO_COUNT = "SET_TOTAL_VIDEO_COUNT";
const SET_PAGE_SIZE_VIDEO = "SET_PAGE_SIZE_VIDEO";
const SET_CATEGORY_VIDEO = "SET_CATEGORY_VIDEO";
const SET_CURRENT_PAGE_VIDEO_CATEGORY = "SET_CURRENT_PAGE_VIDEO_CATEGORY";

let initialState={
    videos: [],
    pageSize: 3,
    totalVideoCount: 0,
    currentPage: 1,
    isFetching: true,
    followingInProgress: [],
    category: [],
    currentCategory: 0
};

const videoReducer = (state = initialState, action) => {
    switch(action.type){
        case SET_VIDEOS:{
            return{...state, videos: action.videos}
        }
        case SET_CURRENT_PAGE_VIDEO:{
            return{...state, currentPage: action.currentPage}
        }
        case SET_TOTAL_VIDEO_COUNT: {
            return{...state, totalVideoCount: action.totalVideoCount}
        }
        case SET_PAGE_SIZE_VIDEO: {
            return{
                ...state, pageSize: action.pageSize
            }
        }
        case SET_CURRENT_PAGE_VIDEO_CATEGORY: {
            return{
                ...state, currentCategory: action.currentCategory
            }
        }
        case SET_CATEGORY_VIDEO: {
            return{
                ...state, category: action.category
            }
        }
       
        default:
            return state;
    }
}

export const setVideos = (videos) => ({type: SET_VIDEOS, videos})
export const setCurrentPageAction = (currentPage) => ({type: SET_CURRENT_PAGE_VIDEO, currentPage})
export const setTotalVideoCount = (totalVideoCount) => ({type: SET_TOTAL_VIDEO_COUNT, totalVideoCount})
export const setPageSizeAction = (pageSize) => ({type: SET_PAGE_SIZE_VIDEO, pageSize})
export const setCategory = (category) => ({type: SET_CATEGORY_VIDEO, category})

export const setCurrentCategory = (currentCategory) => ({type: SET_CURRENT_PAGE_VIDEO_CATEGORY, currentCategory})


export const requestVideos = async (currentPage, dispatch, pageSize, categoryid) => {
    console.log('requestVideo')
    const response = await VideoService.getVideo(currentPage, pageSize, categoryid)
    console.log(response.data) 

    dispatch(setCurrentPageAction(currentPage))
    dispatch(setTotalVideoCount(response.data.conterVideos))
    dispatch(setPageSizeAction(pageSize))
    dispatch(setVideos(response.data.videos))
    dispatch(setCategory(response.data.categoryVideos))
}

export const requestCurrentCategory = (currentCategory, dispatch) => {
    dispatch(setCurrentCategory(currentCategory))
}



// export const requestCategoryVideo = async () => {
//     const response = await VideoService.getCategoryVideos()
//     console.log(response.data)
// }

export default videoReducer;