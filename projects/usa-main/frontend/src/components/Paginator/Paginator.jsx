import React , {useState} from "react";
import styles from './Paginator.module.css';
import cn from "classnames";  // npm install classnames //  classNames= {cn(styles.paginator, styles.selectedPages)}
                                  // classNames= {cn(styles.paginator, [styles.selectedPages]: true)}


let Paginator = ({totalUsersCount, pageSize, currentPage, onPageChanged, portionSize = 3}) => {

    console.log("Paginator");
    // console.log(totalIcereamsCount)
    // console.log(pageSize)
    console.log(currentPage)
    // console.log(portionSize)

    let pagesCount = Math.ceil(totalUsersCount / pageSize); //   12/4 =3

    let pages = [];
    for (let i = 1; i <= pagesCount; i++){
        pages.push(i);
    }

    let portionCount = Math.ceil(pagesCount / portionSize); //4
    let [portionNumber, setportionNumber] = useState(1);
    let leftPortionPageNumber = (portionNumber - 1) * portionSize + 1;
    let rightPortionPageNumber = portionNumber * portionSize

    return <div className={styles.paginator}>
        {portionNumber > 1 &&
            <button onClick={ () => { setportionNumber(portionNumber - 1)}}>PREV</button>}

                {pages 
                     .filter(p => p >= leftPortionPageNumber && p <= rightPortionPageNumber )
                        .map(p =>{
                            return <span className={ cn ({
                                [styles.selectedPage]: currentPage === p 
                            }, styles.pageNumber)}
                                key={p}
                                onClick={(e) => {
                                    onPageChanged(p);
                                }}>{p}</span>                            
                        })}
                {portionCount > portionNumber &&
                    <button onClick={() =>{setportionNumber(portionNumber + 1 )}}>NEXT</button> }
                    
    </div>
}

export default Paginator