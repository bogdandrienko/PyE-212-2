import React, { forwardRef } from "react";
const PostItem = forwardRef((props, ref) => {
  const content = `${props.info.id} ${props.info.title}`;
  return <div className="post-list__item" ref={ref}>{content}</div>;
});
export default PostItem;