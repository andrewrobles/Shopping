import {useState, useEffect} from 'react'
import styles from './items.module.css'

export default function Items(props) {
    const [state, setState] = useState({
      items: []
    })
  
    useEffect(() => {
      getItems()
    })
  
    const getItems = () => {
      fetch('http://localhost:8000/item/')
      .then(response => response.json())
      .then(data => saveItems(data));
    }
  
    const saveItems = (items) => {
      if (items != state.items) {
        setState({
          items: items
        })
      }
    }
  
    const listItems = state.items.map((item) =>
      <Item item={item}/>
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
      .then(data => console.log(data));
    }
    return <div className={styles.item}>
        <div className={styles.itemContent}>
            <div className={styles.itemName}>{props.item.itemName}</div>
            <div className={styles.itemDescription}>{props.item.description}</div>
            <button name="deleteItem" onClick={deleteItem}></button>
        </div>
    </div>
}