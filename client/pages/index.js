import { useState, useEffect } from 'react';
import styles from '../styles/Home.module.css'

import Navbar from '../components/navbar/navbar'
import Items from '../components/items/items'
import Modal from '../components/modal/modal'

export default function Home() {
  const [state, setState] = useState({ 
    show: false,
    items: []
  })

  const toggleModal = () => {
    setState({
      show: !state.show,
      items: state.items
    })  
  }

  const setItems = (items) => {
    setState({
      show: state.show,
      items: items
    })
  }

  const updateItems = () => {
    fetch('http://localhost:8000/item/')
    .then(response => response.json())
    .then(data => setItems(data));
  }

  return (
    <div className={styles.container}>
      <Navbar />
      <Modal setItems={setItems}/>
      <Items items={state.items} updateItems={updateItems}/>
    </div>
  )
}