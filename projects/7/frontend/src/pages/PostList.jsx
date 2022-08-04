import React, { useState, useEffect, forwardRef, createRef, useRef } from "react";
import axios from "axios";
import PostItem from "./PostItem";
const PostList = () => {
  const [posts, setPosts] = useState({ data: [], page: 1 });
  const portion = 20;
  const totalPages = Math.ceil(100 / portion);
  const getNewPosts = () => {
    axios
      .get("https://jsonplaceholder.typicode.com/posts", {
        params: {
          _limit: portion,
          _page: posts.page,
        },
      })
      .then(({ data }) => {
        setPosts({
          data: [...posts.data, ...data], 
          page: posts.page + 1 
        });
      });
  };
//загрузка самой первой порции данных
useEffect(() => {
  getNewPosts();
}, []);

const lastItem = createRef();
const observerLoader = useRef();
const actionInSight = (entries) => {
  if (entries[0].isIntersecting && posts.page <= totalPages) {
    getNewPosts();
  }
};
//регистрируем на последний элемент наблюдателя, когда последний элемент меняется
useEffect(() => {
  if (observerLoader.current) {
    observerLoader.current.disconnect();
  }
  
  observerLoader.current = new IntersectionObserver(actionInSight);
  if (lastItem.current) {
    observerLoader.current.observe(lastItem.current);
  }
}, [lastItem]);
return (
 <div className="post-list">
   {posts.data.map((item, index) => {
     if (index + 1 === posts.data.length) {
       return <PostItem key={item.id} info={item} ref={lastItem} />;
     }
     return <PostItem key={item.id} info={item} />;
   })}
 </div>
);
};
export default PostList;