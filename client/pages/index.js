import { useState } from 'react';
import styles from '../styles/Home.module.css'

export default function Home() {
  const [state, setState] = useState({ show: false })

  const toggleModal = () => {
    setState({
      show: !state.show
    })
  }

  return (
    <div className={styles.container}>
      <button id={'add-item-button'} className={styles.blueButton} onClick={ () => { toggleModal() }}>Add your first item</button>
      <Modal show={state.show} hide={toggleModal}/>
    </div>
  )
}

function Modal(props) {
    if (!props.show){
      return null
    } else return (
      <div>
        <button onClick={() => props.hide()}>Hide</button>
        <div>Hello Modal</div>
        <input></input>
        <input></input>
        <select name="amount" id="amount">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
        </select>
        <button onClick={() => props.hide()}>Add Item</button>
      </div>
    )
}
