import {useEffect} from 'react'
import styles from './items.module.css'

export default function Items(props) {  
    useEffect(() => {
      props.updateItems()
    }, [])
  
    const listItems = props.items.map((item) =>
      <Item item={item} updateItems={props.updateItems}/>
    );
    console.log(listItems)
     
    return (
      <div>
        {listItems}
      </div>
    );
}

function Item(props) {
    const deleteItem = () => {
      const request_body = {"id": props.item.id}
      fetch('http://localhost:8000/item/delete/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(request_body)
      })
      .then(response => response.json())
      .then(data => props.updateItems());
    }
    return <div className={styles.item}>
        <div className={styles.itemContent}>
            <div className={styles.itemName}>{props.item.itemName}</div>
            <div className={styles.itemDescription}>{props.item.description}</div>
            <button name="deleteItem" onClick={deleteItem}></button>
        </div>
    </div>
}