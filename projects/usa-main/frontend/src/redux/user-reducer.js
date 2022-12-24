import UserService from "../services/UserService";

const SET_USERS = "SET_USERS";
const SET_CURRENT_PAGE_USER = "SET_CURRENT_PAGE_USER"
const SET_TOTAL_USER_COUNT = "SET_TOTAL_USER_COUNT"
const SET_PAGE_SIZE = "SET_PAGE_SIZE"

let initialState={
    users: [],
    pageSize: 3,
    totalUsersCount: 0,
    currentPage: 1,
    isFetching: true,
    followingInProgress: []
};

const userReducer = (state = initialState, action) => {
    switch(action.type){
        case SET_USERS:{
            return{...state, users: action.users}
        }
        case SET_CURRENT_PAGE_USER:{
            return{
                ...state, currentPage: action.currentPage
            }
        }
        case SET_TOTAL_USER_COUNT: {
            return{
                ...state, totalUsersCount: action.totalUsersCount
            }
        }
        case SET_PAGE_SIZE: {
            return{
                ...state, pageSize: action.pageSize
            }
        }
        default:
            return state;
    }
}

export const setUsers = (users) => ({type: SET_USERS, users})
export const setCurrentPageAction = (currentPage) => ({type: SET_CURRENT_PAGE_USER, currentPage})
export const setPageSizeAction = (pageSize) => ({type: SET_PAGE_SIZE, pageSize})
export const setTotalUserCount = (totalUsersCount) => ({type: SET_TOTAL_USER_COUNT, totalUsersCount})

export const requestUsers = async (currentPage, dispatch, pageSize)  => {
    // return async (dispatch) => {
        console.log('requestUsers')

       const response = await UserService.getUsers(currentPage, pageSize)
        console.log(response.data.datausers)
        
        dispatch(setCurrentPageAction(currentPage))
        dispatch(setTotalUserCount(response.data.datausers.countUser))
        dispatch(setPageSizeAction(pageSize))
        dispatch(setUsers(response.data.datausers.users))
    // }
}

export default userReducer;