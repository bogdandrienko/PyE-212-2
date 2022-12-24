import $api from "../http";

export default class PostService{
    static async getPosts(currentPage, pageSize, postid){
        const resp = $api.get('/api/mypost/', {
            params: {currentPage: currentPage, pageSize: pageSize, postid: postid}})
        return resp
    }

    static async getPost(postid){
        const resp = $api.get('/api/mypost/', {
            params: {postid: postid}})
        return resp
    }

    // static async getCategoryVideos() {
    //     const resp = $api.get('/api/videocategory/')
    //     return resp 
    // }
}