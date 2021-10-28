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

  return (
    <div className={styles.container}>
      <Navbar />
      <Modal />
      {/* <button id={'add-item-button'} className={styles.blueButton} onClick={ () => { toggleModal() }}>Add your first item</button> */}
      {/* <Modal show={state.show} hide={toggleModal}/> */}
      <Items items={state.items}/>
    </div>
  )
}